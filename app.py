from flask import Flask

app = Flask(__name__)
@app.route('/')
def HelloWorld():
    return '你好世界'

if __name__ == '__main__':
    app.run(debug=True)
