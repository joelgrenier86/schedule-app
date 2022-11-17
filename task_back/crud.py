from sqlalchemy.orm import Session
import datetime
from . import models, schemas


#functions required for user: get all, get by id, get by email, post/create user
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, admin=False)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#functions required for meetings: get all, get by id, get by client_id, 
def get_meetings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Meeting).offset(skip).limit(limit).all()

def get_meeting(db: Session, meeting_id: int):
    return db.query(models.Meeting).filter(models.Meeting.id == meeting_id).first()

def get_meetings_by_client(db: Session, client_id:int, admin:bool):
    #again, this is simplified for specified use case.  We are assuming 1 admin account tied to all meetings
    if admin:
        return db.query(models.Meeting).all()
    else:    
        return db.query(models.Meeting).filter(models.Meeting.client_id == client_id).all()


def create_user_meeting(db: Session, meeting: schemas.MeetingCreate, user_id: int):
    db_meeting = models.Meeting(**meeting.dict(), client_id=user_id)
    db.add(db_meeting)
    db.commit()
    db.refresh(db_meeting)
    return db_meeting