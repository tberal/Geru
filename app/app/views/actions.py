import requests
import json

from pyramid.view import view_config

from app.helpers import query_dict
from app.models import Action


@view_config(route_name='actions', renderer='json')
def GetActions(request):
    return query_dict(Action)
