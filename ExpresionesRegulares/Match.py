import re

nombre = "Antonio Lopez"
nombre1 = "Camila Gomez"
nombre2 = "Antonio Gomez"

if re.match("Antonio", nombre):
    print("si esta en nombre")
else:
    print("no esta")

cadena1 = "Antonio Lopez"
cadena2 = "1334565662"
cadena3 = "a111112644"

if re.match("\d", cadena1):
    print("si esta el numero")
else:
    print("no esta")

#busca si hay concidencias al principio de una cadena de texto 