import os
from models import setup_db, Actor, Movie, create_and_drop_all, setup_migrations
import datetime
from flask import Flask, request, abort, jsonify,session,redirect,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import requires_auth, AuthError
from authlib.integrations.flask_client import OAuth
from urllib.parse import urlencode


movies_or_actors_Per_Page = 10


AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
ALGORITHMS = os.getenv('ALGORITHMS')
API_AUDIENCE =  os.getenv('API_AUDIENCE')
SECRET_KEY =  os.getenv('SECRET')
CLIENT_id = os.getenv('client_id')

def pagination_movie_or_actor(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * movies_or_actors_Per_Page
    end = start + movies_or_actors_Per_Page

    movies_or_actors = [movie_or_actor.format() for movie_or_actor in selection]
    current_movies_or_actors = movies_or_actors[start:end]
    return current_movies_or_actors


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    oauth = OAuth(app)

    auth0 = oauth.register(
    'auth0',
    client_id=CLIENT_id,
    client_secret=SECRET_KEY,
    api_base_url=f'https://{AUTH0_DOMAIN}',
    access_token_url=f'https://{AUTH0_DOMAIN}/oauth/token',
    authorize_url=f'https://{AUTH0_DOMAIN}/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)
    setup_db(app)
    setup_migrations(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             "Content-Type,Authorization,true")
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,PATCH,DELETE,OPTIONS')
        return response

    @app.route('/callback')
    def callback_handling():
    # Handles response from token endpoint
     token = auth0.authorize_access_token()
     print(token)
     resp = auth0.get('userinfo')
     userinfo = resp.json()

    # Store the user information in flask session.
     session['jwt_payload'] = userinfo
     session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
     return redirect('/movies')


    @app.route('/login')
    def login():
     return auth0.authorize_redirect(redirect_uri='https://radiant-sands-87798.herokuapp.com/callback',audience=API_AUDIENCE)

    @app.route('/logout')
    def logout():
        session.clear()
        params = {'returnTo': url_for('login', _external=True), 'client_id': CLIENT_id}
        return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))


##--------------------------------------------------------------------------------##

                                    # MOVIES #

##--------------------------------------------------------------------------------##

   # get movies from database
    @app.route('/movies')
    @requires_auth('view:movies')
    def view_Movies(payload):
        
    
        movies = Movie.query.all()
        if movies is None:
            abort(404)
            
        total_movies = len(movies)
        current_movies = pagination_movie_or_actor(request, movies)

        return jsonify({"success": True,
                        "movies": current_movies,
                        "total_movies": total_movies
                        })



 # create a new movie 
    @app.route('/movies', methods=['POST'])
    @requires_auth('add:movies')
    def create_Movies(payload):

        data = request.get_json()
        
        if data is None:
            abort(400)

        # abort if the request body is invalid
        if ('title' not in data or 'release_date' not in data or 'genre' not in data):
            abort(400)

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
            return jsonify({
                "success": True,
                "created": movie.id,
                "total_movies": total_movies,
            })

        except:
            abort(422)
            
            
            
     #edit the movie by id 
    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('edit:movies')
    def edit_movies(payload, id):
      
        data = request.get_json()
           
        if data is None:
                abort(400)
                
        movie = Movie.query.get(id)
            
        if movie is None:
                abort(404)
      
        try:
           
                
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
             abort(422)

        
        
        
        
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        
        movie = Movie.query.get(id)
            
        if movie is None:
                abort(404)
                
        
        try:
           
            movie.delete()
            
            return jsonify({
                "success": True,
                "deleted": movie.id
            })
        except :
          abort(422)
        
        
        
 ##--------------------------------------------------------------------------------##

                                    # Actors #

##--------------------------------------------------------------------------------##

        
        
    @app.route('/actors')
    @requires_auth('view:actors')
    def view_actors(payload):
        
        
            actors = Actor.query.all()
            
            if actors is None:
                abort(404)
                
            total_actors = len(actors)
            current_actors = pagination_movie_or_actor(request, actors)
                
            return jsonify({
                "success": True,
                "actors": current_actors,
                "total_actors": total_actors,
            })
        
        
    @app.route('/actors', methods=['POST'])
    @requires_auth('add:actors')
    def create_actor(payload):
        
        
        data = request.get_json()
        
        if data is None: 
            abort(400)
            
        if ('name' not in data or 'age' not in data or 'gender' not in data):
                abort(400)
        try:
            
                
            actor = Actor(name=data.get("name"),
                          age=data.get("age"),
                          gender=data.get("gender")
                          )
            
            actor.insert()
            
            # get the actors ordered by id
            actors = Actor.query.order_by(Actor.id).all()
            # total number of actors in the database after insert the new actor
            total_actors = len(actors)
            # paginate the actors
            return jsonify({
                "success": True,
                "created": actor.id,
                "total_actors": total_actors,
            })
        except :
            abort(422)
            
            
    
    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('edit:actors')
    def edit_actor(payload, id):
        
        data = request.get_json()
            
            
        if data is None:
                abort(400)
                
        actor = Actor.query.get(id)
            
        if actor is None:
                abort(404)
                
        
        try:
            
            
            if 'name' in data:
                actor.name = data.get("name")
                
            if 'age' in data:
                actor.age = data.get("age")
                
            if 'gender' in data:
                actor.gender = data.get("gender")
                
            actor.update()
            
            return jsonify({
                "success": True,
                "actor": actor.format()
            })
        except :
            abort(422)     
            
       
    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload,id):
        
        actor = Actor.query.get(id)
            
        if actor is None:
            abort(404)
                
        try:
            
            actor.delete()
            
            return jsonify({
                "success": True,
                "deleted": actor.id
                })
        except:
            abort(422)   
            
    
           
 ##--------------------------------------------------------------------------------##

                                    # ERROR HANDLER #

##--------------------------------------------------------------------------------##

        
    
    
    
# handle 404 error in the application
    @app.errorhandler(404)
    def not_found(error):
     return jsonify({
      "success": False,
      'error': 404,
      "message" : "The server can not find the requested resource"
      }
    ),404
  
  #handle 422 error in the application 
    @app.errorhandler(422)
    def unprocessable_entity(error):
     return jsonify({
      "success": False,
      "error": 422,
      "message": "The request was well-formed but was unable to be followed due to semantic errors."
    }),422
     
     
 # handle 400 error in the application 
    @app.errorhandler(400)
    def bad_request(error):
     return jsonify({
      "success": False,
      "error": 400,
      "message": "The server could not understand the request due to invalid syntax."
    }),400        
            
    @app.errorhandler(AuthError)
    def auth_error(error):
        print(error)
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code
       
            
            
           
    return app


app = create_app()

if __name__ == '__main__':
    app.run(port=8080, debug=True)
