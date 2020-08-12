import sqlalchemy
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext import declarative

import settings

engine = sqlalchemy.create_engine(settings.POSTGRES_DB_PATH)
meta = sqlalchemy.MetaData(engine)
Base = declarative.declarative_base()


class PostTable(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    date = Column(Date)
    link = Column(String)


def create_tables():
    """Creates tables of db."""
    Base.metadata.create_all(engine, checkfirst=True)
