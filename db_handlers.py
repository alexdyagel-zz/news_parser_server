import contextlib

import sqlalchemy
from sqlalchemy import orm
import models
import settings


@contextlib.contextmanager
def db_session(db_url):
    """Creates a context with an open SQLAlchemy session."""
    engine = sqlalchemy.create_engine(db_url, convert_unicode=True)
    connection = engine.connect()
    session = orm.scoped_session(orm.sessionmaker(autocommit=False,
                                                  autoflush=True,
                                                  bind=engine,
                                                  expire_on_commit=False))
    try:
        yield session
    finally:
        session.commit()
        session.expunge_all()
        session.close()
        connection.close()


class PostgresHandler:
    """This is a class for performing operations with database."""
    def __init__(self, db_string):
        self.db_string = db_string

    def add_post(self, data: dict):
        """Adds post to db."""
        if self.get_post_by_title(data.get('title')):
            return
        post = models.PostTable(**data)
        with db_session(self.db_string) as db:
            db.add(post)
        return post

    def get_posts(self):
        """Gets all posts from db."""
        with db_session(self.db_string) as db:
            return db.query(models.PostTable).all()

    def get_post_by_title(self, title: str):
        """Returns news post by its title."""
        with db_session(self.db_string) as db:
            return db.query(models.PostTable).filter_by(title=title).first()

    def get_posts_by_date(self, date: str):
        """Returns news posts by its date."""
        with db_session(self.db_string) as db:
            return db.query(models.PostTable).filter_by(date=date).all()


PG_HANDLER = PostgresHandler(settings.POSTGRES_DB_PATH)
