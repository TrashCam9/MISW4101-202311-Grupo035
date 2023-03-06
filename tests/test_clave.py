import unittest

from faker import Faker

from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad
from src.modelo.clave import Clave
from src.modelo.declarative_base import session


class ClaveTestCase(unittest.TestCase):
    clavesList: "list[Clave]"

    def setUp(self) -> None:
        self.fachada = FachadaCajaDeSeguridad()
        self.data_factory = Faker()
        self.database_seeded = False

        # Crear 5 claves para las pruebas si no hay ninguna en la base de datos
        if session.query(Clave).count() == 0:
            for _ in range(5):
                clave = Clave(
                    nombre=self.data_factory.word(),
                    clave=self.data_factory.password(),
                    pista=self.data_factory.sentence(),
                )
                session.add(clave)
            session.commit()
            self.database_seeded = True
        self.clavesList = session.query(Clave).all()

    def test_crear_clave_errada(self):
        self.assertRaises(TypeError, self.fachada.crear_clave, 123, 123, 123)

    def test_crear_clave(self):
        nombre_clave = self.data_factory.word()
        self.fachada.crear_clave(
            nombre=nombre_clave,
            clave=self.data_factory.password(),
            pista=self.data_factory.sentence())

        clave = session.query(Clave).filter(
            Clave.nombre == nombre_clave).first()
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

    def test_editar_clave_que_no_existe(self):
        self.assertRaises(ValueError,
                          self.fachada.editar_clave,
                              nombre="Mi Clave Favorita Que Claramento No Existe",
                              clave="12345678",
                              pista="Mi pista favorita"
                          )

    def test_editar_clave_con_campos_errados(self):
        clave = self.clavesList[0]
        self.assertRaises(TypeError,
                          self.fachada.editar_clave,
                              nombre=clave.nombre,
                              clave=123,
                              pista=123
                          )

    def test_editar_clave_nombre_incorrecto(self):
        self.assertRaises(TypeError,
                          self.fachada.editar_clave,
                              nombre=15,
                              clave="12345678",
                              pista="Mi pista favorita"
                          )
    
    def test_editar_clave_campos_vacios(self):
        clave = self.clavesList[0]
        self.assertRaises(ValueError,
                          self.fachada.editar_clave,
                              nombre=clave.nombre,
                              clave="",
                              pista=""
                          )

    def test_editar_todos_los_campos_de_la_clave(self):
        clave = self.clavesList[0]
        self.fachada.editar_clave(
            nombre=clave.nombre,
            clave="12345678",
            pista="Mi pista favorita")

        claveGuardada = session.query(
            Clave).filter(Clave.nombre == clave.nombre).first()
        self.assertEqual(claveGuardada.clave, "12345678")
        self.assertEqual(claveGuardada.pista, "Mi pista favorita")


    def tearDown(self):
        # Eliminar las claves creadas en el setUp
        if self.database_seeded:
            for clave in self.clavesList:
                session.delete(clave)
            session.commit()
        session.close()
