#!/usr/bin/env python
import os
activate_this = './venv/bin/activate_this.py'
activate_this = os.path.join(os.path.dirname(__file__), activate_this)
execfile(activate_this, dict(__file__=activate_this))

from common import configuration
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
import app
from database import db
# from database.events import Event, LoggerSourceEnum, EventLevelEnum
# from database.scraps import ScrapMessage
from database.types import GUID, INET
# from database.pools import Pool, PoolTypeEnum
# from database.roles import Role
from database.team_members import TeamMember, TeamMemberEnum
# from database.analytics import InstanceState, UserState
# from database.instances import Instance, InstanceTypeEnum, OpenstackProject
# from database.connections import Connection, ProtocolTypeEnum, ConnectionEvent, ConnEventTypeEnum, ConnectionToken
# from background_tasks import sync_openstack_db, collect_db_history, purge_old_data, pool_maintenance
import sys

APP = app.create_and_initialize_app(os.getenv('FLASK_CONFIG') or 'default_config')
MANAGER = Manager(APP)

def add_context_to_shell(flaskapp, manager):
    def make_shell_context():
        if 'production' in configuration.config_name: print "App shell access is forbidden in production!\nExiting!"; sys.exit(1)
        return dict(app=flaskapp, db=db, mainapp=app, configuration=configuration,\
                    TeamMember=TeamMember, TeamMemberEnum=TeamMemberEnum, GUID=GUID, INET=INET,\
                    )
    manager.add_command("shell", Shell(make_context=make_shell_context))
add_context_to_shell(APP, MANAGER)

MIGRATE = Migrate(APP, db)
MANAGER.add_command("db", MigrateCommand)

@MANAGER.command
def profile(length=25, dir_profile=None, host='127.0.0.1', port=5000):
    """Start the application under the code profiler"""
    from werkzeug.contrib.profiler import ProfilerMiddleware
    APP.wsgi_app = ProfilerMiddleware(APP.wsgi_app, restrictions=[length],
                                      profile_dir=dir_profile)
    APP.run(host=host, port=port)

@MANAGER.command
def deploy():
    """Run deployment tasks."""
    from flask_migrate import upgrade
    #migrate database to latest revision
    upgrade()
    #create initial roles
    # Role.insert_initial_permissions_roles()
    #create sample users
    # User.create_sample_users()


if __name__ == "__main__":
    MANAGER.run()
