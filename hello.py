#!/usr/bin/python
#cython: language_level=2
from flask import Flask, request, escape

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

#acessar /greet?name=wfp
@app.route('/greet')
def greet():
    name = request.args['name']
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <h1>Hi {}</h1>
    </body>
    </html>'''.format(escape(name))


app.run()
