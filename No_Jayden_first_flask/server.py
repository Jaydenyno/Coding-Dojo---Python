from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route('/dogs')
def dogs():
    return "Dogs are cool"

if __name__ == "__main__":
    app.run(debug = True)