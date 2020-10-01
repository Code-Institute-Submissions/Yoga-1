<img src="https://i.imgur.com/BEAE1lf.png" style="margin: 0;">

# Milestone 4 - SpiritusYoga.no

## Description
---

This is my 4th. and final Milestone in the Full Stack Software developer course With Code Institute.
In our final project we going to show the skills we've learn during the course and the project
needed to be a full stack project, we got different scopes to choose from and I have chosen a project 
that I've made for a friend after I had finished my MS1, which only contained HTML and CSS. 

The project is for a small Yoga studio where people can come and teach about Yoga and to practice Yoga,
She is a certified Yoga instructor and offers three different kinds of sessions. The site will offer
basic information about the courses she offers, as well as the possibility to create an 
account, login, add courses to the basket and go to checkout to pay for the courses.  

Since I've not been able to finish up my project there is a lot of things missing and there is no styling for
the project. So things like userprofile, order history missing and more.

## UX
My goal was to create an upgrade of my earlier design and to add more features and value to the site. 
(Click the link to see: https://weekend79.github.io/spiritusyogamarie/index.html)
The website consists of home, products/courses, account and shopping bag with a functional checkout, where 
Stripe has been integrated for Visa and Mastercard payments. You will also get a receipt with a confirmation
to your email which is only available to see in the terminal. 

There are some toasts in the project together with webhooks with the Stripe payment.  

For the owner of the site the goal is to sell Yoga classes directly in her website and to promote and inform 
possible clients what Yoga is about and when there are new classes available.

The Site can be found here: https://spiritusyoga.herokuapp.com/

## User Stories
As a customer I would like:

* View/Read about Courses / Classes (product)
* See a specific course and read about it
* See the details of a particular courses
* See the total of my shopping bag
* Easy access to my shopping bag
* Choose quantity
* See my order history
* See my profile
* Edit my profile
* Make a purchase
* Contact admin
* Read about the person(s) behind the site
* Receive an email with the order confirmation after completing the checkout.
* View my order confirmation after completing the checkout.
* Register
* Sign in
* Sign out 
* Edit password
* Ask for my password recovery
* Received an email about my purchase

As a site owner I would like:
* Add a new course
* Delete course
* Edit a course
* See my contacts from the form
* See my clients
* Change admin password
* Change admin e-mail
* See order details
* Order History

## Features
* User Authentication
* Login User and admin
* Shopping bag: add courses, update quantity (Not possible to delete)
* Checkout with Stripe payment
* Admin site manager


## Missing Features
* Add contact form
* Add user profile
* Add order History
* Expand the sign up with sosial accounts


## Technologies 

I have use the following technologies:
* HTML
* CSS
* Bootstrap4: Framework for my responsive design 
* GoogleFont: For my Roboto font family
* FontAwesome: For Icons
* JQuery: For manipulating the DOM
* JavaScript: For activating the carousel, and for Stripe
* Python3: main programming language
* Django3: As the full stack Framework
* Pip3: To install side packages
* Stripe: As payment
* Pillow: Python image library
* GitHub: For version control of my code
* AWS: Using S3 to store my static and media fils.
* Imgur: For some static files
* Heroku: Where my app is deployed and 
          I using Heroku Postgres Database
* SqLite3: As a backup database if my main database 
           Connection fails.

## Testing

Only manual testing have been done and there is no automated tests been used during the
development. The main issues that have been found during manually testing is:

* Not possible to delete items from shopping bag
* Not possible to verify a new account when signing up, only from terminal or Heroku. 
(So to login use these credentials:
User: Happy
Pass: Good1234
  )


## Code Validation

There haven't been done any code Validation

## Deployment 
    - Live demo: https://spiritusyoga.herokuapp.com/
    - GitHub repo: https://github.com/weekend79/Yoga

## Credits
The project is inspired by my friend

## Code 
I have follow the LMS example Boutique Ado and refactored the code where needed, to find ways 
to have my own features.

## Content / Media 
    - The images and logo are SpiritusYogaMarie's ownership and I have been given the permission to use it 
      for my MS4


## Special Thanks
I would like to give a special thanks to Code Institute for this amazing journey! To the tutors and to my mentor 
Reuben Ferrante for all the help and support thrugh out the course. 

## Disclaimer

This project is for educational purposes only.