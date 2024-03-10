# Pizzashop 

[![HitCount](http://hits.dwyl.com/udit-001/pizzashop.svg)](http://hits.dwyl.com/udit-001/pizzashop)


## Overview 
This is an app for handling a pizza restaurant’s online orders. Customers will be able to browse the restaurant’s menu, add items to their cart, and submit their orders. They can also add addresses, edit existing addresses. Meanwhile, the restaurant owners will be able to add and update menu items, and view orders that have been placed.


## Database Schema
Here is the database schema employed within the application:

[![Database Schema](/docs/pizza-shop.svg 'Pizza Shop Database Schema')](https://dbdiagram.io/d/Pizza-Shop-62c5666869be0b672caea8e3)

## Running the Project
1. **Run using Docker Compose**: Ensure you have Docker Compose installed on your system. Navigate to the project's root directory and run the following command to build and start the application and its services:

   ```
   docker compose up -d
   ```

2. **Access the Application**: After successfully launching the containers, you can access the application in your web browser at http://localhost:8000
3. **Demo Admin Access** : To access the admin panel, visit http://localhost:8000/admin and use the following credentials:

    - Username: demo
    - Password: demo@123

## Features
- 🍴 **Menu** : The app allows the customer to be able to browse the menu, listing all the menu items, their size variations and their respective prices.

- ➕ **Adding Items** : Using the admin site, restaurant owners can add, update and remove items on the menu.

- 👤 **Registration, Login, Logout** : Customers can register on the application with an email address, password. They can login and logout of our website.

- 🛒 **Shopping Cart** : Once logged in, customers can see all the menu items in the menu, they can add items (along with toppings or extras, if appropriate) to their virtual “shopping cart.” The contents of the shopping are saved even if a customer closes the window, or logs out and logs back in again.

- ☑️ **Placing an Order**: Once there is at least one item in a customer’s shopping cart, they are able to place an order, whereby the customer is asked to confirm the items in the shopping cart, and the total before placing an order.

- 👁️ **Viewing Orders** : Restaurant owners have access to a page where they can view any orders that have already been placed.

- 🕘 **Order Status** : Allows restaurant owners to mark orders as complete and allowing customers to see the status of their pending or completed orders.

- 📍 **Shipping Addresses** : Allows customers to add multiple shipping addresses to their profile which can be selected while placing an order, it also lets the customers edit or remove addresses.

- 💳 **Payment Integration** : The app comes integrated with the Stripe API to allow customers to actually use a credit card to make a purchase during checkout.

- 🔗 **Social Logins** : Allows the customer to be able to signup and login using social authentication providers such as Google & Facebook.

## Technical Details
Libraries used in this project are:

### Frontend 
- [UI Kit](https://getuikit.com/) : A lightweight and modular front-end framework
for developing fast and powerful web interfaces.
- [Places API](https://developers.google.com/places/) : Allows user to be able to add addresses based on their current location and also provides autocomplete functionality for ease of use while adding addresses.

### Backend
- [Django Allauth](https://github.com/pennersr/django-allauth): Used to provide Facebook and Google Registration and Login functionality.
- [Django-environ](https://github.com/joke2k/django-environ) : Used to configure secret keys, API keys through environment variables.
- [Django-recaptcha](https://github.com/praekelt/django-recaptcha) : Allows us to add Google Recaptcha fields to our forms for spam protection.
- [Stripe](https://github.com/stripe/stripe-python): Python wrapper for the Stripe API that allows us to accept payments on our platform.
- [Whitenoise](https://github.com/evansd/whitenoise): Allows us to serve static files without relying on nginx or any other external service.
