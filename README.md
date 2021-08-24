# **Shakes on the Beach**

Live Link - [https://shakes-on-the-beach.herokuapp.com/](https://shakes-on-the-beach.herokuapp.com/)

![responsiveness-image](static/responsiveness.png "image_tooltip")

---

## **Table of Contents**

---

- [Overview](#overview)
- [UX](#ux)
  - [Stories](#stories)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
- [Wireframes](#wireframes)
- [Features](#features)
- [Testing](#testing)
  - [Manual](#manual)
  - [Automated](#automated)
  - [Bugs](#bugs)
- [Technologies Used](#technologies-used)
- [Resources](#resources)
- [Project barriers and the solutions](#project-barriers-and-the-solutions)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)
- [Support](#support)

---

## **Overview**

---

Shakes on the beach is a sea side cafe offering an assortment of food and drinks.

This web application is designed to allow the user to browse the available products and build a basket. The user can then then make a card payment and the order will be proccessed.

---

## **UX**

---

### **Stories**

#### **User Stories**

As a user, I would like to...

- Browse a menu of the available products the cafe offers.
- Select the items I wish to order and add them to a basket.
- Adjust the basket by increaseing or decreasing the amount of an item, or remove the item entirely.
- Enter my delivery and credit card information so I can submit my order to be delievered to my chosen address.
- Recieve a confirmation of my order with the order,billing and delivery details.
- Have option of creating a user profile to store my information to process my future orders more easily.

#### **Developer Stories**

""

""

""

### **Strategy**

#### **Project Goals:**

- 
- 
- 
- 

#### **User Goals:**

- 
- 
- 
- 

---

[Return to Table of Contents](#table-of-contents)

---

### **Scope**

#### **Planned Functionality:**

Navbar:

- Clicking on title or title icon, will navigate the user back to the homepage.
- Account
  - Register - Navigate the user to the sign up page to create a user profile
  - Login - Navigate the user to the login page so the user can login to their user profile
- The basket icon or the total cost of products present in the basket, will navigate the user to the basket page

Menu Page:

- Menu Navbar
  - Clicking the "MENU" anchor will refresh the menu page showing all products available
  - Nav Items
    - Burgers - will show all burgers available on the store
    - Pizza - will show all pizzas available on the store
    - Sandwhich - will show all sandwhiches available on the store
    - Salad - will show all salads available on the store
    - Shakes - will show all shakes available on the store
    - Drinks - will show all drinks available on the store
- Each product will have its own container, where the image can be clicked to bring the user to the product details page of the clicked product

Menu Product Details Page:

- Clicking on the product image will open the image in a new tab for better visibility
- A quantity form for a user to alter the value of the quantity to be added to the basket
  - The "+" will increase the value of the quantity by one
  - The "-" will decrease the value of the quantity by one
  - The user click on the field manually and type the number they wish to add to the basket
- < Keep Shopping - will return the user to the menu page
- Add to Basket - will take product on the page, and the quantity in the selector, and add that ammount of the product into the basket

Basket Page:

- A quantity form for a user to alter the value of the quantity currently in the basket
  - The "+" will increase the value of the quantity by one
  - The "-" will decrease the value of the quantity by one
  - The user click on the field manually and type the number for the the quantity they want in the basket
- Update - the basket will be updated with the quantity that is shown in the selector
- Remove - the item in which the "Remove" anchor is associated with will be removed from the basket
- < Keep Shopping - will return the user to the menu page
- Secure Checkout - will navigate the user to the checkout page with the basket on the current page

Checkout Page:

- Input fields
  - Full Name - User must enter their name
  - E-mail - User must enter their e-mail
  - Phone Number - User must enter their phone number
  - Street Address 1 - User must enter the first line of their address
  - Street Address 2 - User can enter the second line of their address 
  - Town or City - User must enter their town or city
  - Postal Code - User can enter their postal code
  - County, State or Locality - User can enter their county, state or locality
- Create an Account - will navigate the user to the sign up page
- Login - will navigate the user to the login page
- Payment input field - the user must enter their credit card information to proceed with the order
- < Adjust Basket - will return the user to the basket page
- Complete Order - will attempt to process the users order, if successful will navigate the user to the checkout success page

Checkout Success Page:

- This page will display all the information relevant to the order
  - Order Info
    - Order Number
    - Order Date
  - Order Details
    - A list of the products that were in the basket of the order
  - Deliveriy Details
    - The Full Name, Address, County, Town or City, Post Code and Phone Number
  - Billing Information
    - Order Total
    - Delivery Charges
    - Grand Total

Sign Up Page:

- 
- 
- 
- 

Login Page:

- 
- 
- 
- 

Profile Page:

- 
- 
- 
- 

Password Reset Page:

- 
- 
- 
- 

Verification Pages:

- Verification Sent - This page informs you to to check your inbox as the link needed to finalize the profile setup proccess.
- Verification Sent - This page informs you to to check your inbox as the link needed to finalize the profile setup proccess.
- 
- Verification Sent - This page informs you to to check your inbox as the link needed to finalize the profile setup proccess.

Toasts:

- 
- 
- 
- 

Error Pages:

- 
- 
- 
- 

---

[Return to Table of Contents](#table-of-contents)

---

### **Structure**

#### **Interaction Design:**

Navbar:

- Clicking on title or title icon, will navigate the user back to the homepage.
- Account
  - Register - Navigate the user to the sign up page to create a user profile
  - Login - Navigate the user to the login page so the user can login to their user profile
- The basket icon or the total cost of products present in the basket, will navigate the user to the basket page

Menu Page:

- Menu Navbar
  - Clicking the "MENU" anchor will refresh the menu page showing all products available
  - Nav Items
    - Burgers - will show all burgers available on the store
    - Pizza - will show all pizzas available on the store
    - Sandwhich - will show all sandwhiches available on the store
    - Salad - will show all salads available on the store
    - Shakes - will show all shakes available on the store
    - Drinks - will show all drinks available on the store
- Each product will have its own container, where the image can be clicked to bring the user to the product details page of the clicked product

Menu Product Details Page:

- Clicking on the product image will open the image in a new tab for better visibility
- A quantity form for a user to alter the value of the quantity to be added to the basket
  - The "+" will increase the value of the quantity by one
  - The "-" will decrease the value of the quantity by one
  - The user click on the field manually and type the number they wish to add to the basket
- < Keep Shopping - will return the user to the menu page
- Add to Basket - will take product on the page, and the quantity in the selector, and add that ammount of the product into the basket

Basket Page:

- A quantity form for a user to alter the value of the quantity currently in the basket
  - The "+" will increase the value of the quantity by one
  - The "-" will decrease the value of the quantity by one
  - The user click on the field manually and type the number for the the quantity they want in the basket
- Update - the basket will be updated with the quantity that is shown in the selector
- Remove - the item in which the "Remove" anchor is associated with will be removed from the basket
- < Keep Shopping - will return the user to the menu page
- Secure Checkout - will navigate the user to the checkout page with the basket on the current page

Checkout Page:

- Input fields
  - Full Name - User must enter their name
  - E-mail - User must enter their e-mail
  - Phone Number - User must enter their phone number
  - Street Address 1 - User must enter the first line of their address
  - Street Address 2 - User can enter the second line of their address 
  - Town or City - User must enter their town or city
  - Postal Code - User can enter their postal code
  - County, State or Locality - User can enter their county, state or locality
- Create an Account - will navigate the user to the sign up page
- Login - will navigate the user to the login page
- Payment input field - the user must enter their credit card information to proceed with the order
- < Adjust Basket - will return the user to the basket page
- Complete Order - will attempt to process the users order, if successful will navigate the user to the checkout success page

Checkout Success Page:

- This page will display all the information relevant to the order
  - Order Info
    - Order Number
    - Order Date
  - Order Details
    - A list of the products that were in the basket of the order
  - Deliveriy Details
    - The Full Name, Address, County, Town or City, Post Code and Phone Number
  - Billing Information
    - Order Total
    - Delivery Charges
    - Grand Total

Sign Up Page:

- Sign In - an anchor tag that will navigate the user back to the login page if they already have an account
- Sign Up Form - List of text inputs required for a user to set up a user profile
  - E-mail Address
  - E-mail Address confirmation
  - Username
  - Password
  - Password (again)
- Back to Login - An anchor tag that will navigate the user back to the login page if they already have an account
- Sign Up - A button to submit the form and create a user profile if what the user has enetered it valid

Verification Pages:

- E-mail confirmation - A confrim button verifies the profiles e-mail address so the account can be used on the site.
- 
- 
- 

Login Page:

- 
- 
- 
- 

Profile Page:

- 
- 
- 
- 

Password Reset Page:

- 
- 
- 
- 

Toasts:

- 
- 
- 
- 

Error Pages:

- 
- 
- 
- 

---

#### **Information Design:**

Navbar:

- 
- 
- 
- 

Menu Page:

- 
- 
- 
- 

Menu Product Details Page:

- 
- 
- 
- 

Basket Page:

- 
- 
- 
- 

Checkout Page:

- 
- 
- 
- 

Checkout Success Page:

- 
- 
- 
- 

Profile Page:

- 
- 
- 
- 

Login Page:

- 
- 
- 
- 

Sign Up Page:

- 
- 
- 
- 

Password Reset Page:

- 
- 
- 
- 

Verification Pages:

- Verification Sent - This page will inform you that you should have an email in your inbox that will finalize the setup proccess.
- Email Confirmation - This page will advise you of the email you are confiming above the confirmation button.
- 
- 

Toasts:

Examples of potential messsages a user will see in their toast pop ups while navigating the site

- Success
  - You successfully added a product to your basket.
  - You successfully updated the quantity of a product to your basket.
  - You successfully removed a product to your basket.
  - You successfully proccessed the order.
  - You confirmed you email address from pressing confirm on the verify email link.
  - You successfully changed the password for your profile.
  - You successfully signed out of your profile.
- Alert
  - When signing up it will alert when we have sent you an email to verify your e-mail address.
  - When viewing an order from your order history an alert will confirm that this a "past" confirmation rather than a new order.
- Warning
  - If there is an issue with stripe
- Error
  - When there is nothing in your basket
  - If there was a problem adding, updating or removing an item from your basket

Error Pages:

- 
- 
- 
- 

---

[Return to Table of Contents](#table-of-contents)

---

### **Skeleton**

---

### **Surface**

#### **Images**



#### **Colours**



#### **Typography**

- 

---

[Return to Table of Contents](#table-of-contents)

---

## [Wireframes](#wireframes)

---

### Hompage
![homepage](static/wireframes/1.home-page.png "image_tooltip")
### Menu on Large Screens
![menu](static/wireframes/2.menu-large.png "image_tooltip")
### Menu on Medium Screens
![menu](static/wireframes/3.menu-mid.png "image_tooltip")
### Menu on Small Screens
![menu](static/wireframes/4.menu-small.png "image_tooltip")
### Menu Product Details on Large Screens
![product](static/wireframes/5.menu-product-details-large.png "image_tooltip")
### Menu Product Details on Large Screens with Toasts
![product](static/wireframes/6.menu-product-details-with-toast-large.png "image_tooltip")
### Menu Product Details on Medium and Small Screens
![product](static/wireframes/7.menu-product-details-mid&small.png "image_tooltip")
### Menu Product Details on Medium and Small Screens with Toasts
![product](static/wireframes/8.menu-product-details-with-toast-mid&small.png "image_tooltip")
### Basket
![basket](static/wireframes/9.basket.png "image_tooltip")
### Basket on Medium and Small Screens
![basket](static/wireframes/10.basket-mid&small.png "image_tooltip")
### Checkout
![checkout](static/wireframes/11.checkout.png "image_tooltip")
### Checkout on Medium and Small Screens
![checkout](static/wireframes/12.checkout-mid&small.png "image_tooltip")
### Checkout Success
![checkout](static/wireframes/13.checkout-success.png "image_tooltip")
### Checkout Success with Toasts
![checkout](static/wireframes/14.checkout-success-with-toast.png "image_tooltip")
### Checkout Success on Medium and Small Screens
![checkout](static/wireframes/15.checkout-success-small&mid.png "image_tooltip")

---

[Return to Table of Contents](#table-of-contents)

---

---

- 
![alt_text](static/images/wireframes/wireframe-1.png "image_tooltip")

---

[Return to Table of Contents](#table-of-contents)

---

## **Features**

---

### **Existing Features**

- Designed with HTML5, CSS3, JavaScript and Python.
- 
- 
- 
- 

### **Features Left to Implement when skills develop**

- Timer
- Collection
- Loyalty Tokens - Users who post their meals on social media
- 

---

[Return to Table of Contents](#table-of-contents)

---

## **Testing**

---

### **Screen Testing**

Checked compatibility in Safari, Chrome, Firefox

#### Google Chrome Developer Tools - Device frames tests

- Moto G4
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5/SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone X
- iPad
- iPad Pro
- Surface Duo
- Galaxy Fold

#### Desktop Screen Sizes

- 24" - 1920x1200
- 23" - 1920x1080
- 22" - 1680x1050
- 20" - 1600x900

#### Notebook Sizes

- 15" - 1366x768
- 13" - 1024x800
- 10" - 1024x600

#### Tablet Screen Sizes

- iPad Mini - 768x1024
- iPad Retina - 768x1024
- iPad Pro - 1366x1024
- Kindle Fire - 768x1024
- Kindle Fire HD - 768x1024
- Asus Eee - 768x1024
- Nexus 7 - 600x960
- Nexus 9 - 1024x768
- Galaxy Tab 10 - 800x1280

#### Tablet Screen Sizes

- Apple iPhone 3/4/4s - 320x480
- Apple iPhone 5/5s - 320x586
- Apple iPhone 6/6s/7 - 375x667
- Apple iPhone 6 Plus/7 Plus - 414x736
- Samsung Galaxy S5/S6/S7 - 360x640
- Sony Xperia Z2/Z3 - 360x640
- Google Pixel - 411x731
- Nexus 4 - 384x640
- Nexus 5 - 411x731
- Nexus 6 - 411x731

I have tested the website on various physical devices (iPad, iPad Air, Macbook Pro)

### **Validator**

- HTML - [W3C](https://validator.w3.org/) - Markup Validation

- CSS - [W3C](https://jigsaw.w3.org/css-validator/) - Jigsaw CSS Validation

- JavaScript - [JSHINT](https://jshint.com/) - JavaScript code warning & error check

- Python - [Pyton Tester](https://extendsclass.com/python-tester.html) Python code syntax checker

### **Defensive Design**

- User can navigate throughout the site without the need to press the "back" or "forward" buttons in the browser interface.
- 
- 
- 

---

[Return to Table of Contents](#table-of-contents)

---
### **Manual**
---

Navbar:

- 
- 
- 
- 

Menu Page:

- 
- 
- 
- 

Menu Product Details Page:

- 
- 
- 
- 

Basket Page:

- 
- 
- 
- 

Checkout Page:

- 
- 
- 
- 

Checkout Success Page:

- 
- 
- 
- 

Profile Page:

- 
- 
- 
- 

Login Page:

- 
- 
- 
- 

Sign Up Page:

- 
- 
- 
- 

Password Reset Page:

- 
- 
- 
- 

Verification Pages:

- 
- 
- 
- 

Error Pages:

- 
- 
- 
- 

---

[Return to Table of Contents](#table-of-contents)

---
### **Automated**
---

|         Test Case - User Profiles         | Result |
|:-----------------------------------------:|:------:|
|          Create a User Profile            |  Pass  |
|    Logging in with a verified account     |  Pass  |
|       Logging out of a User Profile       |  Pass  |

---

|                 Test Case - Creating an Order                | Result |
|:------------------------------------------------------------:|:------:|
|                Adding a product to the basket                |  Pass  |
|       Updating the quantity of a product in the basket       |  Pass  |
|              Removing a product from the basket              |  Pass  |
|             Taking a basket to the checkout page             |  Pass  |
| Filling out the form and payment details to process an order |  Pass  |

---

|              Test Case - Error Testing             | Result |
|:--------------------------------------------------:|:------:|
| Trying to create a user with an already used email |  Pass  |
|     Trying to log in with an unverified profile    |  Pass  |
|            Trying to access the checkout page without any items in your basket            |  Pass  |
| Trying to access the profile page without having signed into a account throws a 404 error |  Pass  |

---

[Return to Table of Contents](#table-of-contents)

---

### **Bugs**

---

#### **Found**

1. 
2. 
3. 
4. 

#### **Resolution**

1. 
2. 
3. 
4. 

#### **Unresolved**

- 
- 
- 
- 

[Return to Table of Contents](#table-of-contents)

---

## **Technologies Used**

---

### **1. Languages**

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### **2. Integrations**

- [Materialize](https://materializecss.com/) by linking via [Materialize CDN](https://materializecss.com/getting-started.html) to HTML Doc
- [jQuery](https://jquery.com) by linking via jQueryCDN to HTML Doc.
- [FontAwesome](https://fontawesome.com/) Icons for links in Footer.
- [Google Fonts](https://fonts.google.com/) - Overall Typography import.
- [Django](https://www.djangoproject.com/) Python Web framework that encourages rapid development.

### **3. Workspace, version control and Repository storage**

- [GitPod](https://github.com/mkuti/corklagos-venture/blob/master/gitpod.io) - Main workspace IDE(Integrated Development Environment)
- [Git](https://git-scm.com/) - Distributed Version Control tool to store versions of files and track changes.
- [GitHub](https://github.com/) - A cloud-based hosting service to manage my **Git** repositories.
- [Heroku](https://heroku.com) - Container-based cloud platform for deployment and running of apps.

---

[Return to Table of Contents](#table-of-contents)

---

## **Resources**

---

- [Code Institute Course Content](https://courses.codeinstitute.net/)
- Code Institute **SLACK Community**
- [Coolers](https://coolors.co/) - Color picker
- [Stack Overflow](https://stackoverflow.com/) - General resource
- [Youtube](https://www.youtube.com/) - General resource
- [CSS-Tricks](https://css-tricks.com/) - General resource
- [W3.CSS](https://www.w3schools.com/w3css/4/w3.css) - General resource
- [Balsamiq](https://balsamiq.com/wireframes/) - Wire-framing design tool
- Unicorn Revealer - Chrome Extension
- ColorZilla - Chrome Extension

---

[Return to Table of Contents](#table-of-contents)

---

## **Project barriers**

---

- 
- 
- 
- 

---

[Return to Table of Contents](#table-of-contents)

---

## **Deployment**

---

GitPod was used to write all code in this repository and pushed via Git to GitHub.

### Local Installation

#### 1. Cloning the project

- The code can be run locally through clone or download from the repository on [GitHub]("").
- You can do this by opening the repository, clicking on the Code' button and selecting either 'clone or download'.

![Image](static/images/cloning.png)
- The Clone option provides a URL, which you can use on your CLI with `git clone <paste url>`.
- The Download ZIP option provides a link to download a ZIP file that can be unzipped on your local machine. The files can then be uploaded to your IDE.

#### 2. Create Environmental Variables

- Create an env.py file, in this file enter the Environmental Variables (**replace values with your own**) as follows:

```python
        import os

        os.environ.setdefault("IP", "IP_ADDRESS")
        os.environ.setdefault("PORT", "PORT")
        os.environ.setdefault("SECRET_KEY", "SECRET_KEY")
        os.environ.setdefault("MONGO_URI", "MONGO_URI")
        os.environ.setdefault("MONGO_DBNAME", "MONGO_DBNAME")
```

#### 3. Create a .gitignore file

- Create a file called **.gitignore** in the root directory and ensure it contains the following git exclusions:

```text
        core.Microsoft*
        core.mongo*
        core.python*
        env.py
        .env
        __pycache__/
        *.py[cod]
        node_modules/
        *sqlite3
        *.pyc
```

#### 4. Install project dependencies

- Install project requirements by typing `pip install -r requirements.txt`

#### 5. Create a database on MongoDB

Register for a free account with [MongoDB](https://account.mongodb.com/account/register)

- Create a new Project and call it 'ShakesOnTheBeach'.
- Create a Cluster, choose the free tier option and select your region, the name I choose was 'ShakesOnTheBeach'.
- Create a new database and call it 'Shakes-on-the-Beach'.
- Create Collections named '', '', '', '' and 'users' an enter key/values as follows:  

- **users** collection

```json
            _id: <ObjectId>
            username: "<string>"
            password: "<string>"
```

#### 6. Deploy locally

- To run the project locally, in the terminal type `python3 manage.py runserver`
- This will open a localhost address, which is provided in the CLI.

#### 7. Remote Deployment on Heroku

[Heroku](https://www.heroku.com) is a Cloud Application Platform that enables developers to build, run, and operate applications in the cloud.

The Deployment process is as follows:

Create a **requirements.txt** file to store dependencies of installed packages for the project. In the CLI type `pip freeze --local > requirements.txt`.

Create a file named **Procfile** to declare what commands are run by the application's dynos on the Heroku platform. For this project, run by the app.py file, the Procfile should contain: `web: python app.py`

- Register for a free account on the Heroku [Signup](https://signup.heroku.com/login) page.
- On the Dashboard, click the 'New' button and select 'Create new app'.
- Choose a name and region.
- Under the 'Settings' tab, click on 'Config Vars' to add Configuration Variables from the env.py file (As shown in step **3. Create Environmental Variables** above). Remember to use your own credentials.
- In your CLI terminal install Heroku by typing `npm install -g heroku`
- Select the 'Deploy' option from the menu.
- Under the 'Deployment method' select the GitHub option to connect to your GitHub repository. Ensure GitHub Username is selected and use the search function to find the relevant repository. It is recommended to use a 'main' branch as default, due to GitHub depreciating the 'master' branch name.
- Select Automatic deploys from the main branch and click 'Deploy Branch'.
- Click on the 'Open App' button on the top-right to open the deployed app.
- There is no difference between the deployed version and the development version.

---

[Return to Table of Contents](#table-of-contents)

---

## **Credits**

---

### **Media**

Favicon

- [Image](https://www.google.com/url?sa=i&url=https%3A%2F%2Ffreepngimg.com%2Fpng%2F10976-beach-png-images%2Ficon&psig=AOvVaw0BDiH7b_mnvotE5Q96c7p8&ust=1629389804662000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCJCugZb8uvICFQAAAAAdAAAAABAD)

Pictures

- All photos with names ending in "-stock" in the media folder were taken from [shutterstock](https://www.shutterstock.com/)
- About page [image](https://business.facebook.com/ParadiseCoveBeachCafe/photos/a.594035813999865/5517528321650565/?type=3&theater)
- Gallery page [image](https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/beach-quotes-1559667853.jpg)
- Burgers
  - [Cheese Burger](https://assets.epicurious.com/photos/5c745a108918ee7ab68daf79/master/pass/Smashburger-recipe-120219.jpg)
  - [Bacon Cheese Burger](https://simply-delicious-food.com/wp-content/uploads/2015/07/Bacon-and-cheese-burgers-3-480x270.jpg)
  - [The Hot Chick](https://www.recipetineats.com/wp-content/uploads/2017/07/Chicken-Burgers-4.jpg)
  - [Grilled Jerk Chicken Burger](https://www.thepetitecook.com/wp-content/uploads/2018/04/Chicken-Burger-1.jpg)
- Pizza
  - [Meat Central](https://media-cdn.tripadvisor.com/media/photo-s/0b/38/d7/4e/meat-lovers-pizza.jpg)
  - [Hawaiian Five OH!](https://i.ytimg.com/vi/dJ8gWah4axo/maxresdefault.jpg)
  - [Hot Veggie](https://media-cdn.tripadvisor.com/media/photo-s/0e/bc/93/c6/four-star-pizza.jpg)
  - [Hot Passion](https://previews.123rf.com/images/dedmityay/dedmityay1704/dedmityay170400020/75325776-fresh-hot-meat-pizza-in-a-box-delivery-of-fast-food-concept.jpg)
- Sandwiches
  - [BLT](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/posh-blt-2c4aa27.jpg?quality=90&webp=true&resize=440,400)
  - [Southern Fried Panini](https://www.rockrecipes.com/wp-content/uploads/2011/09/Fried-Chicken-Club-Sandwich-Panini-pn-a-wooden-cutting-board-with-coleslaw-in-background-1.jpg)
  - [Veggie Ciabatta](https://4.bp.blogspot.com/-KxpMdpQ2a6w/UHH1TfrcH_I/AAAAAAAAA9E/QH3owDBDyik/s1600/IMG_2359.jpg)
  - [Red Hot Wrap](https://i2.wp.com/studenteats.co.uk/wp-content/uploads/2015/07/student-eats-meals-recipes-16.jpg?fit=800%2C536&ssl=1)
- Salads
  - [Beetroot Relish](https://cdn.scrambledchefs.com/wp-content/uploads/2015/07/Beetroot-and-Feta-Cheese-Salad-_-Scrambled-Chefs-5.jpg)
  - [Split pea Hummus](https://www.brewinghappiness.com/wp-content/uploads/2017/05/featured-image-3.jpg)
  - [Baba Ghanoush](https://tarateaspoon.com/wp-content/uploads/2021/01/Loaded-Roasted-Veggie-Baba-Ganoush-close-horiz.jpeg)
  - [Fijian Kokoda](https://i1.wp.com/nationalfoods.org/wp-content/uploads/2017/07/National-Dish-of-Fiji-Fijian-Kokoda-food.jpg?resize=640%2C480&ssl=1)
- Shake
  - [Chocolate Malt](https://thelemonbowl.com/wp-content/uploads/2017/06/Dark-Chocolate-Malt-with-Cinnamon-an-ice-cream-dessert-recipe.jpg)
  - [Oreo Cookie Malt](https://thesaltymarshmallow.com/wp-content/uploads/2018/08/oreo-milkshakes2.jpg)
  - [Peanut Butter Malt](https://storcpdkenticomedia.blob.core.windows.net/media/recipemanagementsystem/media/recipe-media-files/recipes/retail/x17/17932-double-chocolate-peanut-butter-malt-600x600.jpg?ext=.jpg)
  - [Mint Chocolate Malt](https://realfood.tesco.com/media/images/RFO-MAIN-472x310-CSRMilkshake-7dcab72d-ac8c-4bd9-9bf6-e0ca0327acd6-0-472x310.jpg)
  - [Nutella Malt](https://www.halfbakedharvest.com/wp-content/uploads/2015/08/Salted-Pretzel-Nutella-Fudge-Milkshake-with-Malted-Milk-Whipped-Cream-5.jpg)
  - [Vanilla Malt](https://www.thespruceeats.com/thmb/RyfnsTX6chkOkwmJtT4j-NPe3pY=/2624x3936/filters:fill(auto,1)/vanilla-malted-milk-shake-recipe-909370-hero-01-5bdcc3e1c9e77c0051bb2a21.jpg)
  - [Strawberry Malt](https://www.chelseasmessyapron.com/wp-content/uploads/2020/04/Strawberry-Milkshake-1.jpg)
- Mineral
  - [Soft Drinks](https://cdn-a.william-reed.com/var/wrbm_gb_food_pharma/storage/images/publications/food-beverage-nutrition/foodnavigator-asia.com/article/2018/03/29/soft-drink-health-concerns-not-yet-trickled-down-into-social-media-users-mentions-of-brands/7819019-1-eng-GB/Soft-drink-health-concerns-not-yet-trickled-down-into-social-media-users-mentions-of-brands.jpg)
  - [Water](https://cdn3.evostore.io/productimages/vow_premium/l/lb0007.jpg)
  - [Capri Sun](https://digitalcontent.api.tesco.com/v2/media/ghs/687d33aa-bd47-4052-8960-e04e8bea272a/snapshotimagehandler_120314822.jpeg?h=540&w=540)

### **Code Snippets**

''

---

[Return to Table of Contents](#table-of-contents)

---

## **Acknowledgements**

---

### I would like to thank

- **[CI staff](https://codeinstitute.net/)** and **[Slack Community](https://slack.com/intl/en-ie/)**
- **[Guido Cecilio](https://github.com/guidocecilio)** - My mentor, for his time and guidance.
- **[Sean Murphy](https://github.com/nazarja)** - For his knowledge and reliable feedback.
- **[Anthony O'Brien](https://github.com/auxfuse)** - For his expertise in the industry.
- **[Jim Lynx](https://github.com/JimLynx)** - For his support and assistance.

---

## **Support**

---

If you require any help or assistance you may contact me on

john.doyle.mail@icloud.com

---

[Return to Table of Contents](#table-of-contents)

---