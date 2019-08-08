
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
app.config['MONGO_URI'] = 'mongodb+srv://2@myfirstcluster-uyvei.mongodb.net/DB_ecommerce?retryWrites=true'
                            

mongo = PyMongo(app)

#you need to set the home under this route.
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', 
    #to display three products of each category using for loop
    letronics=mongo.db.eletronics.find(),
    home_garden=mongo.db.home_garden.find(),
    motors=mongo.db.motors.find())
    
#category 1 
@app.route('/eletronics')
def eletronics():
    
    return render_template('eletronics.html', eletronics=mongo.db.eletronics.find())

#category 2 
@app.route('/home_garden')
def home_garden():
    return render_template('home_garden.html', home_garden=mongo.db.home_garden.find())

#category 3 
@app.route('/motors')
def motors():
    return render_template('motors.html', motors=mongo.db.motors.find())
    
@app.route('/login')
def login():
    return render_template('login.html')

#add methods as needed\    
@app.route('/register')
def register():
    return render_template('register.html')
    
@app.route('/user')
def user():
    return render_template('user.html')
    

#@app.route('/insert_product', methods='POST')
#def insert_product():
#    if request.method == "POST":
#        if request.form.get('category') == "electronics":
#            form = request.form.to_dict()
#            mongo.db.electronics.insert_one(form)
#        elif request.form.get('category') == 'home_garden':
#            form = request.form.to_dict()
#            mongo.db.home_garden.insert_one(form)
#            return redirect('home_garden')
#        else:
#            form = request.form.to_dict()
#            mongo.db.motors.insert_one(form)
#            return redirect('home')
#        return render_template('insert_product.html')
        
    

#Insert for Eletronics -------------------------
@app.route('/insert_eletronic', methods=['POST'])
def insert_eletronic():
    eletronics=mongo.db.eletronics
    eletronics.insert_one(request.form.to_dict())
    product_name=request.name.get('product_name')
    price=request.name.get('price')
    product_description=request.get('product_description')
    eletronics.insert({'product_name':product_name, 'price':price, 'product_description':product_description})
    return redirect(url_for('eletronics'))

#Insert for Home & Garden ----------------------    
@app.route('/insert_hg', methods=['POST'])
def insert_hg():
    home_garden=mongo.db.home_garden
    home_garden(request.form.to_dict())
    product_name=request.name.get('product_name')
    price=request.name.get('price')
    product_description=request.get('product_description')
    home_garden.insert({'product_name':product_name, 'price':price, 'product_description':product_description})
    return redirect(url_for('home_garden'))
    
#Insert for Motors -------------------------
@app.route('/insert_motors', methods=['POST'])
def insert_motors():
    motors=mongo.db.motors
    motors.insert_one(request.form.to_dict())
    product_name=request.name.get('product_name')
    price=request.name.get('price')
    product_description=request.get('product_description')
    motors.insert({'product_name':product_name, 'price':price, 'product_description':product_description})
    return redirect(url_for('motors'))
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)