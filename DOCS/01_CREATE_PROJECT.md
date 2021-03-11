# Create the Project

For this project, the main folder will be flask-todo-sqlite-heroku-app
```
mkdir flask-todo-sqlite-heroku-app
```

## The .env file

This file define the variables that required Flask to run the application
This is the structure of this file.  You add your required values.
**This file must be omited in git and Heroku**

The file in in the root of your main project.

To create the file

```
touch .env
```

The content, contain the following variables.

```
FLASK_APP=app.py

# For development the value is 1, for deployment on Heroku the value is 0
FLASK_DEBUG=1

# For development environment, in production you can ommit this variable
FLASK_ENV=development

# The port where Flask run. The default port is 5000, but you define your required port
FLASK_RUN_PORT=5000

# The name of the database. For this project the database is todoapp.db
APP_DATABASE=todoapp.db

# The secret key required for session and tokens. For development you can use any value, but for production use a more complex value
APP_SECRET=supersecret
```

## Create virtual environment
Inside of your main folder, create a virtual environment with pipenv

```
pipenv shell
```

## Install dependencies

You can install all dependencies in one line or one by one.  The main dependencies to install are

- flask: The micro framework to develope the web application in Python.
- flask-wtf: The required library to use forms components in Flask.
- flask-bootstrap4: The library that integrate with Bootstrap with Flask.
- werkzeug: Is a comprehensive WSGI web application library.
- python-dotenv: The dependency to read environment variables and take these values in application.
- gunicorn: Library to deploy the application in Heroku.

```
pipenv install flask flask-wtf python-dotenv flask-bootstrap4 werkzeug gunicorn
```


