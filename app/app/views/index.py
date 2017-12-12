import requests
import json

from app.helpers import register_action, api_endpoint
from pyramid.view import view_config


@view_config(route_name='index', renderer='templates/index.pt')
def Index(request):
    register_action(request)
    return {'status': 'OK'}
