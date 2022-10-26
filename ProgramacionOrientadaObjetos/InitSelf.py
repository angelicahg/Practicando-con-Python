class FabricaTelefonos ():
    marca = "samsung"

    def ElaborarHuawei(self):
        self.marca ="Huawai"

telefono = FabricaTelefonos()
telefono.ElaborarHuawei()
print(telefono.marca)

#init sirve para ser el constructr de una clase (primer metodo que se ejecuta al construir una clase)  

class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca =marca
        self.color=color
telefono= FabricaTelefonos("huawai", "Azul")
print(telefono.marca)
print(telefono.color)

