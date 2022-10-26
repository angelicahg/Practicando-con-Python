# Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

class Fabrica ():
    def __init__(self,llantas,color,precio):
        self.llantas=llantas
        self.color= color
        self.precio=precio

class Carro(Fabrica):
    def datos(self):
        print ("la cantidad de llantas esd de: ",self.llantas)
        print ("el color del carro  esd de: ",self.color)
        print ("el precio del carro esd de: ",self.precio)

class Moto(Fabrica):
    def datos(self):
        print ("la cantidad de llantas de la moto esd de: ",self.llantas)
        print ("el color del moto  esd de: ",self.color)
        print ("el precio de la moto esd de: ",self.precio)

moto=Moto (2, "negro", 5000)
moto.datos()

carro =Carro(5, "Azul", 6000)
carro.datos()