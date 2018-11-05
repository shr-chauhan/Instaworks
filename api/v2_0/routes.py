from .team_members import TeamMembersAPI, SingleTeamMembersAPI
from . import api_bp
from api import APIBase
from app import rate_limiter
from flask import jsonify
from schemas import ma
api_mappers = [TeamMembersAPI, SingleTeamMembersAPI]


for mapper_obj  in api_mappers:
    view = mapper_obj.as_view(mapper_obj.api_endpoint)
    api_bp.add_url_rule(mapper_obj.api_url, view_func=view)
