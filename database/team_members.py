from . import db, BaseMixin

from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
import database
import enum
from common import exceptions
from common.logging import applogger

class TeamMemberEnum(enum.Enum):
    admin     = "admin"
    regular   = "regular"

class TeamMember(BaseMixin, db.Model):
    __tablename__       = 'team_members'
    __bind_key__        = 'team_db'
    __repr_attrs__      = ["id", "email", "phone_number"]
    __track_attrs__     = ["name", "uuid", "instances"]
    #attributes
    id                  = db.Column(db.Integer, primary_key=True)
    first_name          = db.Column(db.String, nullable=False, index=True)
    last_name           = db.Column(db.String, index=True)
    phone_number        = db.Column(db.BigInteger, unique=True, index=True)
    email               = db.Column(db.String, unique=True, index=True)
    role                = db.Column(db.Enum(TeamMemberEnum), nullable=False, default=TeamMemberEnum.regular)

    @staticmethod
    def create_member(first_name, last_name, phone_number, email, role):
        new_member = TeamMember(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, role=role)
        db.session.add(new_member)
        db.session.commit()
        return new_member

    def delete(self,commit=True):
        db.session.delete(self)
        if commit: db.session.commit()
        
    def update_member(self, first_name, last_name, phone_number, email, role):
        if first_name is not None: self.first_name=first_name
        if last_name is not None: self.last_name=last_name
        if phone_number is not None: self.phone_number=phone_number
        if email is not None: self.email=email
        if role is not None: self.role=role
        applogger.debug("Gettinggg dataaaa")
        db.session.add(self)
        db.session.commit()
        

