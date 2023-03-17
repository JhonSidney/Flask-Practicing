from flask import Flask 

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=""):
    return "<h1> Seja bem vindo{} </h1>".format(name)

@app.route('/blog/')
@app.route('/blog/<int:postID>')
def blog(postID):
    if postID >= 2:
        return "blog info {}".format(postID)
    else:
        return " blog todo"

if __name__ == '__main__':
    app.run()