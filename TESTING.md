
# Testing

The devices that the application was tested were:

### Mobile

- BlackBerry Z30
- Galaxy Note 3
- Moto G4
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 4
- iPhone 5 SE
- iPhone 6, 7 and 8
- iPhone 6, 7 and 8 Plus
- iPhone X

### Tablets

- iPad 
- iPad Mini
- iPad Pro

### Laptops

- ThinkPad X1 Carbon
- ThinkPad T430


## Function Testing And Unsolved Bugs

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
