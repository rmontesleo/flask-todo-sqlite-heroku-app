from flask import (
    Blueprint, request, url_for, g,
    redirect,render_template,abort, current_app
)
from werkzeug.local import LocalProxy

from todoapp.auth_bp import login_required
from todoapp.helpers.validators import (  validate_not_empty_values )
from todoapp.helpers.messenger import ( send_flash, notify_empty_fields, notify_error )
from todoapp.dao.todo_dao import TodoDAO as TodoDB

prefix = 'todov1'
bp  = Blueprint( prefix, __name__, url_prefix= f'/{prefix}' )

logger = LocalProxy( lambda : current_app.logger )


@bp.errorhandler(404)
def page_not_found(error):    
    context ={
        "error_message": error
    }
    return render_template('404.html', **context ), 404


@bp.errorhandler(500)
def handle_app_error(error):
    context ={
        "error_message": error
    }
    return render_template('500.html', **context ), 500


@bp.route('/')
@login_required
def index():
    try:
        user_id = g.logged_user['id']
        user_name = g.logged_user['user_name']
        tododb = TodoDB()
        todo_list = tododb.select_todos_by_user( user_id )

        context = {
            "user_name": user_name,
            "todo_list": todo_list,
            "update_endpoint" : f'{prefix}.update',
            "add_endpoint" :  url_for(f'{prefix}.add')
        }
                
        return render_template( f'/{prefix}/index.html', **context )

    except Exception as error:
        message  = 'Todos coud not be loaded'
        notify_error( message, error )
        abort( 500, message  )
    


@bp.route('/add', methods=['GET', 'POST']  )
@login_required
def add():

    if request.method == 'GET':
        return render_template( f'/{prefix}/create.html')

    form = request.form
    is_valid_form = validate_not_empty_values( ['title', 'description'], form )
    
    if is_valid_form:
        try:

            tododb = TodoDB()
            todo = {
                "created_by" : g.logged_user['id'],
                "title": form['title'],
                "description" : form['description']
            }
                        
            new_todo = tododb.insert_todo( todo )
            send_flash( 'TODO was successfully created', 'success', True )
            return redirect(  url_for( f'{prefix}.index') )
        except Exception as error:
            message = 'Todo could not be save..'
            notify_error( message , error )
            abort( 500, message )        
    else:
        input_array =[ 
            { "name":"title", "label": "Title"  }, 
            { "name":"description", "label": "Description"  },
        ]        
        notify_empty_fields( input_array, form )
        return render_template( f'/{prefix}/create.html')


def get_todo_by_id( user_id, id ):
    todo = None
    try:
        tododb = TodoDB()        
        todo = tododb.select_by_id( user_id, id )
        return todo    
    except Exception as error:
        message = f'Something wrong quering id {id}'
        notify_error( message , error )
        abort( 500, message )


@bp.route('/update/<int:id>', methods=['GET', 'POST'] )
@login_required
def update(id):
    user_id = g.logged_user['id']
    todo = get_todo_by_id( user_id, id )

    if todo is None:
        send_flash( f'Todo with id {id} not found' )
        abort( 404, f'Todo with id {id} not found' )

    is_completed = bool( todo['is_completed'] )
    todo['is_completed'] = is_completed
    
    context = {
        "todo": todo,
        "delete_endpoint": f'{prefix}.delete'
    }

    if request.method == 'GET':        
        return render_template( f'{prefix}/update.html', **context )
    
    try:
        form = request.form
        is_valid = validate_not_empty_values( ['title', 'description'], form )

        if is_valid:

            completed_value = 0
            if  'isCompleted' in form :
                completed_value = 1

            tododb = TodoDB()                
            todo = {
                "created_by" : g.logged_user['id'],
                "title": form['title'],
                "description" : form['description'],
                "is_completed" : completed_value
            }

            is_updated  = tododb.update_todo( id, todo )
            send_flash( 'TODO was updated', 'success' )

            return redirect(  url_for( f'{prefix}.index') )
        else: 
            input_array =[ 
                { "name":"title", "label": "Title"  }, 
                { "name":"description", "label": "Description"  },
            ]        
            notify_empty_fields( input_array, form )
            return render_template( f'/{prefix}/update.html', **context )
    except Exception as error:
        message = f'Something wrong updating todo with id {id}'
        notify_error( message, error )
        abort( 500, message )


@bp.route('/delete/<int:id>', methods=['POST'] )
@login_required
def delete(id):
    try:        
        tododb = TodoDB()
        user_id = g.logged_user['id']
        was_deleted = tododb.delete_todo( id, user_id )

        send_flash( 'TODO was deleted', 'success' )
        return redirect( url_for( f'{prefix}.index') )
    except Exception as error:
        message = f'Can not be deleted todo with id {id}'
        notify_error( message, error )
        abort( 500, message )