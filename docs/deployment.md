## Deploying the Project:
To deploy the project to a production environment, utilize our Docker Compose setup as follows:

### Step 1: Clone the project on server
Begin by cloning the project repository onto your server using the following command:

```bash
git clone https://github.com/udit-001/pizzashop.git
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

#### Step 3.1: Set Django Settings Values
Adjust the values for the following settings in the `.envs/.production/.django` file:

- `ALLOWED_HOSTS` - Specify the domain of the server to make the app accessible. Refer to [this section](https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts) in the Django documentation for further details.
- `SECRET_KEY` - Assign a unique and unpredictable value. Utilize a [Django secret key generator](https://djecrety.ir/) for assistance. The `SECRET_KEY` is crucial for various security purposes in Django, as explained in the [documentation](https://docs.djangoproject.com/en/dev/ref/settings/#secret-key).
- `DEBUG` - Ensure this variable is set to False. Debug mode should never be enabled in a production environment. For further details, refer to [this section](https://docs.djangoproject.com/en/dev/ref/settings/#std-setting-DEBUG) of the Django docs.
- `DATABASE_URL` - If you're using a managed database server in the cloud, you can input the database details in the following format: `postgres://<username>:<password>@<ip_or_host>:5432/<database_name>`.

  For instance, if you're running your application locally, it might resemble: `postgres://postgres:postgres@localhost:5432/pizzitalia`.


### Step 4: Setting up the reCAPTCHA Site
To run this project in a production environment, it is necessary to generate your own reCAPTCHA site keys. This can be achieved by creating a new site through the [Google reCAPTCHA console](https://www.google.com/recaptcha/admin/). Choose the reCAPTCHA type as Challenge (v2) and opt for the Invisible reCAPTCHA Badge. Subsequently, include the domain where the implementation will be utilized. A screenshot illustrating the required configuration is attached for your reference.

![reCAPTCHA Setting](/docs/recaptcha-setting.png)

Upon completion of the setup process, you will gain access to the reCAPTCHA keys. Subsequently, please proceed to update the `.envs/.production/.django` file, assigning the site key to `RECAPTCHA_PUBLIC` and the secret key to `RECAPTCHA_PRIVATE`.


### Step 5: Configuring Email SMTP Server

#### Using SendGrid
To set up the project's SMTP server, SendGrid was selected due to its reliable free tier. For detailed instructions, consult the [SendGrid documentation](https://docs.sendgrid.com/for-developers/sending-email/integrating-with-the-smtp-api) and acquire the API key.

Once obtained, insert the API key value in the `.envs/.production/.django` file under the label `SENDGRID_API`. Additionally, ensure the correct sender address by updating the `DEFAULT_FROM_EMAIL` environment variable.

#### Using Other SMTP Provider
Alternatively, if you prefer to use a different SMTP Provider, simply configure the following environment variables to match your SMTP server settings:

- `EMAIL_HOST`
- `EMAIL_PORT`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `EMAIL_USE_TLS`
- `DEFAULT_FROM_EMAIL`

For more information on [SMTP configurations](https://docs.djangoproject.com/en/dev/topics/email/#smtp-backend), refer to the SMTP section in the Django documentation.

### Step 6: Setting up Google Places Integration
In this project, we employ the Google Places API to offer users an autocomplete feature when inputting address details. To ensure proper functionality in a production environment, it is necessary to generate an API key. Please consult the documentation provided [here](https://developers.google.com/maps/documentation/places/web-service/get-api-key) to obtain the API key. Once acquired, insert the key into the `.envs/.production/.django` file, assigning it to the variable `PLACES_API_KEY`.

### Step 7: Setting up Stripe Integration
To facilitate credit card payments from users, Stripe integration is implemented in this project. To enable this functionality, it is necessary to configure the project with your account's secret key. You can find this key in your Stripe Dashboard. Set the `STRIPE_API_KEY` in the `.envs\.production\.django` file to the corresponding value.

### Step 8: Running the container
Ensure that you are in project's root directory, if not, then navigate to the project's root directory using the terminal. Then run the following command to build and start the application:

   ```
   docker compose up -f production.yaml -d
   ```

After the container completes the build process, your application will be accessible at `http://localhost:8000`.

### Step 9: Setting up the Web Server
To make your application accessible to the public, you'll need to utilize a web server like NGINX or Apache HTTP Server.

If you wish to learn how to proceed with this step, you can refer to [an article](https://idiomaticprogrammers.com/post/django-in-production-part-2/) I've authored detailing the process of exposing your Django application to the internet using NGINX.
