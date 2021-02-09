# Project structure

.
├── app.py
├── DOCS
│   ├── 00_REQUIREMENTS.md
│   ├── 01_CREATE_PROJECT.md
│   ├── 02_INSTALL_PROJECT_FROM_GITHUB.md
│   ├── 03_INSTALL_DB.md
│   ├── 04_PROJECT_STRUCTURE.md
│   ├── 05_RUN_PROJECT.md
│   ├── 06_REFERENCES.md
│   └── 07_DEPLOY_HEROKU.md
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── Procfile
├── README.md
├── requirements.txt
├── scripts
│   ├── ddl_scripts.sql
│   └── query_scripts.sql
├── tests
│   └── test_base.py
├── todoapp
│   ├── auth_bp.py
│   ├── dao
│   │   ├── base_dao.py
│   │   ├── __init__.py
│   │   ├── rdbms_dao.py
│   │   ├── todo_dao.py
│   │   └── user_dao.py
│   ├── helpers
│   │   ├── messenger.py
│   │   └── validators.py
│   ├── __init__.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       ├── addTodo.js
│   │       ├── getTodos.js
│   │       ├── loadTodos.js
│   │       ├── postTodo.js
│   │       ├── updateTodo.js
│   │       └── validations.js
│   ├── templates
│   │   ├── 404.html
│   │   ├── 405.html
│   │   ├── 500.html
│   │   ├── auth
│   │   │   ├── authBase.html
│   │   │   ├── login.html
│   │   │   └── signup.html
│   │   ├── base.html
│   │   ├── header.html
│   │   ├── macros.html
│   │   ├── todov1
│   │   │   ├── create.html
│   │   │   ├── index.html
│   │   │   └── update.html
│   │   ├── todov2
│   │   │   ├── create.html
│   │   │   ├── index.html
│   │   │   └── update.html
│   │   └── todov3
│   │       └── index.html
│   ├── todov1_bp.py
│   ├── todov2_bp.py
│   └── todov3_bp.py
├── todoapp.db
└── todo_errors.log


14 directories, 55 files