from faker import Faker

from src.modelo.declarative_base import session
from src.modelo.clave import Clave
from src.modelo.elemento import Login, Identificacion

from datetime import date

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


def crear_5_logins_aleatorios(clave: Clave):
    for _ in range(5):
        login = Login(tipo = "login",
                        nombre = data_factory.word(),
                        nota = data_factory.sentence(),
                        clave = clave.id,
                        usuario = data_factory.user_name(),
                        email = data_factory.email(),
                        url = data_factory.url())
        session.add(login)
    session.commit()

def crear_5_identificacioens_aleatorias():
    for _ in range(5):
        fecha_nacimiento = date(*map(int, data_factory.date().split("-")))
        fecha_expedicion = fecha_nacimiento.replace(year=fecha_nacimiento.year + 18)
        fecha_vencimiento = fecha_expedicion.replace(year=fecha_expedicion.year + 10)
        identificacion = Identificacion(tipo = "identificacion",
                                        nombre = data_factory.word(),
                                        nota = data_factory.sentence(),
                                        numero = data_factory.random_int(),
                                        nombreCompleto = data_factory.name(),
                                        fechaNacimiento = fecha_nacimiento,
                                        fechaExpedicion = fecha_expedicion,
                                        fechaVencimiento = fecha_vencimiento)
        session.add(identificacion)
    session.commit()