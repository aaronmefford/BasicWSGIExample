# BasicWSGIExample

Here is some more detailed information about the scripts I have written.  I do not consider myself a programmer, I create these little programs as experiments to have a play with the language, or to solve a problem for myself.  I would gladly accept pointers from others to improve the code and make it more efficient, or simplify the code.  If you would like to make any comments then please feel free to email me at craig@geekcomputers.co.uk.

In the scripts the comments etc are lined up correctly when they are viewed in [Notepad++](https://notepad-plus-plus.org/). This is what I use to code Python scripts.

BasicWSGIExample
^^^^^^^^^^^^

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

  
