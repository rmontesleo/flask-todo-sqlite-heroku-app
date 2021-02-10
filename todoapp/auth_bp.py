""" This python file defines the logic for login, logout, signup and the decorators to evaluate 
    if some request is authenticated.
"""

import functools

from flask import (
    Blueprint, request, render_template, g,
    redirect, session, url_for, current_app
)

from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.local import LocalProxy

from todoapp.helpers.messenger import send_flash, notify_empty_fields, notify_error
from todoapp.helpers.validators import validate_not_empty_values
from todoapp.dao.user_dao import UserDao as UserDB

home_prefix = 'todov1'
prefix = 'auth'

bp = Blueprint( prefix, __name__, url_prefix= f'/{prefix}' )

logger = LocalProxy( lambda : current_app.logger )


@bp.route('/sigup', methods=['GET', 'POST' ] )
def sigup():
    if request.method == 'GET':
        return render_template( f'/{prefix}/signup.html' )
   
    form = request.form
    is_valid_form = validate_not_empty_values( ['username', 'password'] ,form )
    
    if is_valid_form:
        user_name = form['username']
        password =  form['password']

        userdb = UserDB()
        count = 0

        try:
            count = userdb.count_user_name( user_name )
        except Exception as error:
            message ='User can not be registered, please try later'
            notify_error( message, error )
            return render_template( f'/{prefix}/signup.html' )
        

        if count == 0:
            try:
                id = userdb.insert_user( user_name, generate_password_hash(password) )                
                return redirect( url_for( f'{prefix}.login') )
            except Exception as error:
                message ='User can not be registered, please try later'
                notify_error( message, error )
                return render_template( f'/{prefix}/signup.html' )                
        else:
            send_flash( f'User {user_name} is already registered' )
            return render_template( f'/{prefix}/signup.html' )
    else:        
        input_array =[ 
            { "name":"username", "label": "Username"  }, 
            { "name":"password", "label": "Password"  },
        ]
        notify_empty_fields( input_array , form )
        return render_template( f'/{prefix}/signup.html' )
        


@bp.route('/login', methods=['GET', 'POST' ] )
def login():
    if request.method == 'GET':
        return render_template( f'/{prefix}/login.html')

    form = request.form
    
    is_valid_form = validate_not_empty_values( ['username', 'password'] ,form )

    if is_valid_form:
        user_name = form['username']
        password = form['password']

        userdb = UserDB()
        try:            
            user = userdb.find_user( user_name )

            if user and check_password_hash( user['password'], password ) :            
                session.clear()
                session['user_id'] = user['id']
                session['user_name'] = user_name
                return redirect( url_for( f'{home_prefix}.index' ) )
            else:
                send_flash('Invalid credentials')
                return render_template( f'/{prefix}/login.html')

        except Exception as error:            
            messae = 'Login can not be executed, please try later', 'error'
            notify_error( message, error )
            return render_template( f'/{prefix}/login.html')
    else:
        input_array =[ 
            { "name":"username", "label": "Username"  }, 
            { "name":"password", "label": "Password"  },
        ]        
        notify_empty_fields( input_array, form )
        return render_template( f'/{prefix}/login.html')



@bp.before_app_request
def load_logged_user_id():
    user_id = session.get('user_id')
    user_name = session.get('user_name')

    if user_id is None or user_name is None:
        g.logged_user = None
    else:
        #go for token or something else
        g.logged_user= {
            "id" : user_id,
            "token" : "some_token..",
            "user_name": user_name
        }   


def login_required(view):
    """ Decorator to verified logged user """
    
    @functools.wraps(view)
    def wrapped_view( **kwargs ):
        if g.logged_user is None:
            return redirect( url_for( f'{prefix}.login') )
        
        return view(**kwargs)

    return wrapped_view    

@bp.route('/logout')
def logout():
    session.clear()
    return redirect( url_for( f'{prefix}.login') )