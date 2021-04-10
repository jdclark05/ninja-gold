from flask import Flask , render_template, request, redirect, session, flash 
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key='159487263'

@app.route('/')
def index():
    if 'user_gold' not in session:
        session['user_gold'] = 0
    else:
        user_gold=session['user_gold']
    if 'live_update' not in session:
        live_update = ""
    else:
        live_update=session['live_update']
    return render_template("index.html", user_gold=session['user_gold'], live_update=live_update)

@app.route('/process_money', methods=['POST'])
def process_money():
    date = datetime.now()
    difference = 0
    win_lose = ""
    activity_update1 = ""
    activity_update2 = ""
    user_gold=session['user_gold']
    if 'live_update' in session:
        live_update = session['live_update']
    else:
        live_update = []
    if request.form['building'] == 'farm':
        user_gold += random.randrange(10,21)
        difference = user_gold - session['user_gold']
        activity_update1 = f" Earned {difference} gold from the {request.form['building']} ---- {date}!"
        live_update.append({ "text": activity_update1, "color": "green" })
        print(live_update)
    if request.form['building'] == 'cave':
        user_gold += random.randrange(5,11)
        difference = user_gold - session['user_gold']
        activity_update1 = f" Earned {difference} gold from the {request.form['building']}! ---- {date}"
        live_update.append({ "text": activity_update1, "color": "green" })
        print(live_update)
    if request.form['building'] == 'house':
        user_gold += random.randrange(2,6)
        difference = user_gold - session['user_gold']
        activity_update1 = f" Earned {difference} gold from the {request.form['building']}! ---- {date}"
        live_update.append({ "text": activity_update1, "color": "green" })
        print(live_update)
    if request.form['building'] == 'casino':
        user_gold += random.randrange(-50,50)
        if user_gold < session['user_gold']:
            win_lose = 'lost'
            difference = user_gold - session['user_gold']
            activity_update2 = f"Entered the {request.form['building']} and {win_lose} {difference} gold! ---- {date}"
            live_update.append({ "text": activity_update2, "color": "red" })
            print(live_update)
        elif user_gold > session['user_gold']:
            win_lose = "won"
            difference = user_gold - session['user_gold']
            activity_update2 = f"Entered the {request.form['building']} and {win_lose} {difference} gold! ---- {date}"
            live_update.append({ "text": activity_update2, "color": "green" })
            print(live_update)
        else:
            win_lose = "broke even - "
            difference = user_gold - session['user_gold']
            activity_update2 = f"Entered the {request.form['building']} and {win_lose} {difference} gold! ---- {date}"
            live_update.append({ "text": activity_update2, "color": "black" })
            print(live_update)
        print(live_update)
    session['live_update'] = live_update
    session['user_gold'] = user_gold
    return redirect('/')

@app.route('/reset')
def reset():
    session['user_gold'] = 0
    session['live_update'] = []
    return redirect('/')
app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)