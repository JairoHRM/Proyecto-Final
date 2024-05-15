import os
import helpers
import database as db


def iniciar():
    while True:
        helpers.limpiar_pantalla()
        
        print("=========================")
        print('Bienvenido al Gestor     ')
        print('=========================')
        print('[1] Listar los empleados ')
        print('[2] Buscar un empleado   ')
        print('[3] Añadir un empleado   ')
        print('[4] Modificar un empleado')
        print('[5] Borrar un empleado   ')
        print('[6] Cerrar el gestor     ')
        print("=========================")

        opcion = input('> ')
        helpers.limpiar_pantalla()

        if opcion == '1':
            print('Listado de los empleados...\n')
            for empleado in db.Empleados.lista:
                print(empleado)
            
        elif opcion == '2':
            print('Buscando un empleado...\n')
            id = helpers.leer_texto(3, 3, 'ID (2 int 1 char)').upper()
            empleado = db.Empleados.buscar(id)
            print(empleado) if empleado else print('Empleado no encontrado.')
                    
        elif opcion == '3':
            print('Añadiendo un empleado...\n')
            id = helpers.leer_texto(3, 3, 'ID (2 int 1 char)').upper()
            nombre = helpers.leer_texto(2, 30, 'Nombre de 2 a 30 chars').capitalize()
            salario = helpers.leer_texto(2, 30, 'valor numérico')
            db.Empleados.crear(id,nombre,salario)
            print('Empleado añadido correctamente.')
                    
        elif opcion == '4':
            print('Modificando un empleado...\n')
            id = helpers.leer_texto(3, 3, 'ID (2 int 1 char)').upper()
            empleado = db.Empleados.buscar(id)
            if empleado:
                nombre = helpers.leer_texto(
                    2,30, f'Nombre de 2 a 30 chars [{empleado.nombre}]').capitalize()
                salario = helpers.leer_texto(
                    2,30, f'Salario de 2 a 30 chars [{empleado.salario}]')
                db.Empleados.modificar(empleado.id,nombre,salario)
                print('Empleado modificado correctamente.')
            else:
                print('Empleado no encontrado.')
                
        elif opcion == '5':
            print('Borrando un empleado...\n')
            id = helpers.leer_texto(3, 3, 'ID (2 int 1 char)').upper()
            print('Empleado borrado correctamente.') if db.Empleados.borrar(id) else print('Empleado no encontrado.')
                   
        elif opcion == '6':
            print('Saliendo...\n')
            break 
        
        input('\nPresiona ENTER para continuar ....')
