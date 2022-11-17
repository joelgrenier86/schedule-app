from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    admin = Column(Boolean, default = False)
    meetings = relationship("Meeting", back_populates="client")


class Meeting(Base):
    __tablename__ = "meetings"
    id = Column(Integer, primary_key=True, index=True)
    note = Column(String, index=True)
    time = Column(DateTime)
    client_id = Column(Integer, ForeignKey("users.id"))
    client = relationship("User", back_populates="meetings")
    client_ack = Column(Boolean, default = False)
    admin_ack = Column(Boolean, default = False)
    #normally an admin/employee/otherperson account would require a 2nd relationship, here we will manually set one user to admin for testing purposes


#started a notifications class as i would with a full application but realized 2 boolean columns in the meeting table is 
#sufficient

# class Notifications(Base):
#     __tablename__ = 'notifications'
#     id = Column(Integer, primary_key=True, index=True)
#     client_dismiss = Column(Boolean, default = False)
#     admin_dismiss = Column(Boolean, default = False)
#     client_id = Column(Integer, ForeignKey("users.id"))
#     client = relationship("User", back_populates="notifications")
#     meeting_id = Column(Integer, ForeignKey("meetings.id"))
#     meeting = relationship("Meeting", back_populates ="notifications")
