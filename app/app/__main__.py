from waitress import serve
from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

session_factory = SignedCookieSessionFactory('gerutestkey')


def main(**settings):
    config = Configurator(settings=settings)
    config.set_session_factory(session_factory)
    config.include('pyramid_chameleon')
    config.add_route('random', '/quotes/random')
    config.add_route('index', '/')
    config.add_route('quotes', '/quotes')
    config.add_route('quote', '/quotes/{quote_number}')
    config.add_route('actions', '/actions')
    config.add_route('session_actions', '/sessions/{session_id}')
    config.add_route('sessions', '/sessions')
    config.scan('app.views')
    return config.make_wsgi_app()


if __name__ == '__main__' :
    app=main()
    serve(app, host='0.0.0.0', port=5000)
