import requests
import json

from pyramid.view import view_config

from app.helpers import Session, convert_dict
from app.models import UserSession


@view_config(route_name='session_actions', renderer='json')
def GetSession(request):
    db_session = Session()
    query = db_session.query(UserSession).filter(
            UserSession.id == request.matchdict['session_id']
            ).first()
    actions = query.actions
    db_session.close()
    return convert_dict(actions)
