
/**
 * 
 * @param {*} todo 
 */
function setTodoValues( todo ){
    const{  title, description, 
            created_at, updated_at, is_completed, id  } = todo;

    document.getElementById('updateTodoisCompleted').checked = is_completed;
    document.getElementById('updateTodoTitle').value = title;
    document.getElementById('updateTodoDescription').value = description;
    document.getElementById('updateTodoCreatedAt').value = created_at;
    document.getElementById('updateTodoUpdatedAt').value = updated_at;
    document.getElementById('updateTodoTodoId').value = id;
}


async function loadTodo(todoId){    
    try {
        const todo_url =  `/todov3/load_by_id/${todoId}`;
        const response = await fetch( todo_url, {
            method: "GET",
            headers:{
                'Content-Type': 'application/json'
            }
        });        
        const todo = await response.json();
        setTodoValues(todo);
        $('#updateTodoWindowModal').modal('show');
    } catch ( error ) {        
        $('#getAlert').modal('show');        
    }
}


function showUpdateModal(todoId){
    loadTodo(todoId);
}


async function deleteTodo(id){
    try {
        const todo_url =  `/todov3/delete/${id}`;
        const response = await fetch( todo_url, {
            method: "DELETE",
            headers:{
                'Content-Type': 'application/json'
            }
        } );
        const status = await response.status;
        const data = await response.json();
        location.href = '/todov3/';
    } catch ( error ) {
        $('#deleteAlert').modal('show');
    }
}


function showDeleteConfirm( todoId ){   
    console.log( `todoId is ${todoId}` );
    
    $('#deleteConfirm').modal('show');    

    const deleteOkBtn = document.getElementById('deleteOkBtn');

    deleteOkBtn.onclick = function( event ){        
        $('#deleteConfirm').modal('hide');
        console.log( `delte todo with id ${todoId}` );
        deleteTodo(todoId);
    };
}


function buildCard( { id, title, description} = {} ){
    
    const card = `<div class="col-md-4">
        <div class="card mb-4 shadow-sm">
            <svg class="bd-placeholder-img card-img-top" width="100%" height="225"
                xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false"
                role="img" aria-label="Placeholder: Thumbnail">
                <title>Placeholder</title>
                <rect width="100%" height="100%" fill="#55595c" />
                <text x="50%" y="50%" fill="#eceeef" dy=".3em">${title}</text>
            </svg>
            <div class="card-body">
                <p class="card-text">${description}</p>
                <div class="d-flex justify-content-between align-items-center">
                    <div class="btn-group">                        
                        <button type="button" id="updateBtn${id}" onclick="showUpdateModal(${id})" class="btn btn-sm btn-outline-secondary">Edit</button>
                        <button type="button" id="deleteBtn${id}" onclick="showDeleteConfirm(${id})" class="btn btn-sm btn-outline-danger">Delete</button>
                    </div>                    
                </div>
            </div>
        </div>
    </div> `;

    return card;
    
}

function buildRowCards( todoArray ){
    const todoMap = todoArray.map( todo=>{
        return buildCard( todo );
    });

    const rowContainer = document.getElementById('rowContainer');
    rowContainer.innerHTML = todoMap.join('');
}



async function loadTodos( todoStatus=0 ) {    
    try {
        url = `/todov3/load?is_completed=${todoStatus}`;
        const response = await fetch( url );
        const data =  await response.json();
        
        console.table(data);

        buildRowCards( data );
    } catch (error) {
        console.error(`error was ${error}`)
        $('#loadAlert').modal('show');
    }
}



const switchBtn = document.getElementById('switchBtn');

switchBtn.addEventListener('click', function( event ){
    const initialClass = 'btn btn-success my-2';
    const switchClass  = 'btn btn-warning my-2';

    const currentClass =  this.className;

    if( currentClass == initialClass ){
        this.className = switchClass;
        this.innerText = "Show Pending TODOS";
        loadTodos( true );
    }else {
        this.className = initialClass;
        this.innerText = "Show Completed TODOS";
        loadTodos( false );
    }
});



function cleanGroupDiv( input ){
    const divControl = input.parentElement;
    divControl.className = 'form-group';
}

const addTodoBtn = document.getElementById('addTodoBtn');

addTodoBtn.addEventListener('click', function( event ){

    const title = document.getElementById('addTodoTitle');
    title.value = '';

    const description = document.getElementById('addTodoDescription');
    description.value = '';

    cleanGroupDiv(title)
    cleanGroupDiv(description);
    
    $('#addTodoWindowModal').modal('show');
    
});



loadTodos( false );