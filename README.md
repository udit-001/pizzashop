# Pizzashop 

[![HitCount](http://hits.dwyl.com/udit-001/pizzashop.svg)](http://hits.dwyl.com/udit-001/pizzashop)


## Overview 
This is an app for handling a pizza restaurant’s online orders. Customers will be able to browse the restaurant’s menu, add items to their cart, and submit their orders. They can also add addresses, edit existing addresses. Meanwhile, the restaurant owners will be able to add and update menu items, and view orders that have been placed.

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

## System Design
For additional insights into the system design of this application, please refer to the document provided [here.](/docs/system-design.md)

## Running the Project Locally
1. **Run using Docker Compose**: Ensure you have Docker Compose installed on your system. Navigate to the project's root directory and run the following command to build and start the application and its services:

   ```
   docker compose up -d
   ```

2. **Access the Application**: After successfully launching the containers, you can access the application in your web browser at http://localhost:8000
3. **Demo Admin Access** : To access the admin panel, visit http://localhost:8000/admin and use the following credentials:

    - Username: `demo`
    - Password: `demo@123`

4. **Social Authentication**: The project includes built-in support for social authentication with Google, Facebook, and Github.

    - [Google OAuth](https://docs.allauth.org/en/latest/socialaccount/providers/google.html#app-registration): This feature is readily available and uses demo credentials configured within the app. If you wish to use your own credentials, modify the Google App entry at the following link: `http://localhost:8000/admin/socialaccount/socialapp/`.

    - [Facebook OAuth](https://docs.allauth.org/en/latest/socialaccount/providers/facebook.html): Out-of-the-box functionality is not provided for Facebook Authentication. However, you can refer to the [django-allauth docs](https://docs.allauth.org/en/latest/socialaccount/providers/facebook.html) and follow the steps to add a social app through the following link: `http://localhost:8000/admin/socialaccount/socialapp/add/`

    - [GitHub OAuth](https://docs.allauth.org/en/latest/socialaccount/providers/github.html): Similar to Facebook Authentication, GitHub Authentication requires configuration and does not work automatically. Follow the instructions in the [django-allauth docs](https://docs.allauth.org/en/latest/socialaccount/providers/github.html) to add an entry here: `http://localhost:8000/admin/socialaccount/socialapp/add/`.

5. **Google reCAPTCHA**: By default, the project uses Google's testing keys when in development mode.


## Deploying the Project:
To deploy the project to a production environment, utilize our Docker Compose setup as follows:

### Step 1: Clone the project on server
Begin by cloning the project repository onto your server using the following command:

```bash
git clone https://github.com/user-name/repo-name.git
```

Navigate to the project directory:
```bash
cd pizzashop
```


### Step 2: Installing Docker and Docker Compose
For production deployment, it is presumed that you are operating on a Linux-based server. Refer to any of the Digital Ocean tutorials tailored to your Linux distribution for installing Docker. These tutorials can be found [here.](https://www.digitalocean.com/community/tutorial-collections/how-to-install-and-use-docker)

### Step 3: Configuring Environment Variables
Before running the project, configure the necessary environment variables for key dependencies. These include:

- `DEBUG`
- `SECRET_KEY`
- `DATABASE_URL`
- `ALLOWED_HOSTS`
- `RECAPTCHA_PUBLIC`
- `RECAPTCHA_PRIVATE`
- `STRIPE_KEY`
- `SENDGRID_API`

#### Step 3.1: Copy the .env.example File
Execute the following command to create a copy of the environment file:
```bash
cp .env.example .env
```

#### Step 3.2: Set Django Settings Values
Adjust the values for the following settings in the newly created .env file:

- `ALLOWED_HOSTS` : Specify the domain of the server to make the app accessible. Refer to [this section](https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts) in the Django documentation for further details.
- `SECRET_KEY` : Assign a unique and unpredictable value. Utilize a [Django secret key generator](https://djecrety.ir/) for assistance. The `SECRET_KEY` is crucial for various security purposes in Django, as explained in the [documentation](https://docs.djangoproject.com/en/dev/ref/settings/#secret-key).
- `DEBUG` : Ensure this variable is set to False. Debug mode should never be enabled in a production environment. For further details, refer to [this section](https://docs.djangoproject.com/en/dev/ref/settings/#std-setting-DEBUG) of the Django docs.


### Step 4: Setup a reCAPTCHA Site
To run this project in a production environment, it is necessary to generate your own reCAPTCHA site keys. This can be achieved by creating a new site through the [Google reCAPTCHA console](https://www.google.com/recaptcha/admin/). Choose the reCAPTCHA type as Challenge (v2) and opt for the Invisible reCAPTCHA Badge. Subsequently, include the domain where the implementation will be utilized. A screenshot illustrating the required configuration is attached for your reference.

![reCAPTCHA Setting](/docs/recaptcha-setting.png)

Upon completion of the setup process, you will gain access to the reCAPTCHA keys. Subsequently, please proceed to update the `.env` file, assigning the site key to `RECAPTCHA_PUBLIC` and the secret key to `RECAPTCHA_PRIVATE`.

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
