from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"


@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route('/say/<string:name>')
def Say_Flask(name):
    return f"Hi {name}"
# @app.route('/say/<michael>')
# def Say_Michael():
#     return "Hi Michael"
# @app.route('/say/<john>')
# def Say_John():
#     return "Hi John"


@app.route('/repeat/<int:num>/<string:word>')
def Repeat_Word(num, word):
    fullString = ""
    for x in range(0,num):
        fullString += f"{word} "
    return fullString



if __name__ == "__main__":
    app.run(debug = True)