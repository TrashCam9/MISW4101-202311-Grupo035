from faker import Faker

from src.modelo.declarative_base import session
from src.modelo.clave import Clave
from src.modelo.elemento import Elemento, ElementoConClave

data_factory = Faker()

def give_unique_word():
    word = data_factory.unique.word()
    while session.query(Clave).filter(Clave.nombre == word).count() > 0:
        word = data_factory.unique.word()
    return word

def crear_clave():
    clave = Clave(nombre=give_unique_word(),
                  clave=data_factory.password(),
                  pista=data_factory.sentence())
    session.add(clave)
    session.commit()
    return clave
