from marshmallow import fields
from marshmallow_enum import EnumField
from database import team_members as team_model
from schemas import ma

class TeamMembersSchema(ma.ModelSchema):
    class Meta:
        fields = ('_self','id', 'first_name', 'last_name', 'phone_number', 'email', 'role')
        model  = team_model.TeamMember
    _self      = ma.Hyperlinks({'url': ma.URLFor('.team_member', member_id='<id>'),})
    role       = EnumField(team_model.TeamMemberEnum, by_value=True)
    
class TeamMembersRequestSchema(ma.Schema):
    first_name         = fields.String(required=True)
    last_name          = fields.String(required=True)
    email              = fields.String(required=True)
    phone_number       = fields.Integer(required=True)
    role               = EnumField(team_model.TeamMemberEnum, by_value=True, required=True)



class TeamMembersRequestPatchSchema(ma.Schema):
    first_name         = fields.String(missing=None)
    last_name          = fields.String(missing=None)
    email              = fields.String(missing=None)
    phone_number       = fields.Integer(missing=None)
    role               = EnumField(team_model.TeamMemberEnum, by_value=True, missing=None)

    