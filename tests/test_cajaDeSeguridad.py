import unittest
from src.modelo.caja_de_seguridad import CajaDeSeguridad
from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad
from src.modelo.declarative_base import Session

class CajaDeSeguridadTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.fachada = FachadaCajaDeSeguridad()

    def test_dar_claveMaestra_nula(self):
        self.assertIsNotNone(self.fachada.dar_claveMaestra())
        
