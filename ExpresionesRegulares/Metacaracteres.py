import re


lista_nombres = ["Angie Gonzalez","Camila Lopez", "Santiago Lopez", "Camila Perez"]
for elemento in lista_nombres:
        if re.findall("Lopez$" , elemento):
            print(elemento)