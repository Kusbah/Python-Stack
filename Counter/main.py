from flask import Flask,render_template,redirect,session

app = Flask(__name__)
app.secret_key= 'kusbahkey'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template("index.html",count=session['count'])
@app.route('/destroy_session')
def clear_seesion():
    session.clear()
    return redirect('/')
@app.route('/add_two', methods=['POST'])
def add_two():
    session['count'] += 1
    return redirect('/')





if __name__ == "__main__":
    app.run(debug=True)