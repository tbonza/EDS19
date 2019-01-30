"""
Database Schemata

http://janvitek.org/events/NEU/6050/a2.html
"""
import io
from contextlib import redirect_stdout

from sqlalchemy import create_engine
from sqlalchemy import (Table, Column, Integer, String, MetaData,
                        ForeignKey, DateTime)

def config_assn2_schema():
    """ Configure the database schema for assignment 2 """
    metadata = MetaData()

    commit_meta = Table('commit_meta', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('owner_name', String),
                       Column('project_name', String),
                       Column('commit_hash', String),
    )

    commit_author = Table('commit_author', metadata,
                          Column('id', Integer, primary_key=True),
                          Column('commit_hash', String), # foreign key
                          Column('author_name', String),
                          Column('author_email', String),
                          Column('author_datetime', DateTime),
    )

    commit_contribs = Table('commit_contribs', metadata,
                            Column('id', Integer, primary_key=True),
                            Column('commit_hash', String), # foreign key
                            Column('contrib_name', String),
                            Column('contrib_email', String),
                            Column('contrib_datetime', DateTime),
    )

    commit_file = Table('commit_file', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('commit_hash', String), # foreign key
                        Column('modified_file', String),
                        Column('modified_add_lines', Integer),
                        Column('modified_subtract_lines', Integer),
    )

    commit_info = Table('commit_info', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('commit_hash', String), # foreign key
                        Column('subject', String),
                        Column('message', String),
    )

    reference = """
    master = Table('master', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('owner_name', String),
                   Column('project_name', String),
                   Column('commit_hash', String),
                   Column('parent_commit_hash', String),
                   Column('commit_author_name', String),
                   Column('commit_author_email', String),
                   Column('commit_commiter_name', String),
                   Column('commit_commiter_email', String),
                   Column('commit_author_datetime', DateTime),
                   Column('commit_commiter_datetime', DateTime),
                   Column('commit_subject', String),
                   Column('commit_message', String),
                   Column('commit_modified_file', String),
                   Column('commit_modified_add_lines', Integer),
                   Column('commit_modified_subtract_lines', Integer),
    )"""            
    return metadata

def metadata_tosql(metadata, db_url: str):
    """ Convert Database metadata into SQL statements. 
    
    Generate SQL for any database supported by SQLAlchemy.
    No commands are executed on a database by this function
    so the db_url can be a mock.

    :param metadata: MetaData object from sqlalchemy containing db schema
    :param db_url: database url, can be a mock
    :return: SQL database schema for db_url database type
    :rtype: string
    """

    def metadata_dump(sql, *multiparams, **params):
        """ print or write to log or file etc """
        print(sql.compile(dialect=engine.dialect))

    engine = create_engine(db_url, strategy='mock', executor=metadata_dump)

    f = io.StringIO()
    with redirect_stdout(f):
        metadata.create_all(engine)
    out = f.getvalue()
    return out

    
