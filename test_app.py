import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Movie, Actor, create_and_drop_all
from app import create_app
import datetime

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
    
    
    
    
    def test_view_movies(self):
        
        res = self.client().get('/movies', headers=self.auth_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        
    def test_401_unauthorized_access_to_view_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'],False)
    
    
    def test_create_movie(self):
        
        movies = Movie.query.all()
        
        res = self.client().post('/movies', json=self.new_movie, headers=self.auth_producer)
        data = json.loads(res.data)
        
        movies_after_create = Movie.query.all()
        new_movie_id = data["created"]
        movie = Movie.query.get(new_movie_id)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(movies_after_create), len(movies)+1)
        self.assertIsNotNone(movie)
        
        
    def test_400_create_movie(self):
        
        movie = {
            "release_date": "2022-01-02",
        }
        
        res = self.client().post('/movies', headers=self.auth_producer, json=movie)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],"The server could not understand the request due to invalid syntax.")
        
        
    def test_403_create_movie(self):
        
        res = self.client().post('/movies', headers=self.auth_assistant, json=self.new_movie)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        
        
    def test_401_create_movie(self):
        
        res = self.client().post('/movies', json=self.new_movie)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        
        
    def test_edit_movie(self):
        
        movie = Movie.query.first()
        res = self.client().patch('/movies/{}'.format(movie.id), json=self.new_movie, headers=self.auth_producer)
        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])
        
        
    def test_404_edit_movie(self):
        
        
        res = self.client().patch('/movies/10000', headers=self.auth_producer, json=self.new_movie)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        
        
    def test_403_edit_movie(self):
        
        res = self.client().patch('/movies/1', headers=self.auth_assistant, json=self.new_movie)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        
        
    def test_401_edit_movie(self):
        
        res = self.client().patch('/movies/1', json=self.new_movie)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        
                                                    
                                                    
    def test_delete_movie(self):
        
        movie = Movie(
                title="new Title",
                release_date=datetime.date.fromisoformat("2021-10-05"),
                genre="new"
                )
        
        movie.insert()
        id = movie.id
        movies = Movie.query.all()
        res = self.client().delete('/movies/{}'.format(id), headers=self.auth_producer)
        data = json.loads(res.data)
        
        movies_after_delete = Movie.query.all()
        deleted_movie = Movie.query.get(id)
        

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])
        self.assertEqual(len(movies),len(movies_after_delete)+1)
        self.assertEqual(deleted_movie,None)
        
    def test_404_delete_movie(self):
        
        
        res = self.client().delete('/movies/10000', headers=self.auth_producer)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        
        
    def test_403_delete_movie(self):
        
        res = self.client().delete('/movies/1', headers=self.auth_assistant)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        
        
    def test_401_delete_movie(self):
        
        res = self.client().delete('/movies/1',)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        
  ##-------------------------------------------------------##
  
                  ## Actors test ##
  
  ##-------------------------------------------------------##     
       
       
    
    def test_view_actors(self):
        
        res = self.client().get('/actors', headers=self.auth_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        
    def test_401_unauthorized_access_to_view_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'],False)
    
    
    def test_create_actors(self):
        
        actors = Actor.query.all()
        
        res = self.client().post('/actors', json=self.new_actor , headers=self.auth_director)
        data = json.loads(res.data)
        
        actors_after_create = Actor.query.all()
        new_actors_id = data["created"]
        actor = Actor.query.get(new_actors_id)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(actors_after_create), len(actors)+1)
        self.assertIsNotNone(actor)
        
        
    def test_400_create_actors(self):
        
        actor = {
            "age": 30,
        }
        
        res = self.client().post('/actors', headers=self.auth_director, json=actor)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],"The server could not understand the request due to invalid syntax.")
        
        
    def test_403_create_actors(self):
        
        res = self.client().post('/actors', headers=self.auth_assistant, json=self.new_movie)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        
        
    def test_401_create_actors(self):
        
        res = self.client().post('/actors', json=self.new_actor)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        
        
    def test_edit_actors(self):
        
        actor = Actor.query.first()
        
        res = self.client().patch('/actors/{}'.format(actor.id), json=self.new_actor, headers=self.auth_director)
        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])
        
        
    def test_404_edit_actors(self):
        
        
        res = self.client().patch('/actors/10000', headers=self.auth_director, json=self.new_actor)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        
        
    def test_403_edit_actors(self):
        
        res = self.client().patch('/actors/1', headers=self.auth_assistant, json=self.new_actor)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        
        
    def test_401_edit_actors(self):
        
        res = self.client().patch('/actors/1', json=self.new_actor)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        
                                                    
                                                    
    def test_delete_actors(self):
        
        actor = Actor(name="name",
                          age=30,
                          gender="gender" )
        actor.insert()
        id = actor.id
        actors = Actor.query.all()
        res = self.client().delete('/actors/{}'.format(id), headers=self.auth_director)
        data = json.loads(res.data)
        
        actors_after_delete = Actor.query.all()
        deleted_actor = Actor.query.get(id)
        

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])
        self.assertEqual(len(actors),len(actors_after_delete)+1)
        self.assertEqual(deleted_actor,None)
        
    def test_404_delete_actor(self):
        
        
        res = self.client().delete('/actors/10000', headers=self.auth_director)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        
        
    def test_403_delete_actor(self):
        
        res = self.client().delete('/actors/1', headers=self.auth_assistant)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        
        
    def test_401_delete_actor(self):
        
        res = self.client().delete('/actors/1',)
        data = json.loads(res.data)
      
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        
                                                                                                             
     
     
if __name__ == '__main__':
    unittest.main()                                                                                                             