# Backend - Full Stack Trivia API 

### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 
  This will install all of the required packages we selected within the `requirements.txt` file.


## Testing
To run the tests, run 
```
dropdb casting_test
createdb casting_test
psql casting_test < casting.pgsql
python -m unittest test_app.py
```

## API Reference

### Endpoints

#### GET '/movies'
- General:
    - Return all movies in the database
    - Role Authorized: Assistant, Director, Producer
- Example: ```curl -H "Authorization: Bearer <Token>" http://127.0.0.1:5000/movies```
```
{
    "movies": [
        {
            "id": 2,
            "release_date": "Fri, 07 Feb 2020 00:00:00 GMT",
            "title": "Birds of Prey"
        },
        {
            "id": 3,
            "release_date": "Sun, 10 Mar 2013 00:00:00 GMT",
            "title": "The Great Gatsby"
        },
        {
            "id": 4,
            "release_date": "Fri, 20 May 2011 00:00:00 GMT",
            "title": "Pirates of the Caribbean: On Stranger Tides"
        },
        {
            "id": 6,
            "release_date": "Wed, 24 Jul 2019 00:00:00 GMT",
            "title": "once upon a time in hollywood"
        }
    ],
    "success": true
}
```
#### GET '/actors'
- General:
    - Return all actors in the database
    - Role Authorized: Assistant, Director, Producer
- Example: ```curl -H "Authorization: Bearer <Token>" http://127.0.0.1:5000/actors```
```
{
    "actors": [
        {
            "age": 30,
            "gender": "F",
            "id": 2,
            "movie_id": 2,
            "name": "Margot Robbie"
        },
        {
            "age": 45,
            "gender": "M",
            "id": 3,
            "movie_id": 3,
            "name": "Leonardo DiCaprio"
        },
        {
            "age": 35,
            "gender": "F",
            "id": 4,
            "movie_id": 3,
            "name": "Carey Mulligan"
        },
        {
            "age": 57,
            "gender": "M",
            "id": 5,
            "movie_id": 4,
            "name": "Johnny Depp"
        }
    ],
    "success": true
}
```

#### POST '/movies'
- General:
    - Add a new movie. The new movie must have all four information. 
    - Role Authorized: Producer
- Example: ```curl -X POST - H '{"Content-Type: application/json", "Authorization: Bearer <TOKEN>}' -d '{"title": "Call Me by Your Name", "release_date": "2017-10-20"}' http://127.0.0.1:5000/movies```
```
{
    "movie": {
        "id": 16,
        "release_date": "Fri, 20 Oct 2017 00:00:00 GMT",
        "title": "Call Me by Your Name"
    },
    "success": true
}
```

#### POST '/actors'
- General:
    - Add a new actor. The new movie must have all four information. 
    - Role Authorized: Director, Producer
- Example: ```curl -X POST - H '{"Content-Type: application/json", "Authorization: Bearer <TOKEN>}' -d '{"name": "Timothée Chalamet", "age": 24, "gender": "M", "movie_id": 6}' http://127.0.0.1:5000/actors```

```
{
    "actor": {
        "age": 24,
        "gender": "M",
        "id": 11,
        "movie_id": 6,
        "name": "Timothée Chalamet"
    },
    "success": true
}
```

#### PATCH '/movies/<int:id>'
- General:
    - Update some information of a movie based on a payload.
    - Roles authorized : Director, Producer.
- Example: ```curl http://127.0.0.1:5000/movies/3 -X PATCH -H '{"Content-Type: application/json", "Authorization: Bearer <TOKEN>}' -d '{ "title": "", "release_date": "2020-11-01" }'```
```
{
  "movie": {
    "id": 3,
    "release_date": "Sun, 01 NOV 2020 00:00:00 GMT",
    "title": "The Great Gatsby"
  },
  "success": true
}
```

#### PATCH '/actors/<int:id>'
- General:
    - Update some information of an actor based on a payload.
    - Roles authorized : Director, Producer.
- Example: ```curl -X PATCH - H '{"Content-Type: application/json", "Authorization: Bearer <TOKEN>}' -d '{"name": "", "age": 88, "": "M", "movie_id": }' http://127.0.0.1:5000/actors/3```
```
{
  "actor": {"age": 88,
    "gender": "M",
    "id": 3,
    "movie_id": 3,
    "name": "Leonardo DiCaprio"
  }, 
  "success": true
}
```

#### DELETE '/movis/<int:id>'
- General:
    - Deletes a movie by id form the url parameter.
    - Roles authorized : Executive Producer.
- Example: ```curl -H '{"Content-Type: application/json", "Authorization: Bearer <TOKEN>}' -X DELETE http://127.0.0.1:5000/movies/2```
```
{
  "success": true, 
  "delete": 2
}
```

#### DELETE '/actors/<int:id>'
- General:
    - Deletes a movie by id form the url parameter.
    - Roles authorized : Casting Director, Executive Producer.
- Example: ```curl -H '{"Content-Type: application/json", "Authorization: Bearer <TOKEN>}' -X DELETE http://127.0.0.1:5000/actors/2```
```
{
    "success": "True",
    "deleted": 2
}
```

### Error Handling
Errors are returned in the following json format:
```
{
    'success': False,
    'error': 404,
    'message': 'Resource not found. Input out of range.'
}
```
The API returns 6 types of errors:
- 400: bad request
- 404: not found
- 403: forbidden
- 422: unprocessable
- 500: internal server error
- AuthError: which mainly results in 401 (unauthorized)

## Author and Acknowledgement
- Linda Chen contributed everything in the project. 
- The image of the homepage used in this project is contributed to Alex Litvin on Unsplash
