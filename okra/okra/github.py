""" Place log information into objects 

This is going to generate items for each specified model object
based on git log commands. 
"""
from urllib.parse import urljoin

from okra.models import Meta, Author, Contrib, CommitFile, Info
from okra.assn1_data import (parse_commits, parse_messages, parse_files)

def repo_to_objects(repo_name: str, dirpath: str, last_commit=""):
    """ Retrieve objects from last commit if exists

    This function is a generator so we can specify a buffer size
    when making commits to the database. Otherwise, the I/O would
    slow things way down.

    :param repo_name: git user/git repo name, 'tbonza/EDS19'
    :param dirpath: path to directory storing repo information
    :param last_commit: string of git commit hash last stored in database
    :return: generator of populated model database objects
    :rtype: sqlalchemy database objects
    """
    repopath = urljoin(dirpath, repo_name)

    if len(last_commit) == 0:
        
        cmts = parse_commits(repopath):
        msgs = parse_messages(repopath):
        fobjs = parse_files(repopath):

    else:
        # retrieve from last commit HEAD
        # need to set 'c1' lists

        c1_commits = []
        cmts = parse_commits(repopath, c1=c1_commits):

        c1_messages = []
        msgs = parse_messages(repopath, c1=c1_messages):

        c1_files = []
        fobjs = parse_files(repopath, c1=c1_files):

    # map objects to database objects

    for cmt in cmts:
        pass

    """
    Meta(commit_hash='',
         owner_name='',
         project_name='')

    Author(commit_hash='',
           name='',
           email='',
           authored='')

    Contrib(contrib_id='',
            commit_hash='',
            name='',
            email='',
            contributed='')

    CommitFile(file_id='',
               commit_hash='',
               modified_file='',
               lines_added='',
               lines_subtracted='')

    Info(commit_hash='',
         subject='',
         message='',
         created='')
    """

    for msg in msgs:

        msg_item = Info(commit_hash=msg.hash_val,
                        subject=msg.subject,
                        message=msg.message_body,
                        created='')

        yield msg_item


    for fobj in fobjs:
        pass



    


