from app import app
from flask import render_template


@app.route('/')
def index():
    #this could be a database instead of dictionary
    user_info = {
        'username': 'justin',
        'email': 'jumanjiro@gmail.com'
    }
    colors = ['x', 'y', 'z', 'a', 'b', 'c']
    return render_template('index.html', user=user_info, colors=colors)


@app.route('/test')
def test():
    return 'This is a test'