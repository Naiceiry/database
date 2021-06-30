import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class FavoritePlanets(Base):
    __tablename__ = 'FavoritePlanets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_id = Column(String(250))
    iduser = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer(250))
    rotation_period = Column(Integer(250))
    orbital_period = Column(Integer(250))
    gravity = Column(Integer(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer(250))
    created = Column(String(250))
    edited = Column(String(250))
    name= Column(String(250))
    url= Column(String(250))
    user_id = Column(Integer, ForeignKey('FavoritePlanets.id'))
    user = relationship(FavoritePlanets)

class FavoriteCharacters(Base):
    __tablename__ = 'FavoriteCharacters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_id = Column(String(250))
    iduser = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    height= Column(Integer(250))
    mass= Column(Integer(250))
    hair_color= Column(String(250))
    skin_color= Column(String(250))
    eye_color= Column(String(250))
    birth_year= Column(String(250))
    gender= Column(String(250))
    created= Column(String(250))
    edited= Column(String(250))
    name= Column(String(250))
    homeworld= Column(String(250))
    url= Column(String(250))
    user_id = Column(Integer, ForeignKey('FavoriteCharacters.id'))
    user = relationship(FavoriteCharacters)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')