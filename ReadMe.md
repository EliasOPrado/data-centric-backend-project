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

##Goal 

The main goal of this project is to shows off the ```CRUD``` functionalities using ```MongoDB``` as a Non relational database. 
Bringing to the user the ability to create new posts such as product lists, view and read their postages, update from its profile as well as delete their own postages.

###Functionality

The project is basically designed with Python and the Flask framework in which is used to integrate different templates and its main functionalities. 
Therefore, the application is separeted by eight different sections ```Index, Electronics, Home & Garden, Motors,review, Register, Login and Edit```. In which are used ```jinja```
a web template engine allowing to create functions, loops and conditionals based on the goal of the project. 


####Index

The main page of the project is the place in which all the project categories are displayed with the intent to give an overall view of the project. For instance, there you can see
all three categories with three of its products listed. 

####Categories

The project is separeted into three categories, ```Electronics, Home & Garden and Motors```. Therefore, althought they are different, their functionalities are same, since the
main functionality is to display list products and pagination.

####Create new products 

To create new products the user will need to register and login to have the privilege to add new lists. The function that pushes the new list into the database is the
```insert_product``` that will take the form from the user template and insert into the database. 




##