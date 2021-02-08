from .rdbms_dao import RdbmsDAO

class UserDao(RdbmsDAO):
    """ This clas extends from RdbmsDAO, that means, all the logic to connect, disconect or execute 
        sentences in the database are define in the super classes. 
        This class focus only in resolve the CRUD to the table user of the database todoapp.
        Each method only define the requerired sql sentence and invoke the execute_query or execute_commit
        method of the parent class.
        The methods dont handle an exeption if it occours. That responsability will be of the cliente of this class. 
    """

    def count_user_name( self, user_name ):
        """ This method get the user name and count, how many exist in the database.
            THis method is used in the sigup

            Parameters
            ----------
            user_name: str
            The value of the required user name to validate if exist or not in the database        

            Returns
            -------
            total_user: int
            The total user that match with the required value.
        """

        sql = "SELECT COUNT(*) as TOTAL from user WHERE username = ?"
        values = (user_name,)
        user_list = super().execute_query(sql, values)

        return user_list[0]['TOTAL']
    


    def insert_user( self, user_name, password ):
        """ Method to save the user_name and password in the database.

            Parameters
            ----------
            user_name: str
            The user name to be saved in the database.

            password: str
            The password to be saved in the database. Note: The password must be encripted if you required
            The task of encript or decript depends on the client.

            Returns
            -------
            id : int
            The generated id in the table. Otherwise return None.        
        """

        sql = " INSERT INTO user (username, password) values( ?, ? ) "

        values = (user_name, password)        
        rows, id = super().execute_commit(sql, values)

        if rows == 1:
            return id        

        return None

    def find_user(self, user_name ):
        """  Method is for find some user in the database.
             The method is used in the login operation.

             Parameters
             ----------
             user_name: str
             The required value of the user name

             Returns
             -------
             user: dict
             If the user was fouded in the database is return in a dictionary.
             Otherwise the value None is returned.
        """


        sql = " SELECT * FROM user WHERE username = ? "
        values = (user_name, )
        user_list =  super().execute_query(sql, values)

        if len ( user_list ) == 1:
            return user_list[0]
        else:
            return None    