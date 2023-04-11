from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '비밀 키'

@app.route('/')
def index():
    if not 'num' in session:
        session['num'] = 0
    print(type(session['num']))
    session['num'] += 1
    return  render_template('index.html')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    session['num'] += 1
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)