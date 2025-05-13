from flask import Flask, render_template, redirect, request, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'kusbahkey'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []

    return render_template("index.html", gold=session['gold'], activities=session['activities'])

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    time = datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')

    if building == 'farm':
        gold_earned = random.randint(10, 20)
    elif building == 'cave':
        gold_earned = random.randint(5, 10)
    elif building == 'house':
        gold_earned = random.randint(2, 5)
    elif building == 'casino':
        gold_earned = random.randint(-50, 50)
    else:
        gold_earned = 0

    session['gold'] += gold_earned

    if gold_earned >= 0:
        activity = f"<li style='color:green;'>Earned {gold_earned} gold from the {building}! ({time})</li>"
    else:
        activity = f"<li style='color:red;'>Entered a {building} and lost {gold_earned} gold... Ouch. ({time})</li>"

    session['activities'].insert(0, activity)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)