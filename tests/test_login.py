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

        if len(session.query(Clave).all()) == 0:
            self.clave = testing_utils.crear_clave()
        else:
            self.clave = session.query(Clave).first()

        if session.query(Login).count() == 0:
            testing_utils.crear_5_logins_aleatorios(self.clave)
            self.database_seeded= True

        self.loginsList = session.query(Login).all()


    def tearDown(self):
        if self.database_seeded:
            for login in self.loginsList:
                session.delete(login)
            session.commit()
        session.close()

    def test_crear_login(self):
        nombre = testing_utils.give_unique_word(Login)
        self.fachada.crear_login(nombre,
                                 self.data_factory.email(),
                                 self.data_factory.user_name(),
                                 self.clave.nombre,
                                 self.data_factory.url(),
                                 self.data_factory.sentence())
        self.assertIsNot(len(session.query(Login).filter(Login.nombre == nombre).all()), 0)
        self.loginsList.append(session.query(Login).filter(Login.nombre == nombre).first())

    def test_crear_login_con_clave_inexistente(self):
        self.assertRaises(ValueError, self.fachada.crear_login, 
                          testing_utils.give_unique_word(Login), 
                          self.data_factory.email(),
                          self.data_factory.user_name(),
                          "",
                          self.data_factory.url(),
                          self.data_factory.sentence())

    def test_crear_login_con_parametros_incorrectos(self):
        test_cases = [
            (1, self.data_factory.email(), self.data_factory.user_name(), self.clave.nombre, self.data_factory.url(), self.data_factory.sentence()),
            (testing_utils.give_unique_word(Login), 1, self.data_factory.user_name(), self.clave.nombre, self.data_factory.url(), self.data_factory.sentence()),
            (testing_utils.give_unique_word(Login), self.data_factory.email(), 1, self.clave.nombre, self.data_factory.url(), self.data_factory.sentence()),
            (testing_utils.give_unique_word(Login), self.data_factory.email(), self.data_factory.user_name(), 1, self.data_factory.url(), self.data_factory.sentence()),
            (testing_utils.give_unique_word(Login), self.data_factory.email(), self.data_factory.user_name(), self.clave.nombre, 1, self.data_factory.sentence()),
            (testing_utils.give_unique_word(Login), self.data_factory.email(), self.data_factory.user_name(), self.clave.nombre, self.data_factory.url(), 1)
        ]
        for params in test_cases:
            self.assertRaises(TypeError, self.fachada.crear_login, *params)
