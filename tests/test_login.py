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

    def test_editar_login_con_parametros_incorrectos(self):
        test_cases = [
            ("0", self.data_factory.domain_word(), self.data_factory.email(), self.data_factory.user_name(), self.clave.nombre, self.data_factory.url(), self.data_factory.sentence()),
            (1, 1, self.data_factory.email(), self.data_factory.user_name(), self.clave.nombre, self.data_factory.url(), self.data_factory.sentence()),
            (1, self.data_factory.domain_word(), 1, self.data_factory.user_name(), self.clave.nombre, self.data_factory.url(), self.data_factory.sentence()),
            (1, self.data_factory.domain_word(), self.data_factory.email(), 1, self.clave.nombre, self.data_factory.url(), self.data_factory.sentence()),
            (1, self.data_factory.domain_word(), self.data_factory.email(), self.data_factory.user_name(), 1, self.data_factory.url(), self.data_factory.sentence()),
            (1, self.data_factory.domain_word(), self.data_factory.email(), self.data_factory.user_name(), self.clave.nombre, 1, self.data_factory.sentence()),
            (1, self.data_factory.domain_word(), self.data_factory.email(), self.data_factory.user_name(), self.clave.nombre, self.data_factory.url(), 1)
        ]
        for params in test_cases:
            self.assertRaises(TypeError, self.fachada.editar_login, *params)

    def test_editar_login_inexistente(self):
        self.assertRaises(ValueError, self.fachada.editar_login,
                          0,
                          self.data_factory.domain_word(),
                          self.data_factory.email(),
                          self.data_factory.user_name(),
                          self.clave.nombre,
                          self.data_factory.url(),
                          self.data_factory.sentence())

    def test_editar_parametros_login(self):
        # Crear un login para editar y no modificar los datos existentes
        login = Login(tipo="login",
                      nombre="Login de prueba",
                      nota="Nota de prueba",
                      clave=self.clave.nombre,
                      usuario=self.data_factory.user_name(),
                      email=self.data_factory.email(),
                      url=self.data_factory.url())
        session.add(login)
        session.commit()

        # Editar el login
        nuevo_nombre = self.data_factory.domain_word()
        nuevo_email = self.data_factory.email()
        nuevo_usuario = self.data_factory.user_name()
        nueva_url = self.data_factory.url()
        nueva_nota = self.data_factory.sentence()
        self.fachada.editar_login(login.id,
                                    nuevo_nombre,
                                    nuevo_email,
                                    nuevo_usuario,
                                    self.clave.nombre,
                                    nueva_url,
                                    nueva_nota)
        
        # Verificar que los datos fueron modificados
        login = session.query(Login).filter(Login.id == login.id).first()
        self.assertEqual(login.nombre, nuevo_nombre)
        self.assertEqual(login.email, nuevo_email)
        self.assertEqual(login.usuario, nuevo_usuario)
        self.assertEqual(login.url, nueva_url)
        self.assertEqual(login.nota, nueva_nota)

    def test_editar_clave_inexistente_login(self):
        # Crear un login para editar y no modificar los datos existentes
        login = Login(tipo="login",
                      nombre="Login de prueba",
                      nota="Nota de prueba",
                      clave=self.clave.nombre,
                      usuario=self.data_factory.user_name(),
                      email=self.data_factory.email(),
                      url=self.data_factory.url())
        session.add(login)
        session.commit()

        # Editar el login
        self.assertRaises(ValueError, self.fachada.editar_login,
                          login.id,
                          login.nombre,
                          login.email,
                          login.usuario,
                          "Clave inexistente",
                          login.url,
                          login.nota)
