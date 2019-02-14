""" SQL Database Models 

This is the database schema used for accessing the SQL database.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Table, Column, Integer, String, MetaData,
                        ForeignKey, DateTime)

Base = declarative_base()

class CommitMeta(Base):

    __tablename__ = 'commit_meta'

    Column('id', Integer, primary_key=True, nullable=False)
    Column('owner_name', String(100), nullable=False)
    Column('project_name', String(100), nullable=False)
    Column('commit_hash', String(40),
           ForeignKey("commit_info.commit_hash"),
           ForeignKey("commit_author.commit_hash"),
           ForeignKey("commit_contribs.commit_hash"),
           ForeignKey("commit_file.commit_hash"),
           nullable=False, index=True, unique=True)


class CommitAuthor(Base):

    __tablename__ = 'commit_author'

    Column('id', Integer, primary_key=True)
    Column('commit_hash', String(40), nullable=False,
           index=True, unique=True)
    Column('author_name', String(100), nullable=False,
           index=True)
    Column('author_email', String(200), nullable=True)
    Column('author_datetime', DateTime, nullable=False)

class CommitContrib(Base):

    __tablename__ = "commit_contrib"

    Column('id', Integer, primary_key=True)
    Column('commit_hash', String(40), nullable=False,
           index=True, unique=True)
    Column('contrib_name', String(100), nullable=False,
           index=True)
    Column('contrib_email', String(200), nullable=True)
    Column('contrib_datetime', DateTime,
           nullable=False)
    
class CommitFile(Base):

    __tablename__ = "commit_file"

    Column('id', Integer, primary_key=True)
    Column('commit_hash', String(40), nullable=False,
           index=True, unique=True)
    Column('modified_file', String(400), nullable=False)
    Column('modified_add_lines', Integer, nullable=False)
    Column('modified_subtract_lines', Integer, nullable=False)


class CommitInfo(Base):

    __tablename__ = "commit_info"

    Column('id', Integer, primary_key=True)
    Column('commit_hash', String(4), nullable=False,
           index=True, unique=True)
    Column('subject', String(400), nullable=False)
    Column('message', String(1500), nullable=False)

