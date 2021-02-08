
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