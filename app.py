from flask import Flask, request, g, jsonify, abort
# from flask_rbac import RBAC

from database import db
from schemas import ma

from common import configuration
from common import logging

from common.exceptions import Forbidden, Unauthorized,\
                              raise_exception, register_error_handlers


# def rbac_permission_check_failed():
#     if g.current_user.username == 'anonymous_user':
#           raise_exception(Unauthorized("RBAC rules do not allow anonymous access the requested url"))
#     else: raise_exception(Forbidden("RBAC rules do not allow the user to access the requested url", user=str(g.current_user)))
# rbac = RBAC(role_model=Role, user_model=User,
#             user_loader=lambda: authentication.get_authenticated_user(),
#             permission_failed_hook=rbac_permission_check_failed)

def flask_config_merge(app, flask_config):
    for key, value in flask_config.items(): app.config[key] = value
    return app

def register_blueprints(app):
    #register api blueprints
    #new api runs at <host>/enclouden/sessionbroker/api
    from api.v2_0 import api_bp as api_v2_0
    app.register_blueprint(api_v2_0, url_prefix='/api/v2.0')
    #register frontend blueprint
    return app

def create_app():
    app = Flask(configuration.system['app_name'], static_folder='frontend')
    app = register_blueprints(app)
    app = register_error_handlers(app)
    return app

def init_app_plugins(app):
    # rate_limiter.init_app(app)
    # rbac.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    return app

def create_and_initialize_app(config_name):
    configuration.load_configuration(config_name)
    app = create_app()
    app = flask_config_merge(app, configuration.system['flask_configuration'])
    app = init_app_plugins(app)
    logging.configure_app_logger(configuration.system['debug'], app)
    return app
