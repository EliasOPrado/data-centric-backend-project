
#Imports
import os
from flask import Flask, render_template, redirect, request, url_for
#----mongoDB---- 
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
#
app = Flask(__name__)

#App configuration -- table name and the link
app.config['MONG_DBNAME'] = 'DB_ecommerce'
app.config['MONGO_URI'] = 'mongodb+srv://elias:kb01210012@myfirstcluster-uyvei.mongodb.net/DB_ecommerce?retryWrites=true'
                            

mongo = PyMongo(app)

#you need to set the home under this route.
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
    
#category 1 
@app.route('/eletronics')
def eletronics():
    return render_template('eletronics.html', eletronics=mongo.db.eletronics.find())

#category 2 
@app.route('/home_garden')
def home_garden():
    return render_template('home_garden.html')

#category 3 
@app.route('/motors')
def motors():
    return render_template('motors.html')
    
@app.route('/login')
def login():
    return render_template('login.html')

#add methods as needed\    
@app.route('/register')
def register():
    return render_template('register.html')
    

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)