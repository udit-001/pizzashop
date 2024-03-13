## Database Schema
Here is the database schema employed within the application:

### Menu Items

[![Database Schema](/docs/menu-items.svg 'Pizza Shop Database Schema')](https://dbdiagram.io/d/Pizza-Shop-62c5666869be0b672caea8e3)

Several tables are employed to store information about menu items, including Regular Pizza, Salad, Sicilian Pizza, Topping, Extra, Sub, Pasta, and Platter. These tables contain essential details about each menu item, such as its name and price.


[![Database Schema](/docs/orders-user.svg 'Pizza Shop Database Schema')](https://dbdiagram.io/d/Pizza-Shop-62c5666869be0b672caea8e3)

### Payment
The Payment table is utilized to store metadata related to payment transactions processed through Stripe. Each payment is linked to a user and an order.

### Orders
The OrderItem, Order, and OrderItemLink tables are employed to record information about user orders. The name and price in the OrderItem table are derived from the combination of menu items selected by the user during checkout. 

Presently, the relationship between OrderItem and Order is ManyToMany, established through an intermediate table called OrderItemLink. While this design choice was made during the project's development, I now believe it could be enhanced by adding a ForeignKey directly in the OrderItem table, eliminating the need for a separate through table.

### Address
Users can have multiple addresses associated with their account. Therefore, the Address table has a foreign key relationship with the user table. This table includes all the necessary fields to store a user's address.

## User Cart
The application's cart mechanism operates through the utilization of the `is_ordered` boolean flag within the order table. Once the user successfully completes the payment process, the `is_ordered` field is set to True. Following the completion of payment, the user will no longer view the items in the cart. Instead, they can find the order on the "My Orders" page.

## Authentication
This project offers various authentication methods, including:

1. Email and Password Authentication
2. [Google OAuth](https://docs.allauth.org/en/latest/socialaccount/providers/google.html#app-registration)
3. [GitHub OAuth](https://docs.allauth.org/en/latest/socialaccount/providers/github.html)
4. [Facebook OAuth](https://docs.allauth.org/en/latest/socialaccount/providers/facebook.html)

Social authentication features are facilitated by the [django-allauth](https://github.com/pennersr/django-allauth) provider.

Here's the database schema for the social authentication:

[![Database Schema](/docs/social-auth.svg 'Pizza Shop Database Schema')](https://dbdiagram.io/d/Pizza-Shop-62c5666869be0b672caea8e3)

## Payment
This project utilizes Stripe to collect credit card payments from users for their orders, leveraging [Stripe's Python SDK](https://github.com/stripe/stripe-python). Subsequently, we retain the transaction details in our database for reference, as demonstrated [here.](#payment)

## Google Places Integration
The application is equipped with [Google Places library](https://developers.google.com/places/) to assist users in entering accurate address details. This feature presents users with an autocomplete input, allowing them to select their address from a list of verified options provided by Google. This integration aims to mitigate delivery issues caused by inaccurate addresses.

Additionally, users have the option to autofill their address using their current location, which streamlines the address entry process and saves time.

## Security
Ensuring the highest level of security is our top priority, and we have implemented various measures within the project. Here is a detailed overview:

### Project Secrets Management
In our project, we have prioritized security by storing all sensitive project secrets in a special file called .env. To achieve this, we rely on a convenient package called [django-environ.](https://github.com/joke2k/django-environ) This package helps us retrieve these secrets directly from the .env file located in our project directory.

### reCaptcha Protection
To fortify our system against automated attacks, we have integrated a security feature using the [django-reCAPTCHA](https://github.com/praekelt/django-recaptcha) library. This library serves as a defense mechanism, helping us distinguish between human users and automated bots, thus adding an additional layer of protection.

When someone interacts with our system, especially during sensitive actions like login or registration form submissions, reCAPTCHA steps in.

Specifically, the project utilizes [ReCaptchaV2Invisible](https://developers.google.com/recaptcha/docs/invisible), which monitors user behavior instead of requiring the user to solve a challenge.
