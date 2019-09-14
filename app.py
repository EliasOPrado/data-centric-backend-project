#Imports
import os
import math
from flask import Flask, render_template, redirect, request, url_for, session, jsonify
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId 
import bcrypt
import datetime

app = Flask(__name__, static_url_path='/static')


#App configuration -- table name and the link
app.secret_key = 'any random string'
app.config['MONG_DBNAME'] = 'DB_ecommerce_project'
app.config['MONGO_URI'] = 'mongodb+srv://elias:kb01210012@myfirstcluster-uyvei.mongodb.net/DB_ecommerce_project?retryWrites=true'
                            

mongo = PyMongo(app)



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
            return render_template('register.html',  error="user_exists")
        else:
            mongo.db.user.insert_one(user)
            return render_template('login.html', user=user, password=password)

    return render_template('register.html')
    
#READ FUNCTIONS FOR EACH CATEGORIES   
#category 1 Eletronics
@app.route('/electronics/')
@app.route('/electronics/<page>/<limit>')
def electronics(page=1, limit=6):
    page=int(page)
    limit=int(limit)
    skip = page * limit - limit
    maximum = math.ceil( (mongo.db.products.count_documents({})) / limit)
    electronics = list(mongo.db.products.find({'category_name':"Electronics"}).sort("$natural", pymongo.DESCENDING).skip(skip).limit( limit ))
    return render_template(
        'electronics.html', 
        electronics=electronics,
        page=page,
        pages=range(1, maximum + 1),
        maximum=maximum, limit=limit,
       
    )

#category 2  Home & Garden
@app.route('/home_gardens/', methods=['GET', 'POST'])
@app.route('/home_gardens/<page>/<limit>', methods=['GET', 'POST'])
def home_garden(page=1, limit=6):
    limit = int(limit)
    page = int(page)
    skip = page * limit - limit
    maximum = math.ceil( (mongo.db.products.count_documents({})) / limit)
    homeGarden = list(mongo.db.products.find({'category_name':"Home & Garden"}).sort("$natural", pymongo.DESCENDING).skip(skip).limit( limit ))
    return render_template(
        'home_garden.html',
        homeGarden=homeGarden,
        page=page,
        pages=range(1, maximum + 1),
        maximum=maximum, limit=limit)

#category 3 Motors
@app.route('/motors/')
@app.route('/motors/<page>/<limit>')
def motors(page=1, limit=6):
    limit = int(limit)
    page = int(page)
    skip = page * limit - limit
    maximum = math.ceil( (mongo.db.products.count_documents({})) / limit)
    motors = list(mongo.db.products.find({'category_name':"Motors"}).sort("$natural", pymongo.DESCENDING).skip(skip).limit( limit ))
    return render_template(
        'motors.html',
        motors=motors,
        page=page,
        pages=range(1, maximum + 1),
        maximum=maximum, limit=limit
    )
    
    
@app.route('/view/product_id?=<id>')
def view(id):
    mongo.db.products.find_one_and_update({"_id": ObjectId(id)}, {"$push": {"views": 1}})
    return render_template('product.html')
    
    
#REVIEW FUNCTION
@app.route('/review/product_id?=<id>', methods=['POST', 'GET'])
def review(id):
    now = datetime.datetime.now()
    #have to fix no-logged user error
    name=session['name']
    print_post=request.form.get('review')
    #Gets the product clicked on its link and display on the product.html page
    reviews = mongo.db.products.find_one({"_id": ObjectId(id)})
    if request.method == 'POST':
        mongo.db.products.find_one_and_update({"_id": ObjectId(id)},{
                    '$push':{'review':{
                    'name': name,
                    'post': print_post,
                    'date': now.strftime("%d/%m/%Y")
                    }
                }
            }
        )
        #try to redirect to product.html
        return redirect(url_for('index'))
    #Increments +1 view into the visited product by its id.
    mongo.db.products.find_one_and_update({"_id": ObjectId(id)}, {"$inc": {"views": 1}})
    return render_template('product.html', reviews=reviews)

   
#FORM TO CREATE NEW PRODUCT                                                   
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
    products.insert_one(request.form.to_dict())
    return redirect(url_for('index'))
    
    
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
    return redirect(url_for('index'), )

    
@app.route('/edit_product/<product_id>')
def edit_product(product_id):
    the_product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    all_categories = mongo.db.category.find()
    return render_template('editproduct.html', product=the_product, categories=all_categories)

    
#DELETE FUNCTION  
@app.route('/delete_product/<product_id>')
def delete_product(product_id):
    mongo.db.products.remove({'_id':ObjectId(product_id)})
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)