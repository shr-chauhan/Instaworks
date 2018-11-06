from flask import jsonify
from api import APIBase
import schemas
from database import team_members as team_model
from common import exceptions
from common.logging import applogger


class TeamMembersAPI(APIBase):
    '''API for working with Team Members'''

    response_schema = schemas.team_members.TeamMembersSchema
    request_schema  = schemas.team_members.TeamMembersRequestSchema
    api_url         = '/team_members'
    api_endpoint    = 'team_members'

    def get(self):
        team_members = self.fetch_filter_sort_rows(team_model.TeamMember)
        return jsonify(self.select_fields(team_members, many=True))

    def post(self):
        '''create new group, by providing the group name'''
        request_data=self.get_parsed_request_data()
        try:
            team_member=team_model.TeamMember.create_member(first_name=request_data['first_name'], last_name=request_data['last_name'], phone_number=request_data['phone_number'], email=request_data['email'], role=request_data['role'])
        except:
            raise exceptions.BadRequest('invalid request, email_id or phone number already exists')
        return jsonify(self.select_fields(team_member))


class SingleTeamMembersAPI(APIBase):
    '''API for working with Team Members'''

    response_schema = schemas.team_members.TeamMembersSchema
    request_schema  = schemas.team_members.TeamMembersRequestPatchSchema
    api_url         = '/team_member/<int:member_id>'
    api_endpoint    = 'team_member'

    def get(self, member_id):
        team_member = team_model.TeamMember.query.filter_by(id=member_id).first()
        return jsonify(self.select_fields(team_member))

    def delete(self,member_id):
        team_member = team_model.TeamMember.query.filter_by(id=member_id).first()
        if not team_member: raise exceptions.NotFound('Object not found, check the resource id')
        team_member.delete()
        return jsonify({})

    def patch(self, member_id):
        request_data=self.get_parsed_request_data()
        team_member = team_model.TeamMember.query.filter_by(id=member_id).first()
        if not team_member: raise exceptions.NotFound('Object not found, check the resource id')
        team_member.update_member(first_name=request_data['first_name'], last_name=request_data['last_name'], phone_number=request_data['phone_number'], email=request_data['email'], role=request_data['role'])
        return jsonify(self.select_fields(team_member))


 