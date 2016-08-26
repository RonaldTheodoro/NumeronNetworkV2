import os
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Store(Base):
    __tablename__ = 'store'
    id = Column(Integer, primary_key=True)
    code = Column(String(2), nullable=False)
    store = Column(String(40), nullable=False)
    ramal = Column(String(4), nullable=False)
    phone = Column(String(15), nullable=False)
    ip1 = Column(String(15), nullable=False)
    ip2 = Column(String(15), nullable=False)
    router = Column(String(15), nullable=False)
    sonicwall = Column(String(15), nullable=False)
    desigination = Column(String(13), nullable=False)
    cnpj = Column(String(15), nullable=False)
    supervisor = Column(String(35), nullable=False)
    uf = Column(String(2), nullable=False)
    city = Column(String(20), nullable=False)
    local = Column(String(10), nullable=False)
    label = Column(String(20), nullable=False)
    cep = Column(String(9), nullable=False)
    ie = Column(String(14), nullable=False)
    address = Column(String(150), nullable=False)
