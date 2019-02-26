""" Place log information into objects 

This is going to generate items for each specified model object
based on git log commands. 
"""
from datetime import datetime
from urllib.parse import urljoin

from okra.models import Meta, Author, Contrib, CommitFile, Info
from okra.gitlogs import (parse_commits, parse_messages,
                          parse_commited_files)

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
        fobjs = parse_committed_files(repopath):

    else:
        # retrieve from last commit HEAD
        # need to set 'c1' lists

        cmts = parse_commits(repopath, chash=last_commit)
        msgs = parse_messages(repopath, chash=last_commit)
        fobjs = parse_committed_files(repopath, chash=last_commit)

    # map objects to database objects

    """
    
    CommitFile(file_id='',
               commit_hash='',
               modified_file='',
               lines_added='',
               lines_subtracted='')

    """

    for msg in msgs:

        msg_item = Info(commit_hash=msg.hash_val,
                        subject=msg.subject,
                        message=msg.message_body,
                        created=datetime.fromisoformat(msg.timestamp))

        o,p = repo_name.split('/')
        meta_item = Meta(commit_hash=msg.hash_val,
                         owner_name=o,
                         project_name=p)

        yield msg_item, meta_item

    for cmt in cmts:
        
        author_item = Author(commit_hash=cmt.hash_val,
                             name=cmt.author,
                             email=cmt.author_email,
                             authored=datetime.\
                             fromisoformat(cmt.author_timestamp))

        contrib_item = Contrib(commit_hash=cmt.hash_val,
                               name=cmt.committer,
                               email=cmt.committer_email,
                               contributed=datetime.\
                               fromisoformat(cmt.committer_timestamp))
        
        yield author_item, contrib_item
        
    for fobj in fobjs:
        pass





    


