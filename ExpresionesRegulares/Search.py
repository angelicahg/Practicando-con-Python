import re

nombre = "Antonio Lopez"
nombre1 = "Camila Gomez"
nombre2 = "Antonio Gomez"

if re.search("Gomez", nombre1):
    print("si esta en nombre")
else:
    print("no esta")
    #busca si hay concidencias en toda la cadena de texto 
