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

The main goal of this project is to show the ```CRUD``` functionalities using ```MongoDB``` as a Non relational database. 
Bringing to the user the ability to create new posts such as product lists, view, read, update from its profile and delete their own postages.
The project is basically designed with Python and the Flask framework in which is used to integrate different templates and its main functionalities. 
Therefore, the application is separeted by eight different sections ```Index, Electronics, Home & Garden, Motors,review, Register, Login and Edit```. In which are used ```jinja```
a web template engine allowing to create functions, loops and conditionals based on the goal of the project. 

## Functionality

The functionality of this project is made aiming users to shares its data with other users with distinct privileges non-registered and registered users.
For instance, users without register will not be able to add new products or leave a comment in another user's ad. 
The main functionality of this project are the functions login, register, logout, update_proudct and edit_product and delete_product.
Each of them has many other function to display, delete, retrieve, update or insert a new product into the data base.

## UX:

The template of this project was developed to bring simplicity to the user avoiding unexpected experiences, adding intuitive navigation. 

##### Home page:
For instance, the home page has everything the user need. A simple and well designed carousel with its three categories and an image representing each category. Links with the name of each category to facilitate users to navigate the app.

##### Categories

Under the categories, a pagination scheme is settled to only show six products per page to not overwhelm the user and of course give a good experience. 

##### The product view 
 
Users after clicking on a product card, rather it is on the home page or in categories will be sent to a view page in which will be able to see the product in a larger image and its description as well as post a comment for the seller of the product such as bid or asking the price. 

##### The user account page

The user account page is basically two pages in one where users will be able to add a new product using a form (right page) and see them after submitted on a table with privilege of delete, view and edit (left page).

#### Font 

The font used in this application is the Roboto sans-serify. A geometric font that allows a natural reading.

#### Mobile display

<img src="/static/images/mobile.png" width="200"> 

#### Tablet display

<img src="/static/images/ipad.png" width="200"> 

## Database structure 

``` 
 category{

   _id:<id>
   category_name:"Electronics"
   
   _id:<id>
   category_name:"Home & Garden"
   
   _id:<id>
   category_name:"Motors"

}

products{

   _id:<id>
   category_name:"Electronics"
   product_name:""
   price:"500"
   url:"https://www.londondrugs.com/on/demandware.static/-/Sites-londondrugs-m..."
   seller:" "
   product_description:" "
   views:15
   review:Array
      0:Object
        name:"Lucas"
        post:"add a comment here...."
        date:"17/09/2019"
      1:Object
        name:"eliasprado"
        post:"roses are red and the sky is blue I am just commenting here to appear in the readme file :D"
        date:"14/10/2019"

}

user{

   _id:<id>
   name:"<user name>"
   email:"<user email>"
   password:"<user password>"

}
```

## Technologies 

- HTML
- CSS
- Bootstrap 
- Python
- Flask
- Jinja 2
- Google fonts 
- Font awesome

## Coding challenges during development 

There are some challenges that were faced during the development of this project such as add user comments on a third user product. 
The difficult was that it was required to develop a function in which would embed comments as arrays into the database. 

Embedded DB comment: 
```
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
```
In addition another function that was very hard to develop was the pagination system. 
The algorithms of the function was an set of arithmetics in both ```python``` and ```jinja``` with a 
mix of url management. Innitially it worked but the pagination wasn't showing the real value of pages
based on the number required per page. Having one or two empty pages in advance. This issue was only solved 
with my mentor help.

Authorization and function issues on the url….

## Features

- Register and have its own page.
- Login.
- Add new product from user page based on its login.
- See product list on user page.
- Be able to visualize, edit and delete its own product.
- Navegate product pages. 
- View product on its own page.
- Be able to add comments on product as well as delete it.

## Features left to implement

Since Users are not able to edit comments after post it on the product view page, only delete. there’s room to add edit comment.
The media query for iPad Pro should be improved on the categories page.
In the user account page, the select form should be fixed to have the method “required”.

## Testing

The devices that the application was tested were:

### Mobile:

- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5 SE
- iPhone 6, 7 and 8
- iPhone 6, 7 and 8 Plus
- iPhone X

### Tablets:

- iPad
- iPad Pro

### Laptops:

- ThinkPad X1 Carbon
- ThinkPad T430


## Function testing and unsolved bugs

There had some issues with function authentication and users without being logged having access to sensitive functions
such as ```edit_product```. I had to learn it and add session based access only loged users to have access based on their own 
posts. Therefore, to make sure it was working well I added the function on the url and added a product id without being logged 
to check whether I had access and finally they were fixed. 

### Unsolved bugs

There still a small issue with the ```edit_product``` function 
in which only loged users if tryng to edit other user's prouduct can be redirected to the edit_product form page but with no access to details, not damagin any user data.

Example of function authentication:

``` diff
@app.route('/edit_product/<product_id>')
def edit_product(product_id):
+   seller = session['name']
+   if not seller:
        return redirect(url_for('register'))
    try:
        the_product = mongo.db.products.find_one({"_id": ObjectId(product_id), 'seller':seller})
        all_categories = mongo.db.category.find()
    except:
        return redirect(url_for('index'))
    return render_template('editproduct.html', product=the_product, categories=all_categories)
```

## Deployment

To deploy to Heroku there are some steps to e followed:

1. Using the terminal install the ```requirements.txt``` with the command $ ```pip freeze > requirements.txt ```.
2. Add a Procfile with the follow content ```web: python app.py```.
3. Commit the new files such as requirements.txt and Procfile.
4. In the Heroku website make a new app tappin on the ```new``` button.
5. Choose the application that was already created.
6. Check if the heroku application is proper linked to the right repository in github.
7. Chosed the application you want to deploy and click on ```config vars```.
   - Set the ```IP```: 0.0.0.0
   - Set the ```PORT```: 5000
8. On the ```app.py``` set the config as follow to match the deployment vars:
  ```
  if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
  ```
9. Also the connection of the application with the data base should be displayed:
  ```
  app.secret_key = 'any random string'
  app.config['MONG_DBNAME'] = '<db name>'
  app.config['MONGO_URI'] = 'mongodb+srv://<username>:<password>@cluster0-0oagu.gcp.mongodb.net/recipebook?retryWrites=true'
  ```
10. Install the heroku CLI.
11. Bash commands to deploy:
  ```
  $ heroku login
  $ git add .
  $ git commit -am "make it better"
  $ git push heroku master
  ```
## Credits 

- [Start Bootstrap](https://startbootstrap.com/templates/ecommerce/) for the project template.
- [Sipo](https://github.com/sipostudent) for the help in some hard parts of the code.
- My mentor ```Antonio``` who gave me great help through the project development.