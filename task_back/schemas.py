from pydantic import BaseModel
import datetime




# declare a base model for each class/table in schema
class MeetingBase(BaseModel):
    note: str
    time: datetime.datetime

#pass any variables required for creation such as an encrypted password
class MeetingCreate(MeetingBase):
    pass

#add the auto generated id and implied client_id, activate orm_mode to allow 
#properties to be accessed with dot syntax
class Meeting(MeetingBase):
    
    id: int
    client_id:int
    client_ack:bool
    admin_ack:bool

    class Config:
        orm_mode = True

#repeat for user afterwords, as it relies on class Meeting()
class UserBase(BaseModel):
    email: str
    admin:bool
class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    
    meetings: list[Meeting] = []

    class Config:
        orm_mode = True


# class Notification():
#     id:int
#     client_id:int
#     meeting_id:int
#     client_dismiss:bool
#     admin_dismiss:bool
#     class Config:
#         orm_mode = True
