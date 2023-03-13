import unittest

from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad
from src.modelo.declarative_base import session
from src.modelo.elemento import Identificacion
from tests import testing_utils

class IdentificacionTestCase(unittest.TestCase):
    identificacionesList: "list[Identificacion]"
    
    def setUp(self):
        self.fachada = FachadaCajaDeSeguridad()
        self.data_factory = testing_utils.data_factory
        self.database_seeded = False

        if session.query(Identificacion).count() == 0:
            for _ in range(5):
                identificacion =Identificacion(tipo = "Identificacion",
                                               nombre = testing_utils.give_unique_word(Identificacion),
                                               nota = self.data_factory.sentence(),
                                               numero = int(self.data_factory.credit_card_number()),
                                               nombreCompleto = self.data_factory.name(),
                                               fechaNacimiento = self.data_factory.date_of_birth(minimum_age=35, maximum_age=99),
                                               fechaExpedicion = self.data_factory.date_of_birth(minimum_age=24, maximum_age=35),
                                               fechaVencimiento = self.data_factory.date_of_birth(minimum_age=0, maximum_age=24))
                session.add(identificacion)
            session.commit()
            self.database_seeded= True
        self.identificacionesList = session.query(Identificacion).all()

    def test_crear_identificación_con_parametros_incorrectos(self):
        test_cases = [
            (1, int(self.data_factory.credit_card_number()), self.data_factory.name(), self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24), self.data_factory.sentence()),
            (testing_utils.give_unique_word(Identificacion), "?", self.data_factory.name(), self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24), self.data_factory.sentence()),
            (testing_utils.give_unique_word(Identificacion), int(self.data_factory.credit_card_number()), 1, self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24), self.data_factory.sentence()),
            (testing_utils.give_unique_word(Identificacion), int(self.data_factory.credit_card_number()), self.data_factory.name(), "palabra", self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24), self.data_factory.sentence()),
            (testing_utils.give_unique_word(Identificacion), int(self.data_factory.credit_card_number()), self.data_factory.name(), self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), "palabra", self.data_factory.date_of_birth(minimum_age=0, maximum_age=24), self.data_factory.sentence()),
            (testing_utils.give_unique_word(Identificacion), int(self.data_factory.credit_card_number()), self.data_factory.name(), self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), "palabra", self.data_factory.sentence()),
            (testing_utils.give_unique_word(Identificacion), int(self.data_factory.credit_card_number()), self.data_factory.name(), self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24), 1)
        ]
        for params in test_cases:
            self.assertRaises(TypeError, self.fachada.crear_id, *params)
    
    def test_crear_identificacion_con_campos_de_texto_muy_cortos(self):
        unchangable_data = (self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24))
        number = int(self.data_factory.credit_card_number())
        test_cases = [
            ("aa", number, self.data_factory.name()) + unchangable_data + (self.data_factory.sentence(),),
            (testing_utils.give_unique_word(Identificacion), number, "aa") + unchangable_data + (self.data_factory.sentence(),),
            (testing_utils.give_unique_word(Identificacion), number, self.data_factory.name())+ unchangable_data + ("aa",),
        ]

        for params in test_cases:
            self.assertRaises(ValueError, self.fachada.crear_id, *params)

    def test_crear_identificacion_con_campos_de_texto_muy_largos(self):
        unchangable_data = (self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24))
        number = int(self.data_factory.credit_card_number())
        word_256 = testing_utils.generate_word_of_length(256)
        test_cases = [
            (word_256, number, self.data_factory.name()) + unchangable_data + (self.data_factory.sentence(),),
            (testing_utils.give_unique_word(Identificacion), number, word_256) + unchangable_data + (self.data_factory.sentence(),),
            (testing_utils.give_unique_word(Identificacion), number, self.data_factory.name())+ unchangable_data + (testing_utils.generate_word_of_length(513),),
        ]
        for params in test_cases:
            self.assertRaises(ValueError, self.fachada.crear_id, *params)
    
    def test_crear_identificacion_con_nombre_repetido(self):
        identificacion = self.identificacionesList[0]
        self.assertRaises(ValueError, self.fachada.crear_id, identificacion.nombre, int(self.data_factory.credit_card_number()), self.data_factory.name(), self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24), self.data_factory.sentence())

    def test_crear_identificacion(self):
        nombre = testing_utils.give_unique_word_of_length(Identificacion, 9)
        self.fachada.crear_id(nombre,
                            int(self.data_factory.credit_card_number()),
                            testing_utils.generate_word_of_length(25),
                            self.data_factory.date_of_birth(minimum_age=35, maximum_age=99),
                            self.data_factory.date_of_birth(minimum_age=24, maximum_age=35),
                            self.data_factory.date_of_birth(minimum_age=0, maximum_age=24),
                            testing_utils.generate_word_of_length(30))
        identificacion = session.query(Identificacion).filter(Identificacion.nombre == nombre).first()
        self.assertIsNotNone(identificacion)
        self.identificacionesList.append(identificacion)

    def test_editar_identificacion_inexistente(self):
        self.assertRaises(ValueError, self.fachada.editar_id, 0, 
                            testing_utils.give_unique_word(Identificacion),
                            int(self.data_factory.credit_card_number()),
                            self.data_factory.name(),
                            self.data_factory.date_of_birth(minimum_age=35, maximum_age=99),
                            self.data_factory.date_of_birth(minimum_age=24, maximum_age=35),
                            self.data_factory.date_of_birth(minimum_age=0, maximum_age=24),
                            self.data_factory.sentence())

    def test_editar_identificacion_con_nombre_repetido(self):
        identificacion = self.identificacionesList[0]
        self.assertRaises(ValueError, self.fachada.editar_id, identificacion.id, 
                            self.identificacionesList[1].nombre,
                            int(self.data_factory.credit_card_number()),
                            self.data_factory.name(),
                            self.data_factory.date_of_birth(minimum_age=35, maximum_age=99),
                            self.data_factory.date_of_birth(minimum_age=24, maximum_age=35),
                            self.data_factory.date_of_birth(minimum_age=0, maximum_age=24),
                            self.data_factory.sentence())
    
    def test_editar_identificacion_con_parametros_incorrectos(self):
        test_cases = [
            ("hola", testing_utils.give_unique_word(Identificacion), int(self.data_factory.credit_card_number()), self.data_factory.name(), self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24), self.data_factory.sentence()),
            (1, 1, int(self.data_factory.credit_card_number()), self.data_factory.name(), self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24), self.data_factory.sentence()),
            (1,testing_utils.give_unique_word(Identificacion), "?", self.data_factory.name(), self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24), self.data_factory.sentence()),
            (1,testing_utils.give_unique_word(Identificacion), int(self.data_factory.credit_card_number()), 1, self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24), self.data_factory.sentence()),
            (1,testing_utils.give_unique_word(Identificacion), int(self.data_factory.credit_card_number()), self.data_factory.name(), "palabra", self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24), self.data_factory.sentence()),
            (1,testing_utils.give_unique_word(Identificacion), int(self.data_factory.credit_card_number()), self.data_factory.name(), self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), "palabra", self.data_factory.date_of_birth(minimum_age=0, maximum_age=24), self.data_factory.sentence()),
            (1,testing_utils.give_unique_word(Identificacion), int(self.data_factory.credit_card_number()), self.data_factory.name(), self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), "palabra", self.data_factory.sentence()),
            (1,testing_utils.give_unique_word(Identificacion), int(self.data_factory.credit_card_number()), self.data_factory.name(), self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24), 1)
        ]
        for params in test_cases:
            self.assertRaises(TypeError, self.fachada.editar_id, *params)

    def test_editar_identificacion_con_campos_de_texto_muy_cortos(self):
        unchangable_data = (self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24))
        number = int(self.data_factory.credit_card_number())
        test_cases = [
            (self.identificacionesList[0].id,"aa", number, self.data_factory.name()) + unchangable_data + (self.data_factory.sentence(),),
            (self.identificacionesList[0].id,testing_utils.give_unique_word(Identificacion), number, "aa") + unchangable_data + (self.data_factory.sentence(),),
            (self.identificacionesList[0].id,testing_utils.give_unique_word(Identificacion), number, self.data_factory.name())+ unchangable_data + ("aa",),
        ]

        for params in test_cases:
            self.assertRaises(ValueError, self.fachada.editar_id, *params)

    def test_editar_identificacion_con_campos_de_texto_muy_largos(self):
        unchangable_data = (self.data_factory.date_of_birth(minimum_age=35, maximum_age=99), self.data_factory.date_of_birth(minimum_age=24, maximum_age=35), self.data_factory.date_of_birth(minimum_age=0, maximum_age=24))
        number = int(self.data_factory.credit_card_number())
        word_256 = testing_utils.generate_word_of_length(256)
        test_cases = [
            (self.identificacionesList[0].id, word_256, number, self.data_factory.name()) + unchangable_data + (self.data_factory.sentence(),),
            (self.identificacionesList[0].id,testing_utils.give_unique_word(Identificacion), number, word_256) + unchangable_data + (self.data_factory.sentence(),),
            (self.identificacionesList[0].id,testing_utils.give_unique_word(Identificacion), number, self.data_factory.name())+ unchangable_data + (testing_utils.generate_word_of_length(513),),
        ]
        for params in test_cases:
            self.assertRaises(ValueError, self.fachada.editar_id, *params)

    def test_editar_identificacion(self):
        nombre = testing_utils.give_unique_word_of_length(Identificacion, 9)
        numero = int(self.data_factory.credit_card_number())
        nombre_completo = testing_utils.generate_word_of_length(25)
        fnacimiento = self.data_factory.date_of_birth(minimum_age=35, maximum_age=99)
        fexpedicion = self.data_factory.date_of_birth(minimum_age=24, maximum_age=35)
        fvencimiento = self.data_factory.date_of_birth(minimum_age=0, maximum_age=24)
        self.fachada.editar_id(self.identificacionesList[0].id,
                            nombre,
                            numero,
                            nombre_completo,
                            fnacimiento,
                            fexpedicion,
                            fvencimiento,
                            testing_utils.generate_word_of_length(30))
        identificacion = session.query(Identificacion).filter(Identificacion.nombre == nombre).first()
        self.assertIsNotNone(identificacion)
        self.assertEqual(identificacion.numero, numero)
        self.assertEqual(identificacion.nombreCompleto, nombre_completo)
        self.assertEqual(identificacion.fechaNacimiento, fnacimiento)
        self.assertEqual(identificacion.fechaExpedicion, fexpedicion)
        self.assertEqual(identificacion.fechaVencimiento, fvencimiento)

    def test_editar_identificacion_con_mismo_nombre_que_antes(self):
        numero = int(self.data_factory.credit_card_number())
        nombre_completo = testing_utils.generate_word_of_length(25)
        fnacimiento = self.data_factory.date_of_birth(minimum_age=35, maximum_age=99)
        fexpedicion = self.data_factory.date_of_birth(minimum_age=24, maximum_age=35)
        fvencimiento = self.data_factory.date_of_birth(minimum_age=0, maximum_age=24)
        self.fachada.editar_id(self.identificacionesList[0].id,
                            self.identificacionesList[0].nombre,
                            numero,
                            nombre_completo,
                            fnacimiento,
                            fexpedicion,
                            fvencimiento,
                            testing_utils.generate_word_of_length(30))
        identificacion = session.query(Identificacion).filter(Identificacion.nombre == self.identificacionesList[0].nombre).first()
        self.assertIsNotNone(identificacion)
        self.assertEqual(identificacion.numero, numero)
        self.assertEqual(identificacion.nombreCompleto, nombre_completo)
        self.assertEqual(identificacion.fechaNacimiento, fnacimiento)
        self.assertEqual(identificacion.fechaExpedicion, fexpedicion)
        self.assertEqual(identificacion.fechaVencimiento, fvencimiento)


    def tearDown(self):
        if self.database_seeded:
            for identificacion in self.identificacionesList:
                session.delete(identificacion)
            session.commit()
            self.database_seeded = False
        session.close()