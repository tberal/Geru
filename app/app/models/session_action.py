from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from .base import Base


class Action(Base):
    """
    Database model for registered action.

    Fields:
        id = The unique identifier of an action;
        session_id = Reference to an active session performing this action;
        url = The url accessed in this action;
        created = the date/time when the action was performed;
    """
    __tablename__ = 'actions'
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('sessions.id'), nullable=False)
    url = Column(String(1024), nullable=False)
    created = Column(DateTime, default=datetime.utcnow, nullable=False)
