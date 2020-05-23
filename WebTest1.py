from flask import Flask

app = Flask(__name__)


@app.route('/Sreshta')
def hello_world():
    return 'Hello, SB farmers new World...saturday!'

if __name__ == "__main__":
    app.run()
