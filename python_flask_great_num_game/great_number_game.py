from flask import Flask, flash, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'rando'

@app.route('/')
def index():
    if 'num' not in session:
        num = random.randint(1,101)
        session['num'] = num
        print (session['num'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def checknum():
    session['guess'] = int(request.form['guess'])
    print (session['num'])
    print (session['guess'])
    if session['guess'] == session['num']:
        flash ("you win!")
    if session['guess'] > session['num']:
        flash('Too high, try a lower number')
    elif session['guess'] < session['num']:
        flash('Too low, try a higher number')
    
        
    
    return redirect('/')
    

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    session.clear()
    return redirect ('/')

app.run(debug=True)