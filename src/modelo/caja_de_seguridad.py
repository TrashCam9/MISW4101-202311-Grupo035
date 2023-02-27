from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .declarative_base import Base

class CajaDeSeguridad(Base):

    __tablename__ = 'caja_de_seguridad'
    id = Column(Integer, primary_key=True)
    clave_maestra = Column(String, default='1234')

    def __getitem__(self, key):
        return getattr(self, key)