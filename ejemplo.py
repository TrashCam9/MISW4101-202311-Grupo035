from src.modelo.clave import Clave
from src.modelo.elemento import Elemento, ElementoConClave, Identificacion, Login, Secreto, Tarjeta
from src.modelo.declarative_base import Session, engine, Base
from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad

from datetime import date


if __name__ == '__main__':
    FachadaCajaDeSeguridad()

    session = Session()
    print("SESIÓN INICIADA")

    clave = Clave(clave='1234', pista='pista')
    session.add(clave)
    session.commit()

    print("CLAVE AGREGADA")

    login = Login(usuario='usuario', email='email', url='url', tipo='login',
                  clave=clave.id, nombre='mi login', nota='descripcion de mi login')
    session.add(login)
    session.commit()
    print("LOGIN AGREGADO")

    identificacion = Identificacion(nombre='Cedula', nota='Cedula de Cristobal', tipo='identificacion', numero=1000580058,
                                    nombreCompleto='Cristobal', fechaNacimiento=date(2003, 2, 17), fechaExpedicion=date(2021, 2, 18), fechaVencimiento=date(2025, 2, 18))
    session.add(identificacion)
    session.commit()
    print("IDENTIFICACION AGREGADA")

    session.close()
    print("SESIÓN CERRADA")

    claves = session.query(Clave).all()
    print("CLAVES")
    for clave in claves:
        print(f"Clave: {clave.id}, {clave.clave}, {clave.pista}")
        print("\t Elementos:")
        for elemento in clave.elementos:
            print(f"\t Elemento: {elemento.id}, {elemento.tipo}, {elemento.nombre}, {elemento.nota}")


    elementos = session.query(Elemento).all()
    print("ELEMENTOS")
    for elemento in elementos:
        print(
            f"Elemento: {elemento.id}, {elemento.tipo}, {elemento.nombre}, {elemento.nota}")

    elemtnos_con_clave = session.query(ElementoConClave).all()
    print("ELEMENTOS CON CLAVE")
    for elemento in elemtnos_con_clave:
        print(
            f"Elemento: {elemento.id}, {elemento.tipo}, {elemento.nombre}, {elemento.nota}, {elemento.clave}")
