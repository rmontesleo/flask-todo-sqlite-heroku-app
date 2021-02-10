# Flask Todo App with SQLite3 and deployed in Heroku


The objective of this project is show how to connect whith a relational database with a Flask Web Application. The database used is SQLite3. Finally deploy the application in Heroku.

The applications has two modules:

- Authentication module : The functionallity is to execute SigUp and Login.
- TODO module: Some register user will add their todo in cards. The todos can be created, updated, listed or deleted.


Technologies used in project:
- Python 3
- Flask
- SQLite 3
- Jinja templates
- HTML
- CSS


Technologies used for deployment.
- Heroku


The project is a web app, build with Flask, using a SQLite3 database to store the todos and the users.
The application uses concepts of Object Oriented Programming ( abstract classes, static methods, and separate the classes in different files).

Our goal is make an application  less couple with the database.


The section of DOCS contains files with notes of requirements, how to install project, the database, make and run the container and finally deploy on Heroku.

Maybe is not the best used case, but the goals of this project are:

- Develop an application using design patterns.
- Deploy the application on the cloud.


I hope this code could help you in your own project.

Thank you for your attention.

---

## Structure of the project

- **DOCS**: The documentation, to install project, run application, create containers and deploy on Cloud.
- **scripts**: Folder with the sql scripts to create database, and some queries to test application.
- **tests**: Folder with the unit test for the flask application.
- **todoapp**: Folder with the main module. Contains the files .py .html, etc that conform the application.
- **.env**: File with the enviroment variables to run the project. This file is readed by Flask. But never be versioned.
- **.gitignore**: The file with the list of folders and files to be ignore by git when versioning the project.
- **.slugignore**: The file with the list of folders and files to be ignore for deployment on Heroku.
- **LICENSE**: The MIT licence of the project.
- **app**: The python file that uses flask to run the application. This file and the name app.py  are required by gunicorn to start the application on Heroku.
- **Pipfile**: The file used by pipenv to define the main dependencies.
- **Pipfile.lock**: The file with all the required dependencies. This file is used to install depenencies in the project and in the container.
- **Procfile**: This file is used to deploy on Heroku and run the application.
- **todo_errors.log**: Log file to show error or any required log. This file must be ignore by git.
- **todoapp.db**: The SQLite3 database, the database file required for the application. This file never be versioned. It must be created in the development or in the deployment.
