#!/bin/env python

from werkzeug.formparser import parse_form_data
from werkzeug.utils import escape

def test_form(environ, start_response):
    result = ['<title>Test Form</title>']
    if environ['REQUEST_METHOD'] == 'POST':
        form = parse_form_data(environ)[1]
        result.append('''
            <p>Your request has been received for processing: %s
        ''' % escape(form['url']).encode('utf-8'))
    else: 
        result.append('''
            <form method="post">
                <p>URL: <input type="text" name="url" size="20">
                <input type="submit" >
            </form>
        ''')
    result = ''.join(result)
    print result
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return result

def main():
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 8128, test_form)

if __name__ == '__main__': main()
# vim:sw=4:ts=4:et
