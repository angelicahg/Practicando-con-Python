class FabricaTelefonos():
    def __init__(self, marca , color):
        self.marca=marca
        self.marca =color

    def __str__(self):
        return"el objeto es {} ".format(self.marca)
        
    def __del__(self):
      print("el objeto {} ha sido destruido".format(self.marca))

    
telefono = FabricaTelefonos("Nokia", "negro")
print(telefono.marca)
print(telefono)

 