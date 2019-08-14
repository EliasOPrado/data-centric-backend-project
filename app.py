
#Imports
import os
from flask import Flask, render_template, redirect, request, url_for
#----mongoDB---- 
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
#
app = Flask(__name__)

#App configuration -- table name and the link
app.config['MONG_DBNAME'] = ''
app.config['MONGO_URI'] = ''
                            

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', 
    #to display three products of each category using for loop
    )
    
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
    
@app.route('/login')
def login():
    return render_template('login.html')

#add methods as needed\    
@app.route('/register')
def register():
    return render_template('register.html')
    
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