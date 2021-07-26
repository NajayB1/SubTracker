# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request


# -- Initialization section --
app = Flask(__name__)
#maraidb_connection = mariadb.connect(user='chooseAUserName', password='chooseAPassword', database='Login')

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html") 

@app.route('/features') 
def features():
    return render_template('newindex.html') 

@app.route('/subscriptions') 
def subscriptions():
    return render_template('subscription.html')

@app.route('/budgeting')  
def budgeting():
    return render_template('budgeting.html') 

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html') 

@app.route('/home')
def home():
    return render_template('home.html') 