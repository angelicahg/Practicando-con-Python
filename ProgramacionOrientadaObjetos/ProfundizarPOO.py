class FabricaTelefonos():
    def __init__(self , marca, *colores , **modelos):
        self.marca =marca
        self.colores=colores
        self.modeos =modelos

telefono =FabricaTelefonos("alcatel","negro","rojo", m1=500, m2=100)
print (telefono.marca)
print (telefono.colores)
print (telefono.modeos)
telefono.memoria =512
print (telefono.memoria)
