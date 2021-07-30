# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo
from flask import redirect
from flask import session, url_for
# -- Initialization section --
app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

app.config['MONGO_DBNAME'] = 'Login'
app.config['MONGO_URI'] = 'mongodb+srv://admin:3RP94GXQX8IwtUVR@cluster0.1yjuq.mongodb.net/Login?retryWrites=true&w=majority'

mongo = PyMongo(app) 


# -- Routes section --
@app.route('/')
@app.route('/index', methods=["GET", "POST"]) 
def index():
    #connect to db
    collection = mongo.db.Signup
    #find all the data
    signup = collection.find({}) 
    return render_template('index.html', signup = signup) 

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


@app.route('/signups', methods=['GET', 'POST']) 
def signup():
    if request.method == 'POST':
        print("here") 
        users = mongo.db.Signup
        print(users) 
        exsisting_user = users.find_one({"Name":request.form["username"]})  
        
        if exsisting_user is None:
            users.insert({"Name":request.form["username"], "Password":request.form["password"]})
            session['username'] = request.form['username']
            return redirect(url_for('index')) 
        return 'The username already exists'
    return render_template('signups.html')  

 
def login():
    
    users = mongo.db.users
    login_user = users.find_one({'Name': request.form['username']}) 
    if login_user:
        if request.form['password'] == login_user['password']:
            session['username'] = request.form['username']
            session['email'] = request.form['email'] 
            return redirect(url_for('index')) 
    return 'Invalid username/password combination' 



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
       
 