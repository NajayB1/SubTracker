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