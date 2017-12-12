from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import UserSession, Action

api_endpoint = 'https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes'

engine = create_engine('sqlite:///memory')
UserSession.metadata.create_all(engine)
Action.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def register_action(request):
    session = request.session
    if 'active' not in session:
        new_session = UserSession()
        db_session = Session()
        db_session.add(new_session)
        db_session.commit()
        session['id'] = new_session.id
        session['active'] = True
        db_session.close()
    new_action = Action(
            session_id=session['id'],
            url=request.url
            )
    db_session = Session()
    db_session.add(new_action)
    db_session.commit()
    db_session.close()

def query_dict(db_obj):
    db_session = Session()
    query = db_session.query(db_obj).all()
    db_session.close()
    return convert_dict(query)

def convert_dict(query_obj):
    return {'data':[{
        k: str(v) for k, v in row.__dict__.items() if not str(k).startswith("_")
        } for row in query_obj]}
