from datetime import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import relationship, backref

from .base import Base


class UserSession(Base):
    """
    Database model for registered sessions.

    Fields:
        id = The unique identifier of a session;
        created = the date/time when the session was created;
    """
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.utcnow, nullable=False)

    actions = relationship('Action', order_by='Action.id', backref='session')
