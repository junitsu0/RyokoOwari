from app import app
from flask import render_template
from app.forms import SignUpForm

@app.route('/')
def index():
    #this could be a database instead of dictionary
    user_info = {
        'username': 'justin',
        'email': 'jumanjiro@gmail.com'
    }
    colors = ['Blackjack', 'Baccarat', 'Roulette', 'Craps', 'Three Card Poker', 'Four Card Poker', "Ultimate Texas Hold'em"]
    return render_template('index.html', user=user_info, colors=colors)


@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)