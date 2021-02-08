""" 
    This main file is executed by flask to run the application.
    Create an instance of the applictaion, and then define the 
    route method for the root page.
"""

from flask import ( redirect, url_for )
from todoapp import create_app

app = create_app()

home_prefix = 'todov1'

@app.route('/')
def go_home():
    """ When root path is requested, 
        this function redirects to the index of todo app
    """
    return redirect( url_for( f'{home_prefix}.index' ) )
