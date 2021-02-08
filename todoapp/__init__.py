"""
    This file define the todoapp folder as a module.
    In the create_app method are created/defined:

    1) The Flask application
    2) The logger of application (enable only when the enviroment variables FLASK_DEBUG is set in 1)
    3) Set the Bootstrap implementation for Flask.
    4) Initialize the database layer executing the function init_dao_app
    5) Subscribe the blueprint for authentication
    6) Subscribe the blueprint for the todo app.
    7) Define a command to execute unit tests.
"""

import os
import unittest
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from logging import FileHandler, WARNING, DEBUG, Formatter

from .dao.base_dao import init_dao_app

from . import auth_bp as auth
from . import todov1_bp as todov1
from . import todov2_bp as todov2
from . import todov3_bp as todov3


def create_app():
    app = Flask( __name__ )

    if app.debug:
        file_handler = FileHandler( 'todo_errors.log' )
        file_handler.setLevel( DEBUG )
        formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter( formatter )
        app.logger.addHandler( file_handler )

    app.config.from_mapping(
        SECRET_KEY = os.environ.get('APP_SECRET'),
        DATABASE= os.environ.get('APP_DATABASE')
    )      

    Bootstrap(app)

    init_dao_app( app )

    app.register_blueprint( auth.bp )
    app.register_blueprint( todov1.bp )
    app.register_blueprint( todov2.bp )
    app.register_blueprint( todov3.bp )


    @app.cli.command()
    def test():
        tests = unittest.TestLoader().discover('tests')
        unittest.TextTestRunner().run(tests)

    return app

