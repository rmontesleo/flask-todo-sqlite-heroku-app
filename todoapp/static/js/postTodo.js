import { isValidBasicTodoForm  } from './validations.js';

/**
 * 
 * @param {*} todo 
 */
async function postTodo( todo ){
    try {
        const response = await fetch( '/todov3/save', {
            method: "POST",
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(todo)
        });
        const status = await response.status;
        const data = await response.json();    

        console.log(`data is ${data} and status is ${status} `);
        
        $('#addTodoWindowModal').modal('hide');
        
        location.href =  '/todov3';
        
    } catch ( error ) {
        $('#addTodoWindowModal').modal('hide');
        console.error( error );
        $('#saveAlert').modal('show')
        console.log('bye bye')
    }
}



const postBtn = document.getElementById('saveAddTodoWindowModalBtn');

postBtn.addEventListener( 'click', function( event ){
    
    const addFieldsArray = [
        { id: "addTodoTitle", max: 50,  fieldName: "Title" },
        { id: "addTodoDescription", max: 200,  fieldName: "Description" }
    ]

    if( isValidBasicTodoForm( addFieldsArray ) ){        
        const title = document.getElementById('addTodoTitle').value;
        const description = document.getElementById('addTodoDescription').value;
        const todo = { title, description }
        postTodo( todo );
    }
});



/**
 * 
 * @param {*} todo 
 */
async function putTodo( todo ){
    try {
        const todo_url = `/todov3/update/${todo.id}`;

        const response = await fetch( todo_url, {
            method: "PUT",
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(todo)
        } );
        const status = await response.status;
        const data = await response.json();    

        $('#updateTodoWindowModal').modal('hide');
        console.log(`data is ${data} and status is ${status}` );
        location.href = '/todov3';
    } catch ( error ) {
        $('#updateTodoWindowModal').modal('hide');
        $('#updateAlert').modal('show');        
    }
}



const putBtn = document.getElementById('updateUpdateTodoWindowModalBtn');

putBtn.addEventListener( 'click', function( event ){  
    
    const updateFieldsArray = [
        { id: "updateTodoTitle", max: 50,  fieldName: "Title" },
        { id: "updateTodoDescription", max: 200,  fieldName: "Description" }
    ];    

    if( isValidBasicTodoForm( updateFieldsArray ) ){
        const title = document.getElementById('updateTodoTitle').value;
        const description = document.getElementById('updateTodoDescription').value;
        const isCompleted = document.getElementById('updateTodoisCompleted').checked;
        const id = document.getElementById('updateTodoTodoId').value;
        const todo = { title, description, isCompleted, id };

        console.log(`todo to update is `, todo )
        putTodo( todo );
    }
});