import os
from models import setup_db, Actor, Movie, create_and_drop_all, setup_migrations
import datetime
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import requires_auth, AuthError


Movie_Per_Page = 10


def pagination_Movie(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * Movie_Per_Page
    end = start + Movie_Per_Page

    movies = [Movie.format() for Movie in selection]
    current_movies = movies[start:end]
    return current_movies


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             "Content-Tpe,Authorization,true")
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,PATCH,DELETE,OPTIONS')
        return response

##--------------------------------------------------------------------------------##

                                    # MOVIES #

##--------------------------------------------------------------------------------##

   # get movies from database
    @app.route('/movies')
    @requires_auth('view:movies')
    def View_Movies(payload):

        movies = Movie.query.all()
        if len(movies) == 0:
            abort(404)
        total_movies = len(movies)
        current_movies = pagination_Movie(request, movies)

        return jsonify({"success": True,
                        "movies": current_movies,
                        "total_movies": total_movies
                        })



 # create a new movie 
    @app.route('/movies', methods=['POST'])
    @requires_auth('add:movies')
    def Create_Movies(payload):

        data = request.get_json()

        # abort if the request body is invalid
        if not ('title' in data and 'release_date' in data and 'genre' in data):
            abort(422)

        try:
            movie = Movie(
                title=data.get('title'),
                release_date=datetime.date.fromisoformat(data.get('release_date')),
                genre=data.get("genre")
                )
            # add the new  to the database
            movie.insert()
            # get the movies ordered by id
            movies = Movie.query.order_by(Movie.id).all()
            # total number of movies in the database after insert the new movie
            total_movies = len(movies)
            # paginate the movies
            current_movies = pagination_Movie(request, movies)
            return jsonify({
                "success": True,
                "created": movie.title,
                "movies": current_movies,
                "total_movies": total_movies,
            })

        except:
            abort(422)
            
            
            
     #edit the movie by id 
    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('Edit:movies')
    def Edit_movies(payload, id):
      
        try:
            data = request.get_json()
            if data is None:
                abort(400)
                
            movie = Movie.query.get(id)
            
            if movie is None:
                abort(404)
                
            if 'title' in data:
                movie.title = data.get('title')
            if 'release_date' in data:
                movie.release_date = data.get('release_date')
            if 'genre' in data:
                movie.genre = data.get('genre')
                
            movie.update()
            
            return jsonify({
                "success": True,
                "movie": movie.format()
            })
        except :
             abort(402)

        
        
        
        
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        try:
            movie = Movie.query.get(id)
            
            if movie is None:
                abort(404)
                
            movie.delete()
            
            return jsonify({
                "success": True,
                "deleted": movie.title
            })
        except :
          abort(402)
        
        
        
        
        
        
        
        
          
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
