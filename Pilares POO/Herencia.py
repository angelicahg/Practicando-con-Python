#tener dos o mas clases y que unas hereden a otras clases padres e hijas los metods del padre pasen a los hijos sin necesidad de colocarlos de nuevo  

class Animales():
    def habla(self):
        print("yo soy un animal")
    def decripcion(self):
        print("yo soy un {}".format(self.animal))



class Perro (Animales):
    pass

class Abeja(Animales):
    def __init__(self , animal):
        self.animal =animal

animal =Animales()
animal.habla()
perro =Perro()
perro.habla()