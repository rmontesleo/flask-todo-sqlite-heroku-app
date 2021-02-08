from .rdbms_dao import RdbmsDAO

class TodoDAO(RdbmsDAO):
    """ This clas extends from RdbmsDAO, that means, all the logic to connect, disconect or execute 
        sentences in the database are define in the super classes. 
        This class focus only in resolve the CRUD to the table todo of the database todoapp.
        Each method only define the requerired sql sentence and invoke the execute_query or execute_commit
        method of the parent class.
        The methods dont handle an exeption if it occours. That responsability will be of the cliente of this class. 
    """

    @staticmethod
    def build_values( todo = {} ):
        """ This method helps to insert and update todo methods to get the data in the todo dictionary.
            It helps and avoid an exeption for any key not included in the dictionary.

            Parameters
            ----------
            todo: dict
            The dictionary with the data to be updated or inserted in the table.

            Returns
            -------

            title: str
            The value of the title in the todo table

            description: str
            The value of the description in the todo table

            is_completed: int
            The value of the flag that indicate the todo is completed (1) or not (0)
        """
        
        if 'created_by' not in todo:
            raise Exception

        created_by = todo['created_by']

        title = ''
        if 'title' in todo :  title = todo['title']

        description = ''
        if 'description' in todo : description = todo['description']

        is_completed = 0
        if 'is_completed' in todo: is_completed = todo['is_completed']

        return created_by, title, description, is_completed


    def select_todos_by_user(self, user_id ):
        """ This method get all the records of the todo table by some user. 

            Parameters
            ----------
            user_id: int
            The value of user id to search in the database to fetch the requierd records.

            Returns
            -------
            todo_list: list of dict
            The method returns a list of dictionary with the values of the records of the todo table
            Otherwise returns an empty list
        """

        sql = """
            SELECT  
            t.id as id, 
            t.created_at as created_at,            
            t.title as title, 
            t.description as description, 
            t.is_completed as is_completed
            FROM  user as u,  todo as t
            WHERE u.id = t.created_by
            AND u.id = ?
        """
        values = (user_id,)
        todo_list = super().execute_query(sql, values )
        return todo_list
        

    def select_todos_by_status( self, user_id, is_completed= 0 ):
        sql = """
            SELECT  
            t.id as id,             
            t.title as title, 
            t.description as description
            FROM  user as u,  todo as t
            WHERE u.id = t.created_by            
            AND   u.id = ?
            AND t.is_completed = ?
        """
        values = (user_id, is_completed )
        todo_list = super().execute_query(sql, values )
        return todo_list

    
    
    def insert_todo( self, todo  ):    
        """ This method insert a record of the todo table. The method receive the required data in a dictionary

            Parameters
            ----------            
            todo: dict
            The dictionary with the data to be inserted in the todo table. The required fields are
            title (str), description(str) and is_completed(int with the values 1 or 0 )

            Returns
            -------

            response: bool
            The response if was saved or not in the database
        """

        sql = """
            INSERT INTO todo
                ( created_by, title, description )
                values( ?, ?, ? )
            """

        created_by, title, description, is_completed = TodoDAO.build_values( todo )
        values = ( created_by, title, description )    
        rows, id = super().execute_commit( sql, values )

        if rows == 1:
            todo['id'] = id
            return True

        return False

    def select_by_id( self, user_id, todo_id ):
        """ This method select a record of the todo table. The method receive the id of the row in the todo table
            and the user owner of this record.

            Parameters
            ----------
            user_id: int
            The id of the user owner of this todo.

            todo_id: int
            The id of the record in todo table to be fetch

            Returns
            -------

            todo: dict
            The required record of  todo talbe in a dictionary. If the query matches returns a dictionary with
            the required data otherwise return None.
        """

        sql = 'SELECT * FROM todo WHERE id = ? and created_by = ?'
        values = ( todo_id,  user_id )
        todo_list = super().execute_query(sql, values)

        if len( todo_list ) == 1:
            return todo_list[0]
        else:
            return None


    def delete_todo( self, todo_id, user_id ):
        """ This method delete a record of the todo table. The method receive the id of the row to be deleted
            and the owner of this record. If two value match, the record is deleted.

            Parameters
            ----------
            id: int
            The id of the record in todo table to be deleted

            Returns
            -------

            deleted_rows: bool
            True if record was deleted othewise return False
        """

        sql = 'DELETE FROM todo WHERE id = ? AND created_by = ?'
        values = ( todo_id, user_id )
        deleted_rows, id = super().execute_commit( sql, values )

        if deleted_rows == 1:
            return True

        return False


    def update_todo( self, id, todo ):
        """ This method update a record of the todo table. The method receive the id of the row and the 
            data to be modify in a dictionary.

            Parameters
            ----------
            id: int
            The id of the record in todo table to be updated

            todo: dict
            The dictionary with the data to be updated in the record.

            Returns
            -------

            updated_rows: bool
            True if record was updated othewise return False
        """

        sql = """
            UPDATE todo
            SET
                title = ?,
                description = ?,
                is_completed = ?,
                updated_at = datetime('now')
                WHERE id = ? 
                AND created_by = ?   
            """

        created_by, title, description, is_completed = TodoDAO.build_values( todo )
        values = ( title, description, is_completed, id, created_by )
        updated_rows, id = super().execute_commit( sql, values )

        if updated_rows == 1:
            return True 

        return False 
