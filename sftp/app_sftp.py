# !/usr/bin/env python
# coding:utf-8

from flask import Flask, request, render_template
from sftp import MySFTP

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('transfer.html')

@app.route('/transfer', methods=['POST'])
def transfer():
    host = request.form['host']
    port = request.form['port']
    username = request.form['username']
    pwd = request.form['pwd']
    localpath = request.form['localpath']
    remotepath = request.form['remotepath']

    myFtp = MySFTP(host, int(port), username, pwd)
    #myFtp = MySFTP("127.0.0.1", 22, 'fred', 'charging')

    myFtp.download_file(remotepath, localpath)
    #myFtp.download_file('/home/fred/workspace/test/a.t', '/home/fred/workspace/test/html.t')

    return render_template('transfer.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
