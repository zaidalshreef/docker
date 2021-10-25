# Casting Agency API 
 

### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 
  This will install all of the required packages we selected within the `requirements.txt` file.



## Running the server

From within the directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
. ./setup.sh
flask run
```

#### Flask run tests the token headers set for the enviroment. If they have expired, you need to login using the crededntials below and replace them in setup.sh and run setup.sh again

setup.sh has all the environment variables needed for the project. The app may fail if they are not set properly. If that happens just copy paste lines from setup.sh on you CLI.

# Project deployed at

https://fsnd-casting-agency-udacity.herokuapp.com/

###### To test live APIs the only way right now to do this is curl requests. Add Auth token headers from logins below to test.

OATH login url. There are three logins atm, JWTs for these appear in the url after successfull login. Those tokens are needed to test the different APIs.


https://dev-fc34y9lq.us.auth0.com/authorize?audience=CastingAgencyAPI&response_type=token&client_id=XeqwOu6PsAeC0bwm2dd6giNP0JJaaxIe&redirect_uri=http://localhost:8080/login-results


casting Assistant token castingassistant@example.com Qwerty1234

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJWRXNSUnYwWUZRUDdtU3g5VGJ0TSJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYzM0eTlscS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyMjAzYzNjMTNiMTMwMjI4ZjgxM2FhIiwiYXVkIjoiQ2FzdGluZ0FnZW5jeUFQSSIsImlhdCI6MTU5NjE0MTQ2NSwiZXhwIjoxNTk2MjI3ODY0LCJhenAiOiJYZXF3T3U2UHNBZUMwYndtMmRkNmdpTlAwSkphYXhJZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.U39-EK_wkLbqrUnfsTWb7ih1Djn9L30GwdZwanfKVNyXIsa9BDcxd5yUxH8HD_owfAZWxcqqf2hCjJ_wcQDhuFD_Z8jDYvECtFx_KYWncmf2P4vhm_mNf6ENS2Hi2nNUV6YE7X4Mv3rsktI3GrZFppiMVKfNODRf3EbfAOw5VwqQCE8u3Paiurfyoya7frltSOeuf8pU6o3hVkJXwPSlnpN6Rvos_JL1JvodoZFJQJmtWn4CObJ-Nut-17aFjH1gm9ZsZzUfq-ECfcD74e7RKU28y_Rw_0BS6nFO9OVFVJGHuT3JyoCfxfuneNr5Ao6RYedGBqAw4R5l6TtQuxKQhw

```

Casting director token castingdirector@example.com Qwerty1234

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJWRXNSUnYwWUZRUDdtU3g5VGJ0TSJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYzM0eTlscS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyMjA2MjI1Yzg0OGYwMDM3YzQxNTJmIiwiYXVkIjoiQ2FzdGluZ0FnZW5jeUFQSSIsImlhdCI6MTU5NjE0MTU2MCwiZXhwIjoxNTk2MjI3OTU5LCJhenAiOiJYZXF3T3U2UHNBZUMwYndtMmRkNmdpTlAwSkphYXhJZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9ycyIsImRlbGV0ZTphY3RvcnMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.Zf0BsuoZdBFrkHjIEuPDW5Udt6aJn6qUMWIDpOaoTBxhALV2wRt1aV9qMn9PHihG8RZ_N8rEjpOm6AJGzT-MsDfKUTuF0Ah7CAME8hJ_AdWR0egsjoqb7bosn-cu6VSQNtb7O039dOgm0uX23G95nrbobbfeLg8S3ipSmsyO3IB1B78ebV2NCM8J64DXMCsQwvkJl4OKsNjc0nzxBk6fcjVVkUfftZJW45V6H-NU8Ljc15At1lxQ4SRbdQ3AEpH9lbptCKpKGY-QdAeEgD_gP3uffJbIGfjPEDWy-NMRTt-2ika134hnDvTXEspALVAKHchcp6pRw9pMr8LFmRvLPA

```

Executive Producer executiveproducer@example.com Qwerty1234

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJWRXNSUnYwWUZRUDdtU3g5VGJ0TSJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYzM0eTlscS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyMjRkNGQ1Yzg0OGYwMDM3YzQxNzFkIiwiYXVkIjoiQ2FzdGluZ0FnZW5jeUFQSSIsImlhdCI6MTU5NjE0MTUwNCwiZXhwIjoxNTk2MjI3OTAzLCJhenAiOiJYZXF3T3U2UHNBZUMwYndtMmRkNmdpTlAwSkphYXhJZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9ycyIsImFkZDptb3ZpZXMiLCJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.BgIe6xAaR5YqxM7j0NFjjLLctZnAKIp2x_q93sZPH8rBkCp3HjSDRLlqmz0KyeEwPyBMjLxQabbr3InJQk8OTq8S7rjoepgPs_zHF3mJrjUqZ3V3JaRX5_IvDf5J_-PfV-I6vxz42q1Mb1wMTBOHxOxj7MvtZ0JSycNGy3aRg1h0RsslV1Zyrcsx5cWk6xstpBylBEhaOTwbqHQTWZklWDE2eRnRAC3YYWrHpIy_xepcn8HNxfBoIFWr11SYxGMkYXEMqRDbQ8UqnUcUpOzxqMJXG913cf9YZegljhEiyZwPtsdlW92KNLNYKkLEPbTPXBwEQl_UmsD769fKc_egvA
```


## Testing
To run the tests, run 
```
dropdb casting_test
createdb casting_test
psql casting_test < casting.pgsql
python test_app.py
```

To run tests using Heroku endpoints, run in postman

```
casting-agency.postman_collection.json
```




## API Reference

### Endpoints

GET '/actors'
POST '/actors'
PATCH '/actors/id'
DELETE '/actors/id'
GET '/movies'
POST '/movies'
PATCH '/movies/id'
DELETE '/movies/id'





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

