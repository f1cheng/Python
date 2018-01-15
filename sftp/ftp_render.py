# !/usr/bin/env python
# coding:utf-8

from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, AnyOf


from flask_bootstrap import Bootstrap
from sftp import MySFTP

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Don\'t test others'
bootstrap = Bootstrap(app)

class FtpForm(FlaskForm):
    host = StringField('Host')
    port = StringField('Port')
    username = StringField('Username')
    pwd = PasswordField('Pwd')
    localPath = StringField('LocalPath')
    remotePath = StringField('RemotePath')

@app.route('/', methods=['POST', 'GET'])
def file_transfer():
    ftpForm = FtpForm()
    print('request method={}'.format(request.method))

    if request.method == 'GET':
        return render_template('file_ftp.html', form=ftpForm) 

    if ftpForm.validate_on_submit():
        result = 0
        print('request methodpst={}.btn={}'.format(request.method, request.form['btn']))
        host = ftpForm.host.data
        port = ftpForm['port'].data
        username = ftpForm['username'].data
        pwd = ftpForm['pwd'].data
        localpath = ftpForm['localPath'].data
        remotepath = ftpForm['remotePath'].data
         
        if request.form['btn'] == 'download':
            try:
                myFtp = MySFTP(host, int(port), username, pwd)
                result = myFtp.download_file(remotepath, localpath)
            except Exception as e:
                result = e
        else:
            print("not implemented for upload")
 
        return render_template('file_ftp.html', form=ftpForm, re=result) 


if __name__ == '__main__':
    app.run(debug=True)

'''

    myFtp = MySFTP(host, int(port), username, pwd)
    #myFtp = MySFTP("127.0.0.1", 22, 'fred', 'charging')

    myFtp.download_file(remotepath, localpath)
    #myFtp.download_file('/home/fred/workspace/test/a.t', '/home/fred/workspace/test/html.t')

    return render_template('transfer.html', **locals())
'''
