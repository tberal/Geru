import requests
import json

from app.helpers import register_action, api_endpoint
from pyramid.view import view_config


@view_config(route_name='quote', renderer='templates/quote.pt')
def GetQuote(request):
    register_action(request)
    quote_number = request.matchdict['quote_number']
    return json.loads(requests.get(api_endpoint+'/'+str(quote_number)).text)
