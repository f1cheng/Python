# !/usr/bin/env python
# coding:utf-8

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return '<form action="/echo" method="POST"><input name="text"><input type="submit" value="Echo"></form>'
    return render_template('echo.html')

@app.route('/echo', methods=['POST'])
def echo():
    #return "you said: " + request.form['text']
    return render_template('echo.html', texts = request.form['text'])

if __name__ == '__main__':
    app.run(debug=True)
