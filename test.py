import os
import unittest
from app import app, db


TEST_DB = 'test.db'


class BasicTests(unittest.TestCase):


    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/ewa_anna_szyszka/Desktop/Test/test.db'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        pass


###############
#### tests ####
###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def add(self):
        data = {'new'}
        req = requests.post('http://localhost:5000', data = data)
        self.assertEqual(req.url, "http://localhost:5000")

if __name__ == "__main__":
    unittest.main()
