
# AdPro

<img src="/static/images/mockup.png">

Project Milestone Three - Code Institute

AdPro is a website that emulates the functionality of a C2C (Consumer to Consumer) e-commerce platform. With educational purpose only as part of Code Institute Software Development diploma. The main goal of this project is to show the ```CRUD``` functionalities using ```MongoDB``` as a Non relational database. Bringing to the user the ability to create new posts such as product lists, view, read, update from its profile and delete their own postages.


## Table of contents
<!--ts-->

1. [UX](#UX)
    1. [User goals](#User-goals)
    2. [Design choices](#Design-choices)
       1. [Fonts](#Fonts)
       2. [Colors](#Colors)
       3. [Styling](#Styling)
       4. [Wireframes](#Wireframes)
2. [Features](#Features)
    1. [Navbar](#Navbar)
    1. [Footer](#Footer)
    1. [Register](#Register)
    2. [Login](#Login)
    1. [Home Page](#Home-Page)
    2. [Categories](#Categories)
    3. [The Product View](#The-product-view)
    4. [The User Account Page](#The-User-Account-Page)
    5. [404 page](#404-page)
    6. [Features left to implement](#Features-left-to-implement)
3. [Database Structure](#Database-Structure)
4. [Technologies](#Technologies)
    1. [Tolls](#Tolls)
    2. [Libraries](#Libraries)
    3. [Programming languages](#Programming-languages)
    4. [Coding challenges during development](#Coding-Challenges-During-Development)
5. [Testing](#Testing)
   - You can see the [TESTING.md](TESTING.md) file here.
6. [How to run this application locally](#How-to-run-this-application-locally)  
7. [Deployment](#Deployment)
8. [Credits](#Credits)
   1. [Content](#Content)
   2. [Acknowledgments](#Acknowledgments)
 <!--te-->

# UX:

## User goals
The target audience of AdPro are:
   - People who want to add products for sale.
   - People who want to check different prices based on views.
   - Users who want to check what other users are talking about different products.

User goals:
   - Check what are the products available for sale in different categories.
   - Search a specific category and search a product within this category.
   - Create an account.
   - Login in their account.
   - Add, edit and delete products.
   - See their products in a page with comment box.
   - See their products in a table.
   - Add comments in different ads.
   - Delete their own comments already added.
   - See how many views a products has.

## Design choices

### Fonts
  - The font used in this project is [Roboto](https://fonts.google.com/specimen/Roboto#about) which is an user friendly mainly used by its creator Google to give a proper reading in different screen sizes.

### Colors
   - Baltic Sea: ![#343a40](https://via.placeholder.com/15/343a40/000000?text=+) `#343a40`
   - Matterhorn: ![#545454](https://via.placeholder.com/15/545454/000000?text=+) `545454`
   - White smole: ![#f2f2f2](https://via.placeholder.com/15/f2f2f2/000000?text=+) `#f2f2f2`
   - Tropical rain forest: ![#097460](https://via.placeholder.com/15/097460/000000?text=+) `#097460`
   - Dark lime green: ![#28a745](https://via.placeholder.com/15/28a745/000000?text=+) `#28a745`
   - Pelorous: ![#17a2b8](https://via.placeholder.com/15/17a2b8/000000?text=+) `#17a2b8`
   - Dodger blue: ![#007bff](https://via.placeholder.com/15/007bff/000000?text=+) `#007bff`
   - Amber: ![#fec008](https://via.placeholder.com/15/fec008/000000?text=+) `#fec008`


### Styling
   - Bootstrap cards to group the products.
   - Box shadow to give a depth idea in contrast with the background.
   - The usage of different colours for each category to contrast each other and give direction to users.

## Wireframes

The wireframes for this project were only take three devices in accountability as Mobile phones, iPad and normal screen. In addition, the tool used to develop them was [Balsamiq](https://balsamiq.com/) for a rapid design.

   - [Mobile devices](/static/mockups/mobile-mockups.png)
   - [iPad devices](/static/mockups/ipad-mockups.png)
   - [Desktop devices](/static/mockups/desktop-mockups.png)


# Features

AdPro is made with different features and pages, `Home page`, `Categories`, `Product view`, `User account`, `Register page` and `Login page`. Therefore, the template of this project was developed to bring simplicity to the user avoiding unexpected experiences, adding intuitive navigation.

## Navbar

<p align="center">
<img src="/static/images/not-logged-navbar.png" width="40%">
</p>

- When a user is not logged the navbar will display the login and register links for the user to choose what he needs.

<p align="center">
<img src="/static/images/logged-navbar.png" width="40%">
</p>

- Once the user is logged in the login and register button will desappear giving the space for account and logout instead.

## Footer

<p align="center">
<img src="/static/images/not-logged-footer.png" width="40%">
</p>

- The only difference on the footer is when user is logged in or logged out.

<p align="center">
<img src="/static/images/logged-footer.png" width="40%">
</p>

- If the user is not logged a button will be displayed for he or she to register a new account.

## Register

<p align="center">
<img src="/static/images/register.png" width="40%">
</p>


- The register page is set to add new users with their name, email address and password. Once the user is registered it will be redirected to the login page.

## Login

<p align="center">
<img src="/static/images/login.png" width="40%">
</p>

   - The login page is displayed for registered users to add its email and password to have access to its account, add and delete comments in the product detail page. Once the user is logged in they will be redirected to its account page.

## Home Page

<p align="center">
<img src="/static/images/homepage.png" width="40%">
</p>

   - The home page has everything the user need.
   - A simple and well designed carousel with its three categories and an image representing each category as headers.
   - Links with the name of each category to facilitate users to navigate the app.

## Categories

<p align="center">
<img src="/static/images/categories.png" width="40%">
</p>

   - Under the categories, a pagination scheme is settled to only show six products per page to not overwhelm the user and of course give a good experience.

## The product view

<p align="center">
<img src="/static/images/product_detail.png" width="40%">
</p>

Users after clicking on a product card, rather it is on the home page or in categories will be sent to a view page in which will be able to see the product in a larger image and its description as well as post a comment for the seller of the product such as bid or asking the price.

## The User Account Page

<p align="center">
<img src="/static/images/accounts.png" width="40%">
</p>

   - The user account page is basically two pages in one where users will be able to add a new product using a form (right page) and see them after submitted on a table with privilege of delete, view and edit (left page).
   - So, to add a new product, select the category, add the product name, chose a price, add the image url and description.
   - When the product is post, it will be displayed at the category choosed, such  as `electronics`, `home & garden` or `motors` as well as on the list in account.
   - Three buttons will be displayed at the account page to edit, view the product detail or delete.

## 404 page

<p align="center">
<img src="/static/images/404.png" width="40%">
</p>

   - A 404 page is set to be displayed for when an error occur when a page is not found. Making the user be able to return to the main page with its button.


## Features left to implement

   1. Since Users are not able to edit comments after post it on the product view page, only delete. there’s room to add edit comment.
   2. In the user account page, the select form should be fixed to have the method “required”.



# Database Structure

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

# Technologies

## Tools

   - [Atom](https://atom.io/) as an IDE to develop this project.
   - [MongoDB Atlas](https://www.mongodb.com/) as the database used in this project.
   - [Canva](https://www.canva.com/) for the design of the images.
   - [Pip](https://pip.pypa.io/en/stable/installing/) a package management system used to install the needed packages for this application.
   - [Github](https://github.com/) to share and store code remotely.
   - [Git](https://git-scm.com/) was used to manage version control.
   - [Chrome Devtools](https://developers.google.com/web/tools/chrome-devtools) that was used to easy the design and responsiveness of this project.

## Libraries

   - [Flask](https://palletsprojects.com/p/flask/) a python library to make web developmet easy to process.
   - [Jinja2](https://palletsprojects.com/p/jinja/) a template engine for python used to run programming login within html.
   - [Bootstrap](https://getbootstrap.com/) used to build and structure the design of the web pages as a css library.
   - [Google fonts](https://fonts.google.com/) to get and display customised fonts.
   - [Github](https://github.com/) to share and store code remotely.
   - [Git](https://git-scm.com/) was used to manage version control.
   - [Chrome Devtools](https://developers.google.com/web/tools/chrome-devtools) that was used to easy the design and responsiveness of this project.

## Programming languages

The programming languages used in this project was, Python, Javascript, CSS and HTML.

## Coding challenges during development

There are some challenges that were faced during the development of this project such as add user comments on a third user product and pagination.

   1. The difficult was that it was required to develop a function in which would embed comments as arrays into the database.

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
   2. In addition another function that was very hard to develop was the pagination system.
  The algorithms of the function was an set of arithmetics in both ```python``` and ```jinja``` with a mix of url management. Initially it worked but the pagination wasn't showing the real value of pages, based on the number required per page. Having one or two empty pages in advance.

# How to run this application locally

Before you run this application locally you will need to create an account in [MongoDB](https://www.mongodb.com/) and create a database. PS: You don't need to design the tables again, since they already designed in this project.

1. From the following link https://github.com/EliasOPrado/data-centric-backend-project direct download this project or git clone into your directory.
2. With the project already open in your IDE create a `virtual environment` with the following commands:
   1. Create the virtual environment: `$ python3 -m venv venv` in root.
   2. Activate the virtual environment: `$ source venv/bin/activate`
   3. After activated your directory will be displayed like this: `(venv) <your/directory/path> $`
3. Create a file to hold the project configuration locally: `$ touch venv.py`
4. Into the `venv.py` folder add the following configs:
   ```
   import os

   os.environ.setdefault('SECRET_KEY', '<your secret key>')
   os.environ.setdefault('ENV_MONGO_DBNAME', '<your db name>')
   os.environ.setdefault('ENV_MONGO_URI', 'mongodb+srv://<username>:<password>@cluster0-0oagu.gcp.mongodb.net/<your mongodb name>?retryWrites=true')
   os.environ.setdefault('IP', '0.0.0.0')
   os.environ.setdefault('PORT', '5000')
   ```
5. Create a `.gitignore` file and add `venv.py` and `venv/` directory in it.
6. After the setup to run the local server do the following command: `$ python app.py run`


## Deployment

To deploy to Heroku there are some steps to e followed:

1. Using the terminal install the ```requirements.txt``` packages with the command ```$ pip install -r requirements.txt```.
2. Add a Procfile with the following content ```web: python app.py```.
3. Commit the new files such as requirements.txt and Procfile.
4. In the Heroku website make a new app tapping on the ```new``` button.
5. Choose the application that was already created.
6. Check if the Heroku application is proper linked to the right repository in Github.
7. Chose the application you want to deploy and click on ```config vars```.
   - Set the `IP: 0.0.0.0`
   - Set the `PORT: 5000`
   - Set your `SECRET_KEY: <secret key>`
   - Set the `MONGO_DBNAME: <your mongodb name>`
   - Set the `MONGO_URI: mongodb+srv://<username>:<password>@cluster0-0oagu.gcp.mongodb.net/<your mongodb name>?retryWrites=true`

8. On the ```app.py``` set the config as follow to match the deployment vars:
  ```
  if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
  ```
9. Also the connection of the application with the data base should be displayed:
  ```
  app.secret_key = os.getenv("SECRET_KEY")
  app.config['MONGO_DBNAME'] = os.getenv("ENV_MONGO_DBNAME")
  app.config['MONGO_URI'] = os.getenv("ENV_MONGO_URI")
  ```
10. Install the [Heroku-CLI](https://devcenter.heroku.com/articles/heroku-cli).
11. Bash commands to deploy:
  ```
  $ heroku login
  $ git add .
  $ git commit -am "make it better"
  $ git push heroku master
  ```
# Credits

## Content
  - The content for this project such as images are directly from the internet with the usage of urls.

## Acknowledgments
- [Start Bootstrap](https://startbootstrap.com/templates/ecommerce/) and its creator `David Miller` for the project template.
- [Sipo](https://github.com/sipostudent) for the help in some hard parts of the code.
- My mentor ```Antonio``` who gave me great help through the project development.
