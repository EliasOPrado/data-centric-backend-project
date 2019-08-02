
#Imports
import os
from flask import Flask, render_template, redirect, request, url_for
#from flask_pymongo import PyMongo
#from bson.objectid import ObjectId 

app = Flask(__name__)

#App configuration
#app.config['MONG_DBNAME'] = 'task_manager'
#app.config['MONGO_URI'] = 'mongodb+srv://'
                            

#mongo = PyMongo(app)

#you need to set the home under this route.
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
    
#need to change the name of the categories
#based on its name.
@app.route('/category1')
def category1():
    return render_template('category1.html')

#need to change the name of the categories
#based on its name.  
@app.route('/category2')
def category2():
    return render_template('category2.html')

#need to change the name of the categories
#based on its name.
@app.route('/category3')
def category3():
    return render_template('category3.html')
    
@app.route('/login')
def login():
    return render_template('login.html')

#add methods as needed    
@app.route('/register')
def register():
    return render_template('register.html')
    

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)