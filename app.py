from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_word():
    return '<h1>hello teste</h1>'

if __name__ == '__main__':
    app.run