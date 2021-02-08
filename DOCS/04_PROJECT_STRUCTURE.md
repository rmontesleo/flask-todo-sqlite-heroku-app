
# Project Structure


### Note: Maybe the preview is not the best option, see in the raw text


.
├── development
│   ├── build_env
│   └── dev_env
├── Dockerfile
├── DOCS
│   ├── 00_REQUIREMENTS.md
│   ├── 01_INSTALL_PROJECT.md
│   ├── 02_INSTALL_DB.md
│   ├── 03_RUN_PROJECT.md
│   ├── 04_BUILD_CONTAINER.md
│   ├── 05_DEPLOY_IBM.md
│   ├── 06_PROJECT_STRUCTURE.md
│   └── 07_REFERENCES.md
├── installation_script.sql
├── LICENSE
├── main.py
├── Pipfile
├── Pipfile.lock
├── REAME.md
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
│   │   └── css
│   │       └── styles.css
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
│   │   └── todov1
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── todov1_bp.py
├── todoapp.db
└── todo_errors.log


12 directories, 45 files
