""" Compute Truck Factor

The truck factor assignment includes several factors. We're just
going to focus on the actual truck factor computation from a database
in this file.

References:
  http://janvitek.org/events/NEU/6050/a4.html
"""
from sqlalchemy import func
from okra.models import (Meta, Author, Contrib, CommitFile, Info)

def total_number_of_files_by_project(proj_name, dal):
    """ Compute the total number of files by project. """
    q = dal.session.query(CommitFile.modified_file).\
        group_by(CommitFile.modified_file).all()
    return len(q)

def author_file_owned(proj_name, dal):
    """ Compute file ownership by each author. """

    # Number of lines added by each author per file
    q = dal.session.\
        query(Meta.commit_hash, Author.name, Author.email,
              CommitFile.modified_file,
              func.sum(CommitFile.lines_added).label("total_lines_added"))
    q = q.join(Author).join(CommitFile)
    q = q.group_by(Author.name, CommitFile.modified_file)

    # Author with max number of lines added per file (owner)
    res = q.all()
    return res

def get_truck_factor_by_project(proj_name, dal):
    """ Get the 'truck factor' by project.

    1. For each project, and each file, compute how many lines were 
       added by each unique user.
    2. For each project, and each file, find which user created the file.
    3. Given the above two results compute the ownership of each file.
    4. For each project, and each file pick an owner.
    5. For each project, rank the users by the number of files they own.
    6. Given all of the above compute the Truck Factor as the smallest set 
       of users such that they own more than half of the files in the project.

    :param proj_name: name of GitHub project
    :param dal: okra.models.DataAccessLayer() with connection string param
    :return: Truck factor score for a GitHub project
    :rtype: float
    """
    pass
