#!/bin/env python

import os, sys, re

hex='0123456789abcdef'
def decode_form_value(value):
    return re.sub(r'''%([0-9a-fA-F]{2})''',
        lambda x:
            chr(int(
                16 * hex.find(x.group(1).lower()[0])
                   + hex.find(x.group(1).lower()[1])
            )),
        value
    )

def read_form_data():
    form = {}
    data = sys.stdin.read()
    if data:
        data = [ x.split('=') for x in data.strip().split('&')]
        for key, value in data:
            form[key] = decode_form_value(value)
    return form

print "Content-Type: text/html"
print
print ('<title>Test Form</title>')

if os.environ['REQUEST_METHOD'] == 'POST':
    form = read_form_data()
    print("<p>Your request has been received for processing: ")
    print(form['url'])
else:
    print('''
            <form method="post">
                <p>URL: <input type="text" name="url" size="20">
                <input type="submit" >
            </form>
        ''')
# vim:sw=4:ts=4:et
