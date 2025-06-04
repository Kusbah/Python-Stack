from django.shortcuts import render ,redirect
from random import randint
from datetime import datetime
# Create your views here.

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'index.html')

def process_money(request):
    bullding = request.POST['bullding']
    time = datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')
    if bullding == "farm":
        gold_earn = randint(10,20)
    elif bullding == "cave":
        gold_earn = randint(10,20)
    elif bullding == "house":
        gold_earn = randint(10,20)
    elif bullding == "quest":
        gold_earn = randint(-50,50)
    request.session['gold'] += gold_earn
    if gold_earn >= 0:
        activity = f"<li style='color:green;'>You entered a {bullding} and earned  {bullding} gold. ({time})</li>"
    else:
        activity = f"<li style='color:red;'>you failed a {bullding} and lost {gold_earn} gold Ouch. ({time})</li>"
    request.session['activities'].insert(0, activity)
    return redirect('/')