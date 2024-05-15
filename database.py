class Empleado:
    def __init__ (self,id,nombre,salario):
        self.id = id
        self.nombre = nombre
        self.salario = salario

    def __str__ (self):
        return f"({self.id}) {self.nombre} {self.salario}"
    

class Empleados:

    lista = []

    @staticmethod
    def buscar(id):
        for empleado in Empleados.lista:
            if empleado.id == id:
                return empleado
            
    @staticmethod
    def crear (id,nombre,salario):
        empleado = Empleado(id,nombre,salario)
        Empleados.lista.append(empleado)
        return empleado
    
    @staticmethod
    def modificar (id,nombre,salario):
        for indice, empleado in enumerate(Empleados.lista):
            if empleado.id == id:
                Empleados.lista[indice].nombe = nombre
                Empleados.lista[indice].salario = salario
                return Empleados.lista[indice]
            
    @staticmethod
    def borrar(id):
        for indice, empleado in enumerate(Empleados.lista):
            if empleado.id == id:
                return Empleados.lista.pop(indice)