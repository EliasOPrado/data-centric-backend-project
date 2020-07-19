
# Testing

- [Main README file](ReadMe.md)
- [Live website](http://data-structure-project.herokuapp.com/)

## Table of contents

1. [Manual testing](#Manual-testing)
    1. [Home page](#Home-page)
    2. [Page detail](#Page-detail)
    3. [Categories](#Categories)
    4. [Register](#Register)
    5. [Login page](#Login-page)
    6. [Accounts page](#Accounts-page)
    7. [Edit product](#Edit-product)
    8. [See product](#)
2. [Web testing](#Web-testing)
    1. [Mobile](#Mobile)
    2. [Tablets](#Tablets)
    3. [Laptops](#Laptops)
3. [Validation services](#Validation-services)
4. [Bugs found and solved](#Bugs-found-and-solved)
5. [Unsolved bugs](#Unsolved-bugs)


## Manual testing

### Home page

1. On navbar click on links to check if they are sending to the corespondent page.
2. Click on different categories to check if they are sending to the correspondent page.
3. Click on one of the three header from the carousel and check they are sending the user to the corresponding page.
4. Click on different cards to check if they are sending to the review or product detail page.
5. Click on the social icons to check if they are sending to the correspondent website.

### Page detail

1. On home page click on one product card and go to the page view.
2. After register and login check if it is possible to add a comment.
3. If the comment is created, check if it is possible to delete this comment.
4. When not logged in check if the comment form is disabled.
5. Check if the view is adding one per view you did.

### Categories

1. On the navbar or side card called categories click on a category as `Electronics`, `Home & Garden` or `Motors`.
2. On the category page, check if the products are based within the correspondent category. Like, electronics into Electronics category.
3. Click on a product to see whether the user is sent to the correspondent product view or not receive a error message.
4. Check if the pagination is working, like, if on the last page it should stop the pagination button, not loading empty page.

### Register

1. On navbar click on the register link.
2. On the register page add your username, email and password.
3. Click the sign up button and check if the user is redirected to the login page.

### Login page

1. On navbar click on the login link.
2. On the login page add your email address and your password.
3. If the login is done, the user will be redirected to his account page.

### Accounts page

1. On the account page select the category on the form.
2. Add a product name.
3. Add a price.
4. Add url link.
5. Add description and click submit.
6. If the form is submitted a message will be displayed telling the user the product was listed successful and redirected to the same page.
7. The product will be displayed at the account page after the page is redirected.

### Edit product

1. After listing a product click on the `edit` (green) button.
2. The user will be redirected to a page to change the category, product name, price, image url and description.
4. After the changes is submitted the user will be redirected to its account page with the product edited.

### See product

1. After listing a product click on the `see` (blue) button.
2. The user will be redirected to the product detail, being able to visualize their product.


## Web testing

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
- Macbook Pro

## Validation services

- [W3C Markup validation](https://validator.w3.org/)
- [W3C CSS validation](https://jigsaw.w3.org/css-validator/)
- [JS Hint](https://jshint.com/)

## Bugs found and solved

There had some issues with function authentication and users without being logged having access to sensitive functions
such as ```edit_product```. I had to learn it and add session based access only logged users to have access based on their own
posts. Therefore, to make sure it was working well I added the function on the url and added a product id without being logged
to check whether I had access and finally they were fixed.


## Unsolved bugs

There still a small issue with the ```edit_product``` function
in which only logged users if trying to edit other user's product can be redirected to the edit_product form page but with no access to details, not damaging any user data.

Example of function authentication:

```
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
