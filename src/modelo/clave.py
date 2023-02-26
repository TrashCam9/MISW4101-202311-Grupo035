from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base


class Clave(Base):

    __tablename__ = 'claves'
    id = Column(Integer, primary_key=True)
    clave = Column(String)
    pista = Column(String)
    elementos = relationship(
        'ElementoConClave', cascade='all, delete, delete-orphan')
