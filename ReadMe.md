## Table of contents
<!--ts-->

1. [About](#about)
   1. [Goal](#Goal)
   2. [Functionality](#Functionality)
   3. [Settings](#Settings)
   4. [Four playable buttons](#Four-playable-buttons)
   5. [Initiation](#Initiation)
2. [UX](#UX)
   1. [Layout](#Layout)
   2. [Mobile Display](#Mobile-Display)
   3. [Tablet Display](#Tablet-Display)
   4. [Additional Note](#Additional-Note)
   5. [Color scheme](#Color-scheme)
   6. [Audio Content](#Audio-Content)
3. [Technologies](#Technologies)
4. [Testing](#Testing)
   1. [How the website was tested?](#How-the-website-was-tested)
   2. [Unfixed bugs](#Unfixed-bugs)
5. [Deployment](#Deployment)
   1. [Steps I used to deploy](#Steps-I-used-to-deploy)
6. [Credits](#Credits)
 <!--te-->

## About 

Project Milestone Three - Code Institute

AdPro is a website that emulates the functionality of a C2C (Consumer to Consumer) ecommerce platform. 

## Goal 

The main goal of this project is to shows off the ```CRUD``` functionalities using ```MongoDB``` as a Non relational database. 
Bringing to the user the ability to create new posts such as product lists, view and read their postages, update from its profile as well as delete their own postages.
 
### Functionality

The project is basically designed with Python and the Flask framework in which is used to integrate different templates and its main functionalities. 
Therefore, the application is separeted by eight different sections ```Index, Electronics, Home & Garden, Motors,review, Register, Login and Edit```. In which are used ```jinja```
a web template engine allowing to create functions, loops and conditionals based on the goal of the project. 


#### Index

The main page of the project is the place in which all the project categories are displayed with the intent to give an overall view of the project. For instance, there you can see
all three categories with three of its products listed. 

#### Categories

The project is separeted into three categories, ```Electronics, Home & Garden and Motors```. Therefore, althought they are different, their functionalities are same, since the
main functionality is to display list products and pagination.

#### Create new products 

To create new products the user will need to register and login to have the privilege to add new lists. The function that pushes the new list into the database is the
```insert_product``` that will take the form from the user template and insert into the database. 

```
#CREATE FUNCTION
@app.route('/insert_product', methods=['POST'])
def insert_product():
    products=mongo.db.products
    if request.method == 'POST':
        form_dict = request.form.to_dict()
        form_dict.update({'seller': session['name']})
        products.insert_one(form_dict)
    return redirect(url_for('user'))
```

#### Read posts

There are different aproaches to read and view different postages in this projects. For instance, using ```jinja``` there is the possibility to display multiples posts/prouducts
with a ```for``` loop within each template. 

App.py
```
#category 1 Eletronics
@app.route('/electronics/')
@app.route('/electronics/<page>/<limit>')
def electronics(page=1, limit=6):
    page=int(page)
    limit=int(limit)
    skip = page * limit - limit
    maximum = math.floor( (mongo.db.products.count_documents({})) / limit - 1)
    print(maximum)
    electronics = list(mongo.db.products.find({'category_name':"Electronics"}).sort("$natural", pymongo.DESCENDING).skip(skip).limit( limit ))
    return render_template(
        'electronics.html', 
        electronics=electronics,
        page=page,
        pages=range(1, int(maximum) + 1),
        maximum=maximum, 
        limit=limit
    )
```
electronics.html
```
 <!--ELETRONICS-->
      {% for electronic in electronics %}
      <div class="col-lg-4 col-md-6  my-2 card-position">
        <div class="card h-100 shadow-sm">
          <a href="{{ url_for('review', id=electronic._id)}}"><img class="card-img-top" src="{{ electronic.url }}" width="200" height="200" alt="" class="responsive-img"></a>
          <div class="card-body">
            <h4 class="card-title">
              <a href="{{ url_for('review', id=electronic._id) }}"><small>{{ electronic.product_name }}</small></a>
            </h4>
            <div class="row">
              <div class="col">
                <h5>${{ electronic.price }}</h5>
              </div>
              <div class="col">
                <i class="fas fa-eye text-muted"> {{electronic.views}}</i>
              </div>
            </div>
          </div>
        </div>
      </div>
      {% endfor %}
```
Following the example above, the ```for``` loop will display all the products from the database with its specification such as ```{'category_name':"Electronics"}``` from MongoDb.

Moreover, the ```product.html``` template will allow users to view their posts as well as have the ability to receive comments from other registered users. The function that handles the 
product.html templats is the ```review``` in which will be more detailed in the challenges section..

#### Update posts

The ability to update or edit a post is aimed for registered users. Once a user post a new product, they will be able to view, update and delete its products, each function with its own button.
For instance, to update a product, the user will need to click the button to edit and automatically be changed to a new page called ```editproduct.html``` where all the deail of the 
product will be retrieved in a form. Where the owner of the product will be able to edit. 

##### How does it works?

First and foremost, when users inserts a new product into the database, its list will be tied with their own name based on ```session['name']``` making so the product being displayued