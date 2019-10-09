#Imports
from __future__ import division
import os
import math
from flask import Flask, render_template, redirect, request, url_for, session, jsonify
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId 
import datetime


app = Flask(__name__, static_url_path='/static')


#App configuration -- table name and the link
app.secret_key = 'any random string'
app.config['MONG_DBNAME'] = 'DB_ecommerce_project'
app.config['MONGO_URI'] = 'mongodb+srv://elias:kb01210012@myfirstcluster-uyvei.mongodb.net/DB_ecommerce_project?retryWrites=true'
                            

mongo = PyMongo(app)


#Main page
@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    return render_template('index.html',
    aside_products=mongo.db.products.find(),
    electronics=mongo.db.products.find({'category_name':"Electronics"}),
    homeGarden=mongo.db.products.find({'category_name':"Home & Garden"}),
    motors=mongo.db.products.find({'category_name':"Motors"}))
    
#LOGIN FUNCTION    
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET': 
        return render_template('login.html')
    else:
        user = mongo.db.user
        login_user = user.find_one({
        'email': request.form.get('email'), 
        'password':request.form.get('password'
        )})
        
        if login_user:
            session['email'] = login_user['email']
            session['name'] = login_user['name']
            return redirect(url_for('user'))
       
        return 'Invalid username or password combination'
        
#LOGOUT FUNCTION
@app.route('/logout')
def logout():
    session['email'] = None
    session['name'] = None
    return redirect(url_for('login'))

#REGISTER FUNCTION
@app.route('/register', methods=['POST', 'GET'])
def register():
    email = session.get('email')
    if email:
      return redirect(url_for('index'))
    
    user = None
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = {'name': name, 'email': email, 'password': password}

        if mongo.db.user.find_one({"email": email}):
            return render_template('register.html')
        else:
            mongo.db.user.insert_one(user)
            return render_template('login.html')

    return render_template('register.html')
    
#category 1 Eletronics
@app.route('/electronics/')
@app.route('/electronics/<page>/<limit>')
def electronics(page=1, limit=6):
    page=int(page)
    limit=int(limit)
    start_index = page * limit - limit
    end_index = start_index + 6
    all_products = mongo.db.products.find({'category_name':"Electronics"}).sort("$natural", pymongo.DESCENDING)
    page_number =math.ceil(all_products.count()/6)
    maximum = math.floor( (mongo.db.products.count_documents({})) / limit - 1)
    electronics =  all_products[start_index:end_index]
    return render_template(
        'electronics.html', 
        electronics= electronics,
        page=page,
        pages=range(1, int(page_number)+1),
        maximum=maximum, 
        limit=limit
    )


#category 2  Home & Garden
@app.route('/home_garden/')
@app.route('/home_garden/<page>/<limit>')
def home_garden(page=1, limit=6):
    limit = int(limit)
    page = int(page)
    start_index = page * limit - limit
    end_index = start_index + 6
    all_products = mongo.db.products.find({'category_name':"Home & Garden"}).sort("$natural", pymongo.DESCENDING)
    page_number =math.ceil(all_products.count()/6)
    maximum = math.floor( (mongo.db.products.count_documents({})) / limit - 1)
    homeGarden = all_products[start_index:end_index]
    return render_template(
        'home_garden.html',
        homeGarden=homeGarden,
        page=page,
        pages=range(1, int(page_number)+1),
        maximum=maximum, limit=limit)

#category 3 Motors
@app.route('/motors/')
@app.route('/motors/<page>/<limit>')
def motors(page=1, limit=6):
    limit = int(limit)
    page = int(page)
    start_index = page * limit - limit
    end_index = start_index + 6
    all_products = mongo.db.products.find({'category_name':"Motors"}).sort("$natural", pymongo.DESCENDING)
    page_number =math.ceil(all_products.count()/6)
    maximum = math.floor( (mongo.db.products.count_documents({})) / limit -1)
    motors = all_products[start_index:end_index]
    return render_template(
        'motors.html',
        motors=motors,
        page=page,
        pages=range(1, int(page_number) + 1),
        maximum=maximum, limit=limit
    )
    
    
#REVIEW FUNCTION
@app.route('/review/product_id?=<id>', methods=['POST', 'GET'])
def review(id):
    now = datetime.datetime.now()
    print_post=request.form.get('review')
    #Gets the product clicked on its link and display on the product.html page
    reviews = mongo.db.products.find_one({"_id": ObjectId(id)})
    if request.method == 'POST':
        mongo.db.products.find_one_and_update({"_id": ObjectId(id)},{
                    '$push':{'review':{
                    'name': session['name'],
                    'post': print_post,
                    'date': now.strftime("%d/%m/%Y")
                    }
                }
            }
        )
        return redirect(url_for('review', id=id))
    #Increments +1 view into the visited product by its id.
    mongo.db.products.find_one_and_update({"_id": ObjectId(id)}, {"$inc": {"views": 1}})
    return render_template('product.html', reviews=reviews)
    
@app.route('/delete_comment/product_id?=<id>/post_content?=<post_content>')
def delete_comment(id, post_content):
    print('post_content',post_content)
    mongo.db.products.update({"_id": ObjectId(id)},{
        '$pull':{'review':{
            'post':post_content
            }
        }
    })
    return redirect(url_for('review', id=id))

#USER PAGE                                                 
@app.route('/user')                                                             
def user():
    items=mongo.db.products.find({'seller':session.get('name')})
    category=mongo.db.category.find()
    email = session.get('email')
    if not email:
        return redirect(url_for('login'))
    return render_template('user.html', category=category, items=items)


#CREATE FUNCTION
@app.route('/insert_product', methods=['POST'])
def insert_product():
    products=mongo.db.products
    if request.method == 'POST':
        form_dict = request.form.to_dict()
        form_dict.update({'seller': session['name']})
        products.insert_one(form_dict)
    return redirect(url_for('user'))
    
    
#UPDATE FUNCTION
@app.route('/update_product/<product_id>', methods=['POST'])
def update_product(product_id):
    products = mongo.db.products
    products.update({'_id': ObjectId(product_id)},
        {
        'category_name':request.form.get('category_name'),
        'product_name':request.form.get('product_name'),
        'price':request.form.get('price'),
        'url':request.form.get('url'),
        'seller':request.form.get('seller'),
        'product_description': request.form.get('product_description'),
        })
    return redirect(url_for('user'))

#EDIT FUNCTION - RETRIVES ONLY THE USER'S PRODUCT TO THE TEMPLATE   
@app.route('/edit_product/<product_id>')
def edit_product(product_id):
    seller = session['name']
    if not seller:
        return redirect(url_for('register'))
    try:
        the_product = mongo.db.products.find_one({"_id": ObjectId(product_id), 'seller':seller})
        all_categories = mongo.db.category.find()
    except:
        return redirect(url_for('index'))
    return render_template('editproduct.html', product=the_product, categories=all_categories)

    
#DELETE FUNCTION  
@app.route('/delete_product/<product_id>')
def delete_product(product_id):
    seller = session['name']
    if not seller:
        return redirect(url_for('register'))
    try:
        mongo.db.products.delete_one({'_id':ObjectId(product_id), 'seller':seller})
    except:
        return redirect(url_for('index'))
    return redirect(url_for('user'))

    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
