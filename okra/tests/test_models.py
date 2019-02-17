""" Validating data models at the SQLAlchemy ORM layer. """
import unittest

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from okra.models import DataAccessLayer, Cookie

DAL = DataAccessLayer('sqlite:///:memory:')

def mock_db(session):
    c1 = Cookie(cookie_name='dark chocolate chip',
                cookie_recipe_url='http://some.aweso.me/cookie/dark_cc.html',
                cookie_sku='CC02',
                quantity=1,
                unit_cost=0.75)

    session.bulk_save_objects([c1])
    session.commit()

class TestModels(unittest.TestCase):
    """ Verifying model behavior. """

    @classmethod
    def setUpClass(cls):
        DAL.connect()
        DAL.session = DAL.Session()
        mock_db(DAL.session)
        DAL.session.close()

    def setUp(self):
        self.dal = DAL
        self.dal.session = self.dal.Session()
        
    def tearDown(self):
        self.dal.session.rollback()
        self.dal.session.close()

    # Adding and updating objects

    def test_add_commit_meta(self):
        pass
    

    
