import unittest

from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad
from src.modelo.elemento import Login
from src.modelo.clave import Clave
from src.modelo.declarative_base import session

from tests import testing_utils

class LoginTestCase(unittest.TestCase):
    loginsList: "list[Login]"
    clave: "Clave"
 
    def setUp(self):
        self.fachada = FachadaCajaDeSeguridad()
        self.data_factory = testing_utils.data_factory
        self.database_seeded = False

        self.clave = Clave(nombre = testing_utils.give_unique_word(),
                          clave = self.data_factory.password(),
                          pista = self.data_factory.sentence())
        session.add(self.clave)
        session.commit()

        if session.query(Login).count() == 0:
            
            for i in range(5):
                login = Login(tipo = "Login",
                              nombre = self.data_factory.word(),
                              nota = self.data_factory.sentence(),
                              clave = self.clave.id,
                              usuario = self.data_factory.user_name(),
                              email = self.data_factory.email(),
                              url = self.data_factory.url())
                session.add(login)
 
            session.commit()
            self.database_seeded= True

            self.loginsList = session.query(Login).all()


    def tearDown(self):
        
        session.close()

    def test_crear_login(self):
        nombre = self.data_factory.word() + self.data_factory.word()
        self.fachada.crear_login(nombre,
                                 self.data_factory.email(),
                                 self.data_factory.user_name(),
                                 self.clave.nombre,
                                 self.data_factory.url(),
                                 self.data_factory.sentence())
        self.assertIsNot(len(session.query(Login).filter(Login.nombre == nombre).all()), 0)

    def test_crear_login_con_clave_inexistente(self):
        self.assertRaises(ValueError, self.fachada.crear_login, 
                          self.data_factory.domain_word(), 
                          self.data_factory.email(),
                          self.data_factory.user_name(),
                          "",
                          self.data_factory.url(),
                          self.data_factory.sentence())

    def test_crear_login_con_parametros_incorrectos(self):
        test_cases = [
            (1, self.data_factory.email(), self.data_factory.user_name(), self.clave.nombre, self.data_factory.url(), self.data_factory.sentence()),
            (self.data_factory.domain_word(), 1, self.data_factory.user_name(), self.clave.nombre, self.data_factory.url(), self.data_factory.sentence()),
            (self.data_factory.domain_word(), self.data_factory.email(), 1, self.clave.nombre, self.data_factory.url(), self.data_factory.sentence()),
            (self.data_factory.domain_word(), self.data_factory.email(), self.data_factory.user_name(), 1, self.data_factory.url(), self.data_factory.sentence()),
            (self.data_factory.domain_word(), self.data_factory.email(), self.data_factory.user_name(), self.clave.nombre, 1, self.data_factory.sentence()),
            (self.data_factory.domain_word(), self.data_factory.email(), self.data_factory.user_name(), self.clave.nombre, self.data_factory.url(), 1)
        ]
        for params in test_cases:
            self.assertRaises(TypeError, self.fachada.crear_login, *params)
