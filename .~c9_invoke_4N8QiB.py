#Imports
import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import bcrypt
import datetime

app = Flask(__name__)

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
@app.route('/electronics')
def electronics():
    return render_template('electronics.html', 
    electronics=mongo.db.products.find({'category_name':"Electronics"}))

#category 2  Home & Garden
@app.route('/home_garden')
def home_garden():
    return render_template('home_garden.html',
    homeGarden=mongo.db.products.find({'category_name':"Home & Garden"}))

#category 3 Motors
@app.route('/motors')
def motors():
    return render_template('motors.html', 
    motors=mongo.db.products.find({'category_name':"Motors"}))
 
#FUNCTION TO VIEW PRODUCT BY ITS ID AND RETRIEVE it in product.html            
@app.route('/product/product_id?=<id>', methods=['GET', 'POST'])
def product(id):
    view_product=mongo.db.products.find_one({"_id": ObjectId(id)})
    return render_template('product.html', view_product=view_product)
    
#REVIEW FUNCTION
'''
currently working in this function.
- the main issue is that I need to post reviews on the currently product/post 
and unfortunately I am having issues.
- The product.html template is having matching problems with the product() function

The approach I am having is that, trying to add a new review and update the 
collection with the new update

=== issues:
- updating with all other table field declaring with mongo.db.find
will update it as null but with the right review.

- updating only with the review field will delete the table only displaying the 
review in the place of the product post.

=== SOLUTION:

I should find a way to get the table not using the mongo.db.products... to not
return null or 2nd insert the review with name/post/date straight into the table
'''
@app.route('/review/product_id?=<id>', methods=['POST', 'GET'])
def review(id):
    now = datetime.datetime.now()
    name=session['name']
    post=request.form.get('review')
    reviews = mongo.db.products.find({'_id':ObjectId(id)})
    if request.method == 'POST':
        reviews.mongo.db.products.update([{
                    'review':{'_id':ObjectId(),
                    'name': name,
                    'post': post,
                    'date': now.strftime("%d-%m-%Y")}
                }]
            )
    return render_template('product.html', reviews=reviews, name=name, date=now, post=post)
    
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