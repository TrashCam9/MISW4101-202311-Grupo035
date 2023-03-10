from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .declarative_base import Base


class Elemento(Base):

    __tablename__ = 'elementos'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    nombre = Column(String)
    nota = Column(String)

    def __getitem__(self, key):
        return getattr(self, key)

class ElementoConClave(Elemento):

    __tablename__ = 'elementos_con_clave'
    id = Column(Integer, ForeignKey('elementos.id'), primary_key=True)
    clave = Column(Integer, ForeignKey('claves.id'))


class Identificacion(Elemento):

    __tablename__ = 'identificaciones'
    id = Column(Integer, ForeignKey('elementos.id'), primary_key=True)
    numero = Column(Integer)
    nombreCompleto = Column(String)
    fechaNacimiento = Column(Date)
    fechaExpedicion = Column(Date)
    fechaVencimiento = Column(Date)


class Login(ElementoConClave):

    __tablename__ = 'logins'
    id = Column(Integer, ForeignKey(
        'elementos_con_clave.id'), primary_key=True)
    usuario = Column(String)
    email = Column(String)
    url = Column(String)


class Secreto(ElementoConClave):

    __tablename__ = 'secretos'
    id = Column(Integer, ForeignKey(
        'elementos_con_clave.id'), primary_key=True)
    secreto = Column(String)


class Tarjeta(ElementoConClave):

    __tablename__ = 'tarjetas'
    id = Column(Integer, ForeignKey(
        'elementos_con_clave.id'), primary_key=True)
    numero = Column(Integer)
    titular = Column(String)
    fecha_vencimiento = Column(Date)
    codigo_seguridad = Column(Integer)
    direccion = Column(String)
    telefono = Column(Integer)
