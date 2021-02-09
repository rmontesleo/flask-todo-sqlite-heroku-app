# Running your Project
---

Before run your application, verify the variables of the .env file are loaded. 


```
echo $FLASK_APP
echo $FLASK_DEBUG
echo $FLASK_ENV
echo $FLASK_RUN_PORT
echo $APP_DATABASE
echo $APP_SECRET
```

You must see the values save in your .env file.


When you see values in console,  run the command to start application
```
flask run
```

You must see in console something like that

```
* Serving Flask app "main.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 191-006-456

```