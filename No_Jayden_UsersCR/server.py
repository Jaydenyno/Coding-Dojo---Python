from flask import Flask, render_template, request, redirect, session
# from mysqlconnection import connectToMySQL
from users import Users

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def user_list():
    return render_template('read.html', users=Users.get_all())

@app.route('/users/new')
def user_info():
    return render_template('create.html')

@app.route('/process', methods=["POST"])
def adding_user():
    print(request.form)
    Users.save(request.form)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)