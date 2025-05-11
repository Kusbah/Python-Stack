from flask import Flask,render_template,redirect,request,session
import random

app = Flask(__name__)
app.secret_key = 'kusbehkey'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['message'] = ''
    print(session['number'])
    return render_template('index.html', message=session.get('message', ''))

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])

    if guess < session['number']:
        session['message'] = 'Too low!'
    elif guess > session['number']:
        session['message'] = 'Too high!'
    else:
        session['message'] = f'Correct! The number was {session["number"]}.'
    
    return redirect('/')

@app.route('/play_again')
def play_again():
    session.clear()
    return redirect('/')





if __name__ == "__main__":
    app.run(debug=True)