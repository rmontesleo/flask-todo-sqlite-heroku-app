/**
 * This function build the HTML required to show a todo Card
 * Return a String with the html card to display. * 
 * @param {*} param0: A todo object. This object is deconstructed 
 *      id: integer
 *      title: string
 *      description: string
 */
function buildCard( { id, title, description} = {} ){
    
    const todo_url = `/todov2/update/${id}`;

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
                        <button type="button" onclick="location.href='${todo_url}'" class="btn btn-sm btn-outline-secondary">Edit</button>
                    </div>                    
                </div>
            </div>
        </div>
    </div> `;

    return card;
    
}

/**
 * This function received an array of todos, each todo is map to an HTML card structure.
 * Then the array of stings ins join an injected in the div container.
 * @param {*} todoArray 
 * todoArray: array of todos
 */
function buildRowCards( todoArray ){
    const todoMap = todoArray.map( todo =>{
        return buildCard( todo );
    });
    const rowContainer = document.getElementById('rowContainer');
    rowContainer.innerHTML = todoMap.join('');
}


/**
 * This function load the user's todo by status
 * true by completd
 * false by pending.
 * @param {*} todoStatus 
 */
async function loadTodos( todoStatus=false ) {    
    try {
        url = `/todov2/load?is_completed=${todoStatus}`;
        const response = await fetch( url );
        const data =  await response.json();
        
        //console.table(data);

        buildRowCards( data );
    } catch (error) {
        console.error(`error was ${error}`)
    }
}


// Get swith button in the DOM
const switchBtn = document.getElementById('switchBtn');


/**
 * Set the onclick event to switchBtn to load completed or pending todos
 */
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


/**
 * By initial load, fetch all pending Todos
 */
loadTodos( false );
