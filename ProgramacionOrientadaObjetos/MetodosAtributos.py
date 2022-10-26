#los metod son funciones pero en el POO pasan a llamarse metodos 
#los atributos son caracteristicas cualidades o descripciones que tiene los onbjetos
#los metods van a las clases los atributos a los objetos es una accion

from re import T


class FabricaTelefonos():
    marca ="Huawei"
    color="negro"
    memoria = 32
    alamcenamiento =128

    def llamar(self , mensaje):
        return mensaje 


telefono = FabricaTelefonos()
telefono.marca
telefono.color
print(telefono.marca)
print(telefono.llamar("hola con quien hablo"))
