﻿#Archivo de ejemplo para las pruebas unitarias.
#El nombre del archivo debe iniciar con el prefijo test_

#Importar unittest para crear las pruebas unitarias
import unittest

#Importar la clase Logica_mock para utilizarla en las pruebas
from src.logica.LogicaMock import Logica_mock

#Clase de ejemplo, debe tener un nombre que termina con el sufijo TestCase, y conservar la herencia
class ExampleTestCase(unittest.TestCase):

	#Instancia el atributo logica para cada prueba
	def setUp(self):
		self.logica = Logica_mock()

    	#Prueba para verificar que el caso funciona. El nombre del método usa el prefijo test_
	def test_nombre_claves_01(self):
		claves = self.logica.dar_claves_favoritas()
		self.assertEquals(claves[1]['nombre'], "Con fechas")
		
    	#Prueba para verificar que el caso funciona. El nombre del método usa el prefijo test_
	def test_nombre_claves_02(self):
		claves = self.logica.dar_claves_favoritas()
		self.assertEquals(claves[0]['nombre'], "La de siempre")

    	#Prueba para verificar que el caso funciona. El nombre del método usa el prefijo test_
	def test_nombre_claves_03(self):
		claves = self.logica.dar_claves_favoritas()
		self.assertEquals(claves[2]['nombre'], "Muy segura")
