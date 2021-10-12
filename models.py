import  os
from flask_migrate import Migrate
from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json


db = SQLAlchemy()

DATABASE_URI = os.getenv('DATABASE_URI')

def setup_db(app, database_path=DATABASE_URI):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def setup_migrations(app):
    migrate = Migrate(app, db)


def create_and_drop_all():
    # db.drop_all()
    db.create_all()


MoviesAndActors = db.Table('MoviesAndActors',
    db.Column('Movie_id', db.Integer, db.ForeignKey('actor.id')),
    db.Column('Actor_id', db.Integer, db.ForeignKey('movie.id')),)

class Actor(db.Model):
    __tablename__ = 'actor'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    Movies = db.relationship("movie",secondary=MoviesAndActors,backref="actor", lazy="select")


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }

    def __repr__(self):
        return f'Actor: {self.id}, {self.name}'


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    release_date = db.Column(db.Date(), nullable=False)
    genre = db.Column(db.String(), nullable=False)
    actors = db.relationship("actor",secondary=MoviesAndActors,backref="movie", lazy="select")
   
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date.isoformat(),
            "genre": self.genre
        }

    def __repr__(self):
        return f'Movie:{self.id}, {self.title}'