# Install the database

The application uses a SQLite3 Database. 

Run from command line the execution of the todo app.

```
cat scripts/ddl_scripts.sql | sqlite3 todoapp.db
```

This process apply when you are creating the database or when you are installed


## The model of the database is the following.

<br/>
<br/>


<img src="images/DataBase_Diagram.JPG"
     alt="Login Page"/>


<br/><br/>

## The DAO pattern

- AbstractDAO: This class is used like an interface, to define a contract with the methods to be implemented.
- RdbmsDAO:  Implements the method. It knows what driver implement, and the database to use.
- UserDao: Implements the method referent with the user.
- TodoDao: Implements the CRUD of the todos.

The following diagram show the inheritance relation between classes.

<br/>
<br/>


<img src="images/TODO_DAO_Diagram_class.jpg"
     alt="DAO Diagram class"/>