from select import select
from typing_extensions import Self


class A():
    def __init__(self):
        self._cuenta =0
        self._contador =0

    @property
    def cuenta (self):
        return self._cuenta

    @property
    def contador (self):
        return self._contador
  

a=A()
#se llama metodo no al atributo 

print(a.cuenta)
print(a.contador)