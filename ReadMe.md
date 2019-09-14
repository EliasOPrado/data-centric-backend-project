# Data Centric Backend Project

## To-do



- Add search function:

```  @app.route('/search')  
 def search():
     """Route for full text search bar"""
     db_query = request.args['db_query']
     results = mongo.db.recipe.find({'$text': {'$search': db_query}})
     return render_template('search.html',
                               results=results,
                               title="Search Results")
```

- Check the session['name'] in the code. It is bringing problem with the product.html template.

- PROBLEMS:
  - Having two extra pages in pagination.
  - Make aside product cards loop based on its view DESCENDING. (in all categories and Index[for all categories])
  - Redirect to its own page (product.html) after sending a comment.
  - Delete comment function in the product.html.
  - Deployment Issue..
