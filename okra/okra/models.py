""" SQL Database Models 

This is the database schema used for accessing the SQL database.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (Table, Column, Integer, String, MetaData, Numeric,
                        ForeignKey, DateTime, create_engine)

Base = declarative_base()


class CommitMeta(Base):

    __tablename__ = 'commit_meta'

    commit_hash = Column('commit_hash', String(40), primary_key=True,
                         index=True)
    owner_name = Column('owner_name', String(100), nullable=False)
    project_name = Column('project_name', String(150), nullable=False)

class CommitAuthor(Base):
    """ 
    Author email is false, not all authors require a github account,
    so an email is not going to be required. 
    """
    __tablename__ = 'commit_author'

    commit_hash = Column('commit_hash', String(40), primary_key=True,
                         index=True)
    author_name = Column('author_name', String(150), nullable=False,
                         index=True)
    author_email = Column('author_email', String(200), nullable=True)
    authored = Column('authored', DateTime, nullable=False)

class CommitContrib(Base):

    __tablename__ = 'commit_contrib'

    contrib_id = Column('contrib_id', Integer, primary_key=True)
    commit_hash = Column('commit_hash', String(40), index=True,
                         nullable=False)
    contrib_name = Column('contrib_name', String(150), index=True,
                          nullable=False)
    contrib_email = Column('contrib_email', String(200), nullable=True)
    contributed = Column('contributed', DateTime, nullable=False)

class DataAccessLayer(object):

    def __init__(self, conn_string):
        self.engine = None
        self.session = None
        self.conn_string = conn_string

    def connect(self):
        self.engine = create_engine(self.conn_string)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
