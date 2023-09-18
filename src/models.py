import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column (String(250), nullable=False)
    gender = Column (String(250), nullable=True)
    image = Column (String(250), nullable=False)
    favoritos = relationship("Favorito")

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column (String(250), nullable=False)
    image = Column (String(250), nullable=False)
    favoritos = relationship("Favorito")

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    mail = Column (String(250), nullable=False)
    password = Column (String(250), nullable=False)
    favoritos = relationship("Favorito")

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    id_personaje = Column(Integer, ForeignKey('personaje.id'))
    id_planeta = Column(Integer, ForeignKey('planeta.id'))
    id_usuario = Column(Integer, ForeignKey('usuario.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
