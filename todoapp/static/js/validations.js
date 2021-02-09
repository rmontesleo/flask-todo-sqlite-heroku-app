/**
 * Validate some field is not null, undefined or empty string
 * Returns true if accomplish all conditions, otherwise return false.
 * @param {*} fieldValue 
 */
export function isNotEmpty( fieldValue ){
    let isValid = false;
    
    if ( fieldValue != null && fieldValue != undefined && fieldValue.trim() != ''  ){
        isValid = true;
    }

    return isValid;
}

/**
 * This function validate the max length of some value.
 * @param {*} fieldValue  : The value to evaluate (String)
 * @param {*} max : The max length to evaluate ( Integer)
 */
export function isValidMaxLength( fieldValue, max ){
    let isValid = false;

    if( isNotEmpty(fieldValue) &&  fieldValue.length <= max ){
        isValid = true;
    }

    return isValid;
}

/**
 * 
 * @param {*} input 
 * @param {*} message 
 */
export function showErrorMsg( input, message ){
    console.log( message );

    const divControl = input.parentElement;
    divControl.className = 'form-group error';
    const small = divControl.querySelector('small');
    small.innerText = message;
}

/**
 * 
 * @param {*} input 
 */
export function showSuccess( input ){
    const divControl = input.parentElement;
    divControl.className = 'form-group success';
}



/**
 * 
 * @param {*} controlArray 
 */
export function isValidBasicTodoForm( controlArray ){
    
    let isValid = true;   

    controlArray.forEach( current => {
        const { id, max, fieldName } = current;
        const input = document.getElementById( id );
        const fieldValue = input.value;
          
        if ( isNotEmpty( fieldValue ) ){
             if ( isValidMaxLength( fieldValue, max ) ){
                 showSuccess( input )
             }else{
                showErrorMsg( input, ` The max lengh for ${fieldName} is ${max} characters` );
                isValid = false; 
             }
        }else {
            showErrorMsg( input, `${fieldName} must have content` );
            isValid = false;
        }        
    });

    return isValid;
}

