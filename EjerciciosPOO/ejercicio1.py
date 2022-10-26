# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Estudiante():
    def __init__(self, nombre,nota):
        self.nombre =nombre
        self.nota =nota
    
    def imprimir(self):
        print("nombre:{}  Noota: {}".format(self.nmbre , self.nota))
    
    def resultados(self):
        if self.nota <7:
            print("has reprobado")
        else:
            print("has reprobado")

estudiante1=Estudiante("Camila", 10)
estudiante1.imprimir()
estudiante1.resultados()