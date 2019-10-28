from sqlalchemy import Column, Integer, Text, BLOB
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Setting(Base):
    __table_name__ = 'settings'

    key = Column(Text, primary_key=True)
    value = Column(Text, nullable=True)

    def __repr__(self):
        return "<Setting(key='%s', value='%s')>" % (self.key, self.value)

class Document(Base):
    __table_name__ = 'documents'

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    body = Column(Text, nullable=False)

    def __repr__(self):
        return "<Document(id='%s', title='%s', body='%s')>" % (self.id, self.tokens, self.docs_count)

class Token(Base):
    __table_name__ = 'tokens'

    id = Column(Integer, primary_key=True)
    token = Column(Text, nullable=False)
    docs_count = Column(Integer, nullable=False)
    postings = Column(BLOB, nullable=False)

    def __repr__(self):
        return "<Token(id='%s', token='%s', docs_count='%s', postings='%s')>" % (self.id, self.tokens, self.docs_count, self.postings)

def create_engine(db_path):
    return sqlalchemy.create_engine('sqlite://%s' % db_path)

def create_tables(engine):
    Base.metadata.cleate_all(engine)

def create_session(engine):
    return create_session(bind=engine, autocommit=True, autoflush=False)
