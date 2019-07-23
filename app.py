
#Imports
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

#App configuration
app.config['MONG_DBNAME'] = 'task_manager'
app.config['MONGO_URI'] = 'mongodb+srv://'
                            

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    return 'hello world'
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)