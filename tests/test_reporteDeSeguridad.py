import unittest

from src.modelo.declarative_base import session

from src.modelo.elemento import Login
from src.modelo.clave import Clave

from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad

from tests import testing_utils

class ReporteDeSeguridadTestCase(unittest.TestCase):
    listaLogins: "list[Clave]" = []

    def setUp(self) -> None:
        self.fachada = FachadaCajaDeSeguridad()    
        self.session = session   
        self.data_factory = testing_utils.data_factory                 

        return super().setUp()
    
    def test_retorna_diccionario(self):
        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte, dict)

    def test_llaves_correctas(self):
        llaves = ['logins', 'ids', 'tarjetas', 'secretos', 'inseguras', 'avencer', 'masdeuna', 'nivel']
        reporte = self.fachada.dar_reporte_seguridad()
        for llave in llaves:
            self.assertIn(llave, reporte.keys())

    def test_num_logins(self):
        listaLogins = []
        clave = Clave(nombre = testing_utils.give_unique_word(),
                      clave = testing_utils.data_factory.password(),  
                      pista = testing_utils.data_factory.sentence())
        session.add(clave)
        session.commit()
        
        for _ in range(5):
            login = Login(tipo = "login",
                          nombre = self.data_factory.word(),
                          nota = self.data_factory.sentence(),
                          clave = clave.id,
                          usuario = self.data_factory.user_name(),
                          email = self.data_factory.email(),
                          url = self.data_factory.url())
            session.add(login)
            listaLogins.append(login)
        session.commit()

        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte['logins'], int)
        self.assertEqual(reporte['logins'], len(listaLogins))


    def tearDown(self) -> None:
        return super().tearDown()
