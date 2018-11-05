# Instaworks

#Getting Started
The project will setup a Rest http api to support team management application as a part of Instawroks assignment.
Project has its logging as well, the logging file gets created in the log folder which is mentioned config/system.yaml file.
``` 
log_folder: &logf
/var/log/instawork_shrey
```


#Prerequisite
Postgres SQL server setup in the local or in the network, allowing app server to access(not needed in case of local). Supports sqlite database as well which requires no setup, and sqlite database gets created in the log folder.

#Setup
1. Enter Postgres SQL server:
    - create database "instaworks_team_db" in database.
    ``` create database instaworks_team_db; ```
    - create user "shrey" with some password or without.
    ```  create user "Shrey" with password 'somepassword'; ```
    - Grant all privillages to the created user on the created database.
    ``` GRANT ALL PRIVILEGES ON DATABASE "instaworks_team_db" TO "shrey"; ```
2. Run install.sh to install all dependencies in a virtual environment, the project will run from the virtual environment.
    ``` ./install.sh ```

#Run
1. Need to fill the write details in config/system.yaml, like database_ip, database_name. In case of passwords it should be mentioned in config/passwords.yaml.
But in case of production there should not be any password file and all passwords should be taken from systems env variables.
1. Manage.py runs the app in the dev mode for production it will need webserver(apache/nginx).
    ``` python manage.py runserver ```
    this command will run in the default mode i.e development mode, so it will work on sqlite database. To work with Postgres SQL need to run this production mode, for that we need to set an environment variable 'FLASK_CONFIG', like as follows
    ``` export FLASK_CONFIG=production_config ```
    ``` python manage.py runserver ```     