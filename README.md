# Flask Todo App with SQLite3 and DAO pattern.


The objective of this project is show how to connect whith a relational database with a Flask Web Application. The database used is SQLite3.

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



The project is divided in  10 parts, in each one we see how to install the database, connect with Python in scripts,  divide the code using functions. Then we group the code in classes using Object Oriented Programming. Finally we apply concepts of abstract classes, static methods, and separate the classes in different files.

Our goal is make a code less couple with the database.

Each Part has a README file with instructions of how to run the code, the specific objective of that part.

The section of DOCS contains files with notes of requirements, how to install project, the database, make and run the container and finally deploy on IBM Cloud with Kubernetes.

Maybe is not the best used case, but the goals of this project are:

- Develop an application using design patterns.
- Run the application with containers.
- Deploy the application on the cloud.


I hope this code could help you in your own project.

Thank you for your attention.

---

## Structure of the project

- **development**: Folder to add env files for create or run containers. This folder must be created, but never be versioned.
- **DOCS**: The documentation, to install project, run application, create containers and deploy on Cloud.
- **scripts**: Folder with the sql scripts to create database, and some queries to test application.
- **tests**: Folder with the unit test for the flask application.
- **todoapp**: Folder with the main module. Contains the files .py .html, etc that conform the application.
- **.dockerignore**: In this file are added, the files, folders or extentions to be ignore when creating the container.
- **.env**: File with the enviroment variables to run the project. This file is readed by Flask. But never be versioned.
- **.gitignore**: The file with the list of folders and files to be ignore by git when versioning the project.
- **Dockerfile**: The file with the instructions of how to build the conatainer.
- **installation_script.sql**: The sql file required to install the database in the container.
- **LICENSE**: The MIT licence of the project.
- **main**: The python file that uses flask to run the application.
- **Pipfile**: The file used by pipenv to define the main dependencies.
- **Pipfile.lock**: The file with all the required dependencies. This file is used to install depenencies in the project and in the container.
- **todo_errors.log**: Log file to show error or any required log. This file must be ignore by git.
- **todoapp.db**: The SQLite3 database, the database file required for the application. This file never be versioned. It must be created in the development or in the deployment.
