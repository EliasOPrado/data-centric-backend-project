# Data Centric Backend Project

## To-do

- Install packages
  - Still problems...
- Proper connect templates (done)...
- Create the database and tables (done) 
- Connect the links within each template (done)
- Improve the design of the register and login pages
  - [See this example](http://azmind.com/wp-content/uploads/2015/06/Hype-Enterprise-Login.png)
  - [and this too](https://file.mockplus.com/image/2019/05/886d7ebd-61e1-4227-9348-c8bac23c364b.png)
- Footer needs to be fixed on mobile.
- CRUD
  - Create:(done);
  - Read (done);
  - Update (done);
  - Delete(done);

### For the database:

- Implement USER page with UPDATE, DELETE and PRODUCTS done by the user;<<<<<--------
- Find the way to place and retrive data in the templates;(done)
- Implement Login and ```@login_required``` on its user page; (done)
  - Use password _encription_ login;(done)
- Encript the MongoDB connection;()
- USE THE TASK PROJECT TO RECYCLE THE DELETE FUNCTION...;(done)
  - You may use ```@login_required```to entry in categories pages and be able to >>edit and delete<< products.(not needed)
  - May not need to add requirements for now, just add it and require login after.(done) Week 2
  - TO DELETE YOU WILL NEED TO CONNECT FIRST USER AND RETRIEVE EACH PRODUCT BASED ON THE LOGGED USER.(done)
  - # check for logged in user
- ADD COMMENTS ON PRODUCTS BY USERS [done]

- Add trend:
``` 
{% if reviews.views >= 10 %}
              <div class="col">
                </small><i class="fas fa-chart-line text-muted"></i>
              </div>
              {%endif%}
              
```

- Add search function:

```  @app.route('/search')  
 def search():
     """Route for full text search bar"""
     db_query = request.args['db_query']
     results = mongo.db.recipe.find({'$text': {'$search': db_query}})
     return render_template('search.html',
                               results=results,
                               title="Search Results")```