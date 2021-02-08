from flask import ( 
    flash, current_app
 )
from werkzeug.local import LocalProxy

logger = LocalProxy( lambda : current_app.logger )

def send_flash( message, category='warning', is_logged=False ):    
    """

    """

    flash( message, category )

    if is_logged:
        logger.debug( message )


def notify_empty_fields( input_array, form ):
    """

    """
    
    for input in input_array:
        if not form[ input['name'] ]:
            flash( f'{ input["label"] } is required', 'warning' )


def log_error( message, error ):
    """

    """
    logger.error( f'Message error is {message}' )
    logger.error( f'Error is {error} ' )

def notify_error( message='Something goes wrong' , error = {} ):
    """

    """    
    log_error( message, error )
    flash( message, 'error' )