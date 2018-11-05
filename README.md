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
    ``` 
    create database instaworks_team_db;
     ```
    - create user "shrey" with some password or without.
    ``` 
    create user "Shrey" with password 'somepassword'; 
    ```
    - Grant all privillages to the created user on the created database.
    ```
    GRANT ALL PRIVILEGES ON DATABASE "instaworks_team_db" TO "shrey";
    ```
2. Run install.sh to install all dependencies in a virtual environment, the project will run from the virtual environment.
    ```
    ./install.sh
    ```
    install.sh supports only redhat based linux dist(centos/fedora) and not ubuntu, as the project uses YUM to install pip and virtualenv.

#Run
1. Need to fill the write details in config/system.yaml, like database_ip, database_name. In case of passwords it should be mentioned in config/passwords.yaml. But in ase of production there should not be any password file and all passwords should be taken from systems env variables.
2. Run manage.py deploy, as the project uses alembic for migrations, deploy will run upgrade() and will create tables. No need to run init as version file is already placed. manage.py deploy is enough
    ```
    python manage.py deploy
    ```
3. Manage.py runs the app in the dev mode, for production it will need a web-server(apache/nginx).
    ```
    python manage.py runserver
    ```
    this command will run in the default mode i.e development mode, so it will work on sqlite database. To work with Postgres SQL need to run this production mode, for that we need to set an environment variable 'FLASK_CONFIG', like as follows
    ```
    export FLASK_CONFIG=production_config
    python manage.py runserver
    ```

#Endpoints
1. http://127.0.0.1:5000/api/v2.0/team_members
    - GET: list of team members
        -curl: 
            ```
            curl -X GET http://127.0.0.1:5000/api/v2.0/team_members
            ```
    - POST: Add a new team member, needs to give all properties of a member
        -example json:
            ```
                curl -X POST -H "Content-Type:application/json" http://127.0.0.1:5000/api/v2.0/team_members -d '{"email": "sh.chauhan@gma.commm", "first_name": "Shrey", "last_name": "Chauhan", "phone_number": 332987, "role": "regular"}'
            ```
2. http://127.0.0.1:5000/api/v2.0/team_member/{id}
    - GET: Details of a team member
        ```
        curl -X GET http://127.0.0.1:5000/api/v2.0/team_member/{id}
        ```
    - DELETE: Remove the team member from the list of team members
        ```
        curl -X DELETE http://127.0.0.1:5000/api/v2.0/team_member/{id}
        ```
    - PATCH: Edit the properties of a team member
        example json:
            ```
                curl -X PATCH -H "Content-Type:application/json" http://127.0.0.1:5000/api/v2.0/team_member/5 -d '{"role": "admin"}'
            ```
