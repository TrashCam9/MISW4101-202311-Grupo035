import unittest

from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad
from src.modelo.clave import Clave
from src.modelo.declarative_base import Session

class ClaveTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.fachada = FachadaCajaDeSeguridad()
        self.session = Session()

    def test_crear_clave_errada(self):
        self.assertRaises(ValueError, self.fachada.crear_clave, 123, 123, 123)

    def test_crear_clave(self):
        self.fachada.crear_clave('Clave bonita', 'HelloFromTheOtherSide', 'Lyrics de Hello - Adele')
        clave = self.session.query(Clave).filter(Clave.nombre == 'Clave bonita').first()
        self.assertNotEqual(clave, None)

    def test_generar_clave(self):
        clave = self.fachada.generar_clave()
        self.assertNotEqual(clave, None)
        self.assertTrue(len(clave) >= 8)
        self.assertTrue(len(clave.split(' ')) == 1)
        self.assertTrue(not clave.isalpha())
        self.assertTrue(not clave.islower())
        self.assertTrue(not clave.isalnum())