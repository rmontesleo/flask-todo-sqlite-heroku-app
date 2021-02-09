from flask import ( 
    flash, current_app
 )
from werkzeug.local import LocalProxy

logger = LocalProxy( lambda : current_app.logger )

def send_flash( message, category='warning', is_logged=False ):    
    """ This method send a flash message and could be log the message.

        Parameters
        ----------
        message: str
        The text message to be display in the Flask flash

        category:string
        The category of the flask, by default warning.

        is_logged:bool
        The flag to write in log, by default is False.
    """

    flash( message, category )

    if is_logged:
        logger.debug( message )


def notify_empty_fields( input_array, form ):
    """ This function send flash if the filed of some form not exists.
        If filed in the array is not present in the form, send a flash

        Parameters
        ----------
        input_array: list
        The list of elements to evaluate. The consumer, 
        must add the required fields to validate.

        form:dict
        The posted form that contains the fields use in the Blueprint.
    """
    
    for input in input_array:
        if not form[ input['name'] ]:
            flash( f'{ input["label"] } is required', 'warning' )


def log_error( message, error ):
    """ Function to log the message error and the error sent by application.

    message: str
    The message text with the description of the error.

    error: obj
    The error, exeption throw by the applcation.
    """

    logger.error( f'Message error is {message}' )
    logger.error( f'Error is {error} ' )


def notify_error( message='Something goes wrong' , error = {} ):
    """ A wrapper function to log the erro and the send a flash

        message:str
        The display text to send in a flash and log
        By default 'Somthing goes wrong', but use a more descriptive message.


        error: dict
        The object error/exeption throw by the application
    """    

    log_error( message, error )
    flash( message, 'error' )
    