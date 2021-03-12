import { isValidBasicTodoForm  } from './validations.js';

/**
 * This function POST a todo and if is successfull, redirects to home in the version 2.
 *  Structure of todo 
 *  title: string
 *  description: string
 * 
 * @param {*} todo 
 */
async function postTodo( todo ){
    try {
        const response = await fetch( '/todov2/save', {
            method: "POST",
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(todo)
        } );
        const status = await response.status;
        const data = await response.json();    

        //console.log(`data is ${data} and status is ${status} `);
        location.href = '/todov2';
    } catch ( error ) {
        //console.error( error );
        $('#todoModal').modal('show')        
    }    

}


const postBtn = document.getElementById('postBtn');

postBtn.addEventListener( 'click', function( event ){
    const controlArray = [
        { id: "title", max: 50,  fieldName: "Title" },
        { id: "description", max: 200,  fieldName: "Description" }
    ]    
    
    if( isValidBasicTodoForm( controlArray ) ){
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const todo = { title, description }
        postTodo( todo );
    }
});