import sqlite3 as driver

from flask import current_app, g
from werkzeug.local import LocalProxy

from  .base_dao import AbstractDAO

logger = LocalProxy( lambda : current_app.logger )

class RdbmsDAO( AbstractDAO ):
    """
        This class extends of AbstractDAO and must implements the inherited and abstract methods, to be usefull for some client.
        This clas implements the methods considering , they will be implemented to work with SQLite3.

        The parameter of the database is passed by environment variable. This need and .env file to get the value of the 
        DATABASE indicating how to get to the database.
    """
    
    @staticmethod
    def get_connection():
        """ The method that returns the connection and the cursor to execute SQL statements.

            Returns
            -------
            connection: A sqlite3 connection object
            cursor: A sqlite3 cursor object.
        """

        if 'connection' not in g:
            g.connection = driver.connect(  current_app.config['DATABASE']  )
            g.connection.row_factory = driver.Row
            g.cursor = g.connection.cursor()
        
        return g.connection, g.cursor

    @staticmethod
    def get_resultset( fetched_data = [] ):
        """ The method received the result of cursor.fetchall() to get a list of dictionaries.
            This method is a helper to retrieved a list of dictionaries to the client who invoke 
            the method execute_query.

            Parameters
            ----------
            fetched_data: list of fetched data.
            A list of fetched data return by teh cursor after execute a SELECT statement

            Return
            ------
            result_set: List of dictionaries
            The list of dictionaries ready to be used by the client who invoke the method execute_query.
        """

        result_set = [ dict( row ) for row in fetched_data ]
        return result_set


    @staticmethod
    def execute_query( sql , values =() ):
        """ Used to execute a Query in the database. Only SELECT 
            statements could be executed with this method

            Parameters
            ----------

            sql: str
            The SELECT statement to execute to get data from a table.

            values: tupple, optional
            The values that could be added to the SELECT statement
        """

        try :
            conn, cursor = RdbmsDAO.get_connection()
            cursor.execute(sql, values )
            item_list = RdbmsDAO.get_resultset( cursor.fetchall() )        
            return item_list
        except driver.Error as error :
            logger.error( f'### Query Error is {error}' )
            raise error
        finally:
            """
            Closing commit connection in teardown method of current app ( RdbmsDAO.close_connection() )
            If you required add something else, remove the pass statement and implemente your required logic
            """
            pass
            

    @staticmethod
    def execute_commit( sql, values ):
        """ Execute an SQL sentence that modifies the records in some table.
        
            Parameters
            ----------

            sql: str
            The SQL sentence to execute. The Sentence could be an
            INSERT, UPDATE or DELETE.

            values: tupple
            The values that could be added to the sql sentence
        """

        try:
            conn, cursor = RdbmsDAO.get_connection()
            cursor.execute(sql, values)
            conn.commit()        
            rows = cursor.rowcount
            id = cursor.lastrowid        
            return rows, id
        except driver.Error as error:
            logger.error( f'### Commit Error is {error}' )
            raise error
        finally:        
            """
            Closing commit connection in teardown method of current app ( RdbmsDAO.close_connection() )
            If you required add something else, remove the pass statement and implemente your required logic
            """
            pass

