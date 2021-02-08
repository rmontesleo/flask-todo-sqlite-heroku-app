from abc import ABC, abstractmethod
from flask import g


def init_dao_app(app):
    app.teardown_appcontext( AbstractDAO.close_connection )

class AbstractDAO(ABC):
    """
        This abstract class is used like template or interface to define methods.
        The implementation of the abstract methods depends on the required database.
        Only the close_connection method is define in this class.  The rest of methods
        are only declared, but not implemented
    """

    @staticmethod
    def close_connection( e=None ):
        """ The method close the connection and the cursor with the database.
            The connection and the cursor are taken from the g variable of Flask.            
        """
        connection  = g.pop( 'connection', None )
        cursor = g.pop('cursor', None)

        if cursor is not None:
            cursor.close()
            
        if connection is not None:
            connection.close()


    @staticmethod
    @abstractmethod
    def get_connection():
        """
            The implementation of this method depends on the used database
        """
        raise NotImplemented

    @staticmethod
    @abstractmethod
    def execute_query( sql,  values=() ):
        """
            The implementation of this method depends on the used database
        """
        raise NotImplemented

    @staticmethod
    @abstractmethod
    def execute_commit( sql, values ):
        """
            The implementation of this method depends on the used database
        """
        raise NotImplemented