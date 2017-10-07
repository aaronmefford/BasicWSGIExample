
BasicWSGIExample
^^^^^^^^^^^^^^^^

These are a few basic Web form processing scripts to illustrate the fundamentals of recieving processing and responding to web requests in Python.

Each example will display a form, process the requst submitted by the form, and display the submitted data on a result page.

cgi.py
  A simple raw CGI script that will run with a web server that supports CGI like Apache.

low.py
  A low-level script that uses Werkzeug and can be used with WSGI or present it's own web server.

server.py
  A more advanced Werkzeug script that can be used with WSGI or present it's own web server.  It uses templates to display the form and result page.

To install the dependencies run
  ./setup.py install

  
