import random
import string
from faker import Faker
from src.modelo.clave import Clave
from src.modelo.elemento import ElementoConClave, Login, Identificacion, Secreto, Tarjeta

from datetime import date, timedelta

from src.modelo.declarative_base import session

data_factory = Faker()

def give_unique_word(obj):
    word = data_factory.unique.word()
    while session.query(obj).filter(obj.nombre == word).count() > 0:
        word = data_factory.unique.word()
    return word

def give_unique_word_of_length(obj, n):
    word = generate_word_of_length(n)
    while session.query(obj).filter(obj.nombre == word).count() > 0:
        word = generate_word_of_length(n)
    return word

def generate_word_of_length(n):
    return ''.join(random.choices(string.ascii_letters, k=n))

def crear_clave(segura: bool = False):
    password = data_factory.word()
    if segura:
        password = "?aA1;bB2"
    
    clave = Clave(nombre=give_unique_word(Clave),
                  clave=password,
                  pista=data_factory.sentence())
    session.add(clave)
    session.commit()
    return clave

def crear_elemento_con_clave(clave: Clave):
    elemento = ElementoConClave(tipo = "elemento_prueba", 
                                clave = clave.nombre,
                                nombre = give_unique_word(ElementoConClave),
                                nota = data_factory.sentence())
    session.add(elemento)
    session.commit()
    return elemento

def crear_5_logins_aleatorios(clave: Clave):
    for _ in range(5):
        login = Login(tipo="login",
                      nombre=give_unique_word(Login),
                      nota=data_factory.sentence(),
                      clave=clave.nombre,
                      usuario=data_factory.user_name(),
                      email=data_factory.email(),
                      url=data_factory.url())
        session.add(login)
    session.commit()


def crear_5_identificacioens_aleatorias():
    for _ in range(5):
        fecha_nacimiento = date(*map(int, data_factory.date().split("-")))
        fecha_expedicion = fecha_nacimiento.replace(
            year=fecha_nacimiento.year + 18)
        fecha_vencimiento = fecha_expedicion.replace(
            year=fecha_expedicion.year + 10)
        identificacion = Identificacion(tipo="identificacion",
                                        nombre=give_unique_word(Identificacion),
                                        nota=data_factory.sentence(),
                                        numero=data_factory.random_int(),
                                        nombreCompleto=data_factory.name(),
                                        fechaNacimiento=fecha_nacimiento,
                                        fechaExpedicion=fecha_expedicion,
                                        fechaVencimiento=fecha_vencimiento)
        session.add(identificacion)
    session.commit()


def crear_5_tarjetas_aleatorias(clave: Clave):
    for _ in range(5):
        fecha_vencimiento = date(*map(int, data_factory.date().split("-")))
        tarjeta = Tarjeta(tipo="tarjeta",
                          nombre=give_unique_word(Tarjeta),
                          nota=data_factory.sentence(),
                          clave=clave.nombre,
                          numero=data_factory.random_int(),
                          titular=data_factory.name(),
                          fecha_vencimiento=fecha_vencimiento,
                          codigo_seguridad=data_factory.random_int(),
                          direccion=data_factory.address(),
                          telefono=data_factory.phone_number())
        session.add(tarjeta)
    session.commit()


def crear_5_secretos_aleatorios(clave: Clave):
    for _ in range(5):
        secreto = Secreto(tipo="secreto",
                          nombre=give_unique_word(Secreto),
                          nota=data_factory.sentence(),
                          clave=clave.nombre,
                          secreto=data_factory.sentence())
        session.add(secreto)
    session.commit()


def verificar_clave_segura(clave: str) -> bool:
    return len(clave) >= 8 and ' ' not in clave and any(char.isdigit() for char in clave) and any(char.isupper() for char in clave) and any(char.islower() for char in clave) and any(char in "?-*!@#$/(){}=.,;:" for char in clave)

def verificar_vencimiento(fecha_vencimiento: date) -> bool:
    return fecha_vencimiento < (date.today() + timedelta(days=30))

