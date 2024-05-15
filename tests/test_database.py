import copy
import unittest
import database as db


class testDatabase(unittest.TestCase):

    def setUp(self):
        db.Empleados.lista = [
            db.Empleado('15J','Marta','1000'),
            db.Empleado('13G','Mario','2000'),
            db.Empleado('16Y','Antonio','1500'),
            db.Empleado('18S','Sandra','1050'),
        ]

    def test_buscar_empleado(self):
        empleado_existente = db.Empleados.buscar('15J')
        empleado_inexistente = db.Empleados.buscar('13J')
        self.assertIsNotNone(empleado_existente)
        self.assertIsNone(empleado_inexistente)

    def test_crear_empleado(self):
        nuevo_empleado = db.Empleados.crear('39X', 'Hector', '2234')
        self.assertEqual(len(db.Empleados.lista),5)
        self.assertEqual(nuevo_empleado.id, '39X')
        self.assertEqual(nuevo_empleado.nombre, 'Hector')
        self.assertEqual(nuevo_empleado.salario, '2234')
    
    def test_modificar_empleado(self):
        empleado_a_modificar = copy.copy(db.Empleados.buscar('18S'))
        empleado_modificado = db.Empleados.modificar('18S', 'Sandra', '1050')
        self.assertEqual(empleado_a_modificar.salario, '1050')
        self.assertEqual(empleado_modificado.salario, '1050')

    def test_borrar_empleado(self):
        empleado_borrado = db.Empleados.borrar('16Y')
        empleado_rebuscado = db.Empleados.buscar('16Y')
        self.assertEqual(empleado_borrado.id,'16Y')
        self.assertIsNone(empleado_rebuscado)