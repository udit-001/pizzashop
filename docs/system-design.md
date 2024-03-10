## Database Schema
Here is the database schema employed within the application:

[![Database Schema](/docs/pizza-shop.svg 'Pizza Shop Database Schema')](https://dbdiagram.io/d/Pizza-Shop-62c5666869be0b672caea8e3)

## Database Description
Here is a concise overview of the different tables presented in the diagram above:

### Menu Items
Several tables are employed to store information about menu items, including Regular Pizza, Salad, Sicilian Pizza, Topping, Extra, Sub, Pasta, and Platter. These tables contain essential details about each menu item, such as its name and price.

### Payment
The Payment table is utilized to store metadata related to payment transactions processed through Stripe. Each payment is linked to a user and an order.

### Orders
The OrderItem, Order, and OrderItemLink tables are employed to record information about user orders. The name and price in the OrderItem table are derived from the combination of menu items selected by the user during checkout. 

Presently, the relationship between OrderItem and Order is ManyToMany, established through an intermediate table called OrderItemLink. While this design choice was made during the project's development, I now believe it could be enhanced by adding a ForeignKey directly in the OrderItem table, eliminating the need for a separate through table.

### Address
Users can have multiple addresses associated with their account. Therefore, the Address table has a foreign key relationship with the user table. This table includes all the necessary fields to store a user's address.

## Authentication
This project offers various authentication methods, including:

1. Email and Password Authentication
2. Google OAuth
3. GitHub OAuth
4. Facebook OAuth

Social authentication features are facilitated by the [django-allauth](https://github.com/pennersr/django-allauth) provider.

## Payment
This project utilizes Stripe to collect credit card payments from users for their orders, leveraging Stripe's Python SDK.

## Google Places Integration
The application is equipped with [Google Places library](https://developers.google.com/places/) to assist users in entering accurate address details. This feature presents users with an autocomplete input, allowing them to select their address from a list of verified options provided by Google. This integration aims to mitigate delivery issues caused by inaccurate addresses.

Additionally, users have the option to autofill their address using their current location, which streamlines the address entry process and saves time.
