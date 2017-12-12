import requests
import json
from random import randint

from app.helpers import register_action, api_endpoint
from pyramid.view import view_config


@view_config(route_name='random', renderer='templates/random_quote.pt')
def RandomQuote(request):
    register_action(request)
    quotes = json.loads(requests.get(api_endpoint).text)
    index = randint(0, len(quotes['quotes'])-1)
    return {'random_quote': quotes['quotes'][index]}

