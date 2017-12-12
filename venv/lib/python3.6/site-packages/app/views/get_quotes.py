import requests
import json

from pyramid.view import view_config

from app.helpers import register_action, api_endpoint
from app.models import UserSession, Action


@view_config(route_name='quotes', renderer='templates/quotes.pt')
def GetQuotes(request):
    register_action(request)
    return json.loads(requests.get(api_endpoint).text)
