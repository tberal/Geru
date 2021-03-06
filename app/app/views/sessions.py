import requests
import json

from pyramid.view import view_config
from sqlalchemy import inspect

from app.helpers import query_dict
from app.models import UserSession


@view_config(route_name='sessions', renderer='json')
def GetSessions(request):
    return query_dict(UserSession)
