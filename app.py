from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'ni hao, root!'

@app.route('/user/<userid>')
def user_user(userid):
    return 'hello %s' % (userid)

@app.route('/user/')
def user_list():
    lista = ['f1', 'f2', 'f3', 'f4',
             '\n', '\0', '\n', '\r\n',
             'f5', 'f6', 'f7', 'f8']
    return '<h1> user id list =%s <h1>'% (str(lista))
    '''return str(lista)'''

if __name__ == '__main__':
    app.run(debug=True)
