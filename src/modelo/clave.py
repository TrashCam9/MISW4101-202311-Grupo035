from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .declarative_base import Base


class Clave(Base):

    __tablename__ = 'claves'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)
    clave = Column(String)
    pista = Column(String)
    elementos = relationship(
        'ElementoConClave', cascade='all, delete, delete-orphan')

    def __getitem__(self, key):
        return getattr(self, key)