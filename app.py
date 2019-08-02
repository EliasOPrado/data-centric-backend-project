
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
    

@app.route('/category1')
def shop_item():
    return render_template('category1.html')
    
@app.route('/category2')
def shop_item():
    return render_template('category2.html')

@app.route('/category3')
def shop_item():
    return render_template('category3.html')
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)