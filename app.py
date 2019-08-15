#Imports
import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import bcrypt

app = Flask(__name__)

#App configuration -- table name and the link
app.config['MONG_DBNAME'] = ''
app.config['MONGO_URI'] = ''
                            

mongo = PyMongo(app)


@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    return render_template('index.html')
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST': 
        return render_template('login.html')
    else:
        user = mongo.db.user
        login_user = user.find_one({'name': request.form.get('username')})
    
        if login_user:
            if bcrypt.hashpw(request.form.get('password').encode('utf8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form.get('username')
                return redirect(url_for('index'))
       
        return 'Invalid username or password combination'

#Code reference Antony Hebert 
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        user = mongo.db.user
        existing_user = user.find_one({'name':request.form['username']})
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            user.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return render_template('index.html')
        
        return 'That Username already exist!'
    
    return render_template('register.html')
    
#category 1 Eletronics
@app.route('/eletronics')
def eletronics():
    return render_template('eletronics.html', 
    #Will only retrive data from the category_name: Eletronics
    #Name changed to facilitate the display on the main page
    electronics=mongo.db.products.find({'category_name':"Eletronics"}))

#category 2  Home & Garden
@app.route('/home_garden')
def home_garden():
    return render_template('home_garden.html',
    #Will only retrive data from the category_name: Home & Garden (dont forget the space)
    #Name changed to facilitate the display on the main page
    homeGarden=mongo.db.products.find({'category_name':"Home & Garden"}))

#category 3 Motors
@app.route('/motors')
def motors():
    return render_template('motors.html', 
    #Will only retrive data from the category_name: Motors
    #Name changed to facilitate the display on the main page
    mottors=mongo.db.products.find({'category_name':"Motors"}))
    
    
    
@app.route('/user')
def user():
    return render_template('user.html', category=mongo.db.category.find())

    
@app.route('/insert_product', methods=['POST'])
def insert_product():
    products=mongo.db.products
    products.insert_one(request.form.to_dict())
    return redirect(url_for('home'))


    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)