-- todoapp.db

CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE todo (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    created_by INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    is_completed INTEGER NOT NULL CHECK( is_completed IN (0,1) ) DEFAULT 0,
    FOREIGN KEY (created_by) REFERENCES user(id)
);