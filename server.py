#!/bin/env python

#Adapted from an example at 
#http://werkzeug.pocoo.org/docs/0.12/tutorial/#introducing-shortly


import os
import urlparse
from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from jinja2 import Environment, FileSystemLoader

class TestForm(object):

    def __init__(self, config):
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                    autoescape=True)

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def default_route(self, request):
        print "default_route"
        return self.render_template('index.html')

    def process(self,request):
        print "process"
        return self.render_template('results.html',url = request.form['url'])

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        print request.path
        routes = {
            '/process': self.process,
        }
        response = None
        if request.path in routes:
            response = routes[request.path](request)
        else:
            response = self.default_route(request)

        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

def main():
    from werkzeug.serving import run_simple
    app =  TestForm({})
    run_simple('127.0.0.1', 8128, app)

if __name__ == '__main__': main()
# vim:sw=4:ts=4:et
