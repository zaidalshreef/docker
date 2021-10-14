import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Movie, Actor, create_and_drop_all
from app import create_app

TEST_DATABASE_URI = os.getenv('TEST_DATABASE_URI')
ASSISTANT_TOKEN = os.getenv('ASSISTANT_TOKEN')
DIRECTOR_TOKEN = os.getenv('DIRECTOR_TOKEN')
PRODUCER_TOKEN = os.getenv('PRODUCER_TOKEN')


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, TEST_DATABASE_URI)

        self.new_movie = {
            'title': 'Escapes',
            'release_date': '2021-02-21',
            'genre': "Action",
        }
        
        self.new_actor = {
            'name': 'zaid',
            'age': 30,
            'gender': 'male',
        }
        
        self.auth_assistant = {
            'Authorization': "Bearer {}".format(ASSISTANT_TOKEN)
        }
        self.auth_director = {
            'Authorization': "Bearer {}".format(DIRECTOR_TOKEN)
        }
        self.auth_producer = {
            'Authorization': "Bearer {}".format(PRODUCER_TOKEN)
        }
        
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            create_and_drop_all()
            # self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass
    
    
    
    
    def test_movies(self):
        
        res = self.client().get('/movies', headers=self.auth_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        
    def test_401_unauthorized_access_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['code'], 'authorization_header_missing')
