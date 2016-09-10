import re
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import exc
from sqlalchemy.orm import sessionmaker
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
    """Check de value and search in db"""
    try:
        info = _search(store.upper())
    except exc.NoResultFound:
        return False

    return info


def _search(store):
    """Search store in db"""
    return session.query(Store).filter(Store.code == store).one()
