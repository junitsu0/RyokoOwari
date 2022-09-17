from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'suck-it-trebek'


from . import routes

