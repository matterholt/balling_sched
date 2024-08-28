from pydantic import BaseModel
from enum import Enum, IntEnum


class RolePermsionsEnum (str, Enum):
    create = 'create'
    read = 'read'
    update = 'update'
    delete = 'delete'

# set up by admin
class Roles_Base (BaseModel):
    id : int
    role_type: str
    permission: RolePermsionsEnum
    allowed : str

# coaches task to add the basic, first last and contact. the rest is optional ??
# if coach is adding then will be default as role as gardian/parent
# coaches responsiablity to sign up unless i get the admisatranion buys lience
class Users_Base (BaseModel):
    user_id : int
    fist_name: str
    last_name:str
    player : str
    role_id : int
    contact_id: int
    teams_id : int

# best way to contact the players and
class User_Contact_Base (BaseModel):
    eamil: str | None = None
    phone: str | None = None

class Team_Base (BaseModel):
    id : str
    sponsor:str
    association_name: str
    group_class: str
    season_year: str

class Field_Satus_Enum (str,Enum):
    home="home"
    vistor="vistor"
    practice = "practice"

class Team_Schedule_Base (BaseModel):
    start_event_datetime: str
    end_event_datetime: str
    team_field_status: Field_Satus_Enum
    field_id : str
    location: str | None = None
    opponent: str | None = None
