import unittest

from faker import Faker

from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad
from src.modelo.elemento import Elemento, ElementoConClave, Identificacion, Secreto
from src.modelo.declarative_base import session

class ElementoTestCase(unittest.TestCase):
    def setUp(self):
        self.session = session
        self.fachada = FachadaCajaDeSeguridad()
        self.data_factory = Faker()

    def test_dar_elementos(self):
        elementos = self.fachada.dar_elementos()
        self.assertIsNotNone(elementos)
        self.assertIsInstance(elementos, list)

    def test_eliminar_elemento_inexistente(self):
        self.assertRaises(ValueError, self.fachada.eliminar_elemento, 0)

    def test_eliminar_elemento_existente_sin_clave(self):
        # Crear un elemento para no modificar el estado de la base de datos
        identificacion = Identificacion(
            tipo='identificacion',
            nombre=self.data_factory.name(),
            nota=self.data_factory.sentence(),
            numero=self.data_factory.random_int(),
            nombreCompleto=self.data_factory.name(),
            fechaNacimiento = self.data_factory.date_of_birth(minimum_age=35, maximum_age=99),
            fechaExpedicion = self.data_factory.date_of_birth(minimum_age=24, maximum_age=35),
            fechaVencimiento = self.data_factory.date_of_birth(minimum_age=0, maximum_age=24)
        )
        self.session.add(identificacion)
        self.session.commit()

        # Verificamos que el elemento exista
        self.assertIsNotNone(session.query(Elemento).filter(Elemento.id == identificacion.id).first())

        # Eliminamos el elemento
        self.fachada.eliminar_elemento(identificacion.id)

        # Verificamos que no exista en ninguna tabla
        self.assertIsNone(session.query(Elemento).filter(Elemento.id == identificacion.id).first())
        self.assertIsNone(session.query(Identificacion).filter(Identificacion.id == identificacion.id).first())

    def test_eliminar_elemento_existente_con_clave(self):
        # Crear un elemento para no modificar el estado de la base de datos
        secreto = Secreto(
            tipo='secreto',
            nombre=self.data_factory.name(),
            nota=self.data_factory.sentence(),
            clave=self.data_factory.random_int(),
            secreto=self.data_factory.text()
        )
        self.session.add(secreto)
        self.session.commit()

        # Verificamos que el elemento exista
        self.assertIsNotNone(session.query(Elemento).filter(Elemento.id == secreto.id).first())

        # Eliminamos el elemento
        self.fachada.eliminar_elemento(secreto.id)

        # Verificamos que no exista en ninguna tabla
        self.assertIsNone(session.query(Elemento).filter(Elemento.id == secreto.id).first())
        self.assertIsNone(session.query(ElementoConClave).filter(ElementoConClave.id == secreto.id).first())
        self.assertIsNone(session.query(Secreto).filter(Secreto.id == secreto.id).first())


    def tearDown(self):
        self.session.close()


