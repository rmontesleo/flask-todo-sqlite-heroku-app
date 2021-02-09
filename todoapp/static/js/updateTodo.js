import { isValidBasicTodoForm  } from './validations.js';

/**
 * 
 * @param {*} todo 
 */
function setTodoValues( todo ){
    const{  title, description, 
            created_at, updated_at, is_completed   } = todo;

    document.getElementById('isCompleted').checked = is_completed;
    document.getElementById('title').value = title;
    document.getElementById('description').value = description;
    document.getElementById('createdAt').value = created_at;
    document.getElementById('updatedAt').value = updated_at;
}

/**
 * 
 * @param {*} todoId 
 */
export async function loadTodo( todoId ){    
    try {
        const url = `/todov2/load_by_id/${todoId}`;
        const response = await fetch( url, {
            method: "GET",
            headers:{
                'Content-Type': 'application/json'
            }
        });        
        const todo = await response.json();
        setTodoValues(todo);        
    } catch ( error ) {
        console.error( error )
        $('#loadAlert').modal('show');        
    }
}

/**
 * 
 * @param {*} todoId 
 */
async function deleteTodo( todoId ){
    try {
        const url = `/todov2/delete/${todoId}`;
        const response = await fetch( url, {
            method: "DELETE",
            headers:{
                'Content-Type': 'application/json'
            }
        } );
        const status = await response.status;
        const data = await response.json();
        location.href =  '/todov2';
    } catch ( error ) {
        $('#deleteAlert').modal('show');        
    }
}



/**
 * 
 * @param {*} todo 
 */
async function putTodo( todoId, todo ){
    try {
        const url = `/todov2/update/${todoId}`;
        const response = await fetch( url, {
            method: "PUT",
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(todo)
        } );
        const status = await response.status;
        const data = await response.json();    

        console.log(`data is ${data} and status is ${status}` );
        location.href = '/todov2';
    } catch ( error ) {
        $('#updateAlert').modal('show');        
    }
}



const putBtn = document.getElementById('putBtn');

putBtn.addEventListener( 'click', function( event ){
    const controlArray = [
        { id: "title", max: 50,  fieldName: "Title" },
        { id: "description", max: 200,  fieldName: "Description" }
    ];

    if( isValidBasicTodoForm( controlArray ) ){
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const isCompleted = document.getElementById('isCompleted').checked;
        const todo = { title, description, isCompleted };
        const id = document.getElementById('todoIdHidden').value;

        console.log(`todo to update is `, todo )
        putTodo( id, todo  );
    }
});

const deleteBtn = document.getElementById('deleteBtn');

deleteBtn.addEventListener( 'click', function(event){
    $('#deleteConfirm').modal('show');
});

const deleteOkBtn = document.getElementById('deleteOkBtn');

deleteOkBtn.addEventListener('click', function( event ){
    $('#deleteConfirm').modal('hide');
    const id = document.getElementById('todoIdHidden').value;
    deleteTodo(id);
});