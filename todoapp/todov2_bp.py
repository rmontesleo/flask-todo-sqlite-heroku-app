from flask import (
    Blueprint, request, url_for, g, 
    redirect, render_template, abort, current_app, jsonify
)
from werkzeug.local import LocalProxy

from todoapp.auth_bp import login_required
from todoapp.helpers.validators import (  validate_not_empty_values )
from todoapp.helpers.messenger import ( send_flash, notify_empty_fields, log_error )
from todoapp.dao.todo_dao import TodoDAO as TodoDB

prefix = 'todov2'
bp  = Blueprint( prefix, __name__, url_prefix= f'/{prefix}' )

logger = LocalProxy( lambda : current_app.logger )

@bp.route('/', methods=['GET'] )
@login_required
def index():
    user_name = g.logged_user['user_name']    
    context = {
        "user_name": user_name,
        "add_endpoint": url_for( f'{prefix}.save_todo' )
    }    
    return render_template( f'/{prefix}/index.html', **context )


@bp.route('/load', methods=['GET'] )
@login_required
def load_todos():
    try:
        user_id = g.logged_user['id']        
        status = request.args.get('is_completed')

        is_completed = 0
        if status == 'true':
            is_completed = 1

        tododb = TodoDB()
        todo_list = tododb.select_todos_by_status( user_id, is_completed )
        
        return jsonify( todo_list )
    except Exception as error:
        message  = 'Todos coud not be loaded'
        log_error( message, error )               
        abort( 500, message )   


@bp.route('/save' , methods=[ 'GET','POST'] )
@login_required
def save_todo():
    if request.method == 'GET':
        return render_template( f'/{prefix}/create.html' )

    field_array = ['title', 'description']
    body = request.json

    if validate_not_empty_values( field_array, body ):
        try:            
            tododb = TodoDB()
            todo = {
                "created_by" : g.logged_user['id'],
                "title": body['title'],
                "description" : body['description']
            }           

            is_saved = tododb.insert_todo( todo )
            return jsonify({ "todo": todo, "isSaved": is_saved  }),201
        except Exception as error:
            message  = 'Todos coud not be loaded'
            log_error( message, error )
            abort( 500, message )
            
    else:
        abort( 400, f'Some fields are missing' )


def get_todo_by_id( id ):    
    todo = None
    try:
        user_id = g.logged_user['id']        
        tododb = TodoDB()
        todo = tododb.select_by_id( user_id, id )
        return todo    
    except Exception as error:
        message = f'Something wrong quering id {id}'
        log_error( message , error )
        abort( 500, message )


@bp.route('/load_by_id/<int:id>', methods=['GET'] )
@login_required
def load_todo(id):
    todo = get_todo_by_id( id )
    
    if todo is None:
        send_flash( f'Todo with id {id} not found' )
        abort( 404, f'Todo with id {id} not found' )

    is_completed = todo['is_completed']
    todo['is_completed'] = bool(is_completed)

    return jsonify( todo )



@bp.route('/update/<int:id>', methods=[ 'GET','PUT'] )
@login_required
def update_todo( id ):
    if request.method == 'GET':
        context = {
            "todo_id": id
        }    
        return render_template( f'/{prefix}/update.html', **context )


    try:
        field_array = [ 'title', 'description' ]
        body = request.json
        is_valid = validate_not_empty_values( field_array, body )
        is_completed = int( body['isCompleted'] )

        if is_valid:
            tododb = TodoDB()
            todo = {
                "created_by" : g.logged_user['id'],
                "title": body['title'],
                "description" : body['description'],
                "is_completed" : is_completed
            }
            is_updated  = tododb.update_todo( id, todo )

            return jsonify( { "isUpdated": is_updated  } )            
        else:             
            abort(400, 'some fields are missing')
    except Exception as error:
        message = f'Something wrong updating todo with id {id}'
        log_error( message, error )
        abort( 500, message )


@bp.route('/delete/<int:id>', methods=['DELETE'] )
@login_required
def delete(id):
    try:
        tododb = TodoDB()
        user_id = g.logged_user['id']
        is_deleted = tododb.delete_todo( id, user_id )        
        return jsonify( { "isDeleted": is_deleted } )
    except Exception as error:       
        message = f'Can not be deleted todo with id {id}'
        log_error( message, error )
        abort( 500, message )        