from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def empty():
    return "empty"

@app.route('/play/<int:num>/<color>')
def play(num, color):
    return render_template("index.html", num1 = num, color1 = color)

if __name__ == "__main__":
    app.run(debug=True)