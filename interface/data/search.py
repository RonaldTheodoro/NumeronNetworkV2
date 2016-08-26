import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, exc
from .models import Base
from .models import Store


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_DIR = 'sqlite:///' + os.path.join(BASE_DIR, 'database', 'store.db')
engine = create_engine(DB_DIR)

Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def search_store(store):
    try:
        store = _format_info(store)
    except:
        return None

    try:
        info = _search(store)
    except exc.NoResultFound:
        return False

    return info
    
def _format_info(store):
    store = store.upper()

    if len(store) != 2:
        raise

    return store


def _search(store):
    return session.query(Store).filter(Store.code == store).one()
