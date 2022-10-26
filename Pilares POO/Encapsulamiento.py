# aplicar sobre los atributos un alcance para que cierto atributo solo sea utilizado dentro de la clase  

#en las clases las  funciones son metodos 

class A():
    def __init__(self):
        self.contador = 0

    def incremenar (self):
        self.contador +=1
    
    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self.__contador = 0

    def incremenar (self):
        self.__contador +=1
    
    def cuenta(self):
        return self.__contador

a=A()
print(a.cuenta())
a.incremenar()
print(a.cuenta())
print(a.contador)

b=B()
print(b.cuenta())
b.incremenar()
print(b.cuenta())
print(b.__contador)