#crear objetos que que usen el mismo metod pero el objeto es diferente 

class Animales():
    def __init__(self , mensaje):
        self.mensaje =mensaje

    def hablar(self):
        print(self.mensaje)

class Perro (Animales):
    def hablar(self):
        print("yo hago guauu!!")

class Pez (Animales):
    def hablar(self):
        print("yo no hablo")

perro =Perro("guau")
perro.hablar()

animal=Animales ("miua")
animal.hablar()

pez =Pez("nada")
pez.hablar()

