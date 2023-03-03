import unittest

from faker import Faker

from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad
from src.modelo.clave import Clave
from src.modelo.declarative_base import Session

class ClaveTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.fachada = FachadaCajaDeSeguridad()
        self.session = Session()
        self.data_factory = Faker()

    def test_crear_clave_errada(self):
        self.assertRaises(ValueError, self.fachada.crear_clave, 123, 123, 123)

    def test_crear_clave(self):
        nombre_clave = self.data_factory.word()
        self.fachada.crear_clave(
            nombre=nombre_clave,
            clave=self.data_factory.password(),
            pista=self.data_factory.sentence())
        
        clave = self.session.query(Clave).filter(Clave.nombre == nombre_clave).first()
        self.assertNotEqual(clave, None)

    def test_generar_clave(self):
        clave = self.fachada.generar_clave()
        self.assertNotEqual(clave, None)
        self.assertTrue(len(clave) >= 8)
        self.assertTrue(len(clave.split(' ')) == 1)
        self.assertTrue(not clave.isalpha())
        self.assertTrue(not clave.islower())
        self.assertTrue(not clave.isalnum())

    def test_ver_claves_favoritas(self):
        claves = self.fachada.dar_claves_favoritas()
        self.assertIsNotNone(claves)
        self.assertIsInstance(claves, list)

    def tearDown(self):
        self.session.close()
