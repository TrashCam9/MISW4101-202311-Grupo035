import unittest

from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad
from src.modelo.elemento import Elemento
from src.modelo.declarative_base import Session

class ElementoTestCase(unittest.TestCase):
    def setUp(self):
        self.session = Session()
        self.fachada = FachadaCajaDeSeguridad()

    def test_dar_elementos(self):
        elementos = self.fachada.dar_elementos()
        self.assertIsNotNone(elementos)
        self.assertIsInstance(elementos, list)

    def tearDown(self):
        self.session.close()


