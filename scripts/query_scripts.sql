/*
#####################  Queries for user table
*/


-- Count the total of users with the given username
-- if count is 0, the name is available
SELECT COUNT(*) as TOTAL from user WHERE username = ?;

-- Get all fileds of the given username, to compare them if exists
SELECT * FROM user WHERE username = ?

-- Create a new user record in the database
INSERT INTO user (username, password)
                values( ?, ? );


/*
#####################  Queries for todo table
*/

-- Get all todos from the given user
-- only get id, owner id (created_at), title, description, is completed
SELECT  
            t.id as id, 
            t.created_at as created_at,            
            t.title as title, 
            t.description as description, 
            t.is_completed as is_completed
            FROM  user as u,  todo as t
            WHERE u.id = t.created_by
            AND u.id = ? ;

-- Insert new todo
-- send data is owner (created_by), title, description
-- is_completed and created_at are default values
-- is_completed with 0
-- created_at with the current date (CURRENT_TIMESTAMP)
INSERT INTO todo
( created_by, title, description )
values( 4, 'First Todo', 'Do a lot of things' );


-- Get specific todo given the todo id and the owner (created_by)
SELECT * FROM todo WHERE id = ? and created_by = ? ;


-- Delete an specific todo by id and their owner (created_by)
DELETE FROM todo WHERE id = ? AND created_by = ? ;


-- Update an specfic todo by todo id and owner ( created_by )
-- modifiying the title, description, is_completed 
-- and updateing the date modification ( updated_at )
UPDATE todo
SET
    title = ?,
    description = ?,
    is_completed = ?,
    updated_at = datetime('now')
    WHERE id = ? 
    AND created_by = ?;   
