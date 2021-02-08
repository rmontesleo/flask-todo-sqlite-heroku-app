
## Install gunicorn

```
pipenv install gunicorn
```

## Create Procfile
```
touch Procfile
```

## Edit Procfile to indicate the type of application and what file is the app, in this case is main
```
web: gunicorn app:main
```

## Create the requirements text file 
```
pipenv run pip freeze > requirements.txt
```

## setup or verify your git environment 

```
git init
git add .
git commit -m "Initial commit"
```

## Create a .slugignore, and add the files you want to ignore in the deployment
```
touch .slugignore
```

## login with heroku, a web browser will be open
```
heroku login
```

## Create an app with the heroku cli, and see the link to open the application dashboard
```
heroku create
```

## You can rename your app
```
heroku rename <new_amazing_name>
heroku rename flask-todo-sqlite-heroku-app
```
## Deploy the app to heroku, 
```
git push heroku master
```





