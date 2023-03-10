import unittest

from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad

class ReporteDeSeguridadTestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.fachada = FachadaCajaDeSeguridad()
        return super().setUp()
    
    def test_retorna_diccionario(self):
        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte, dict)

    def test_llaves_correctas(self):
        # Debe tener las llaves: logins, ids, tarjetas, secretos, inseguras, avencer, masdeuna, nivel
        llaves = ['logins', 'ids', 'tarjetas', 'secretos', 'inseguras', 'avencer', 'masdeuna', 'nivel']
        reporte = self.fachada.dar_reporte_seguridad()
        for llave in llaves:
            self.assertIn(llave, reporte.keys())


    def tearDown(self) -> None:
        return super().tearDown()
