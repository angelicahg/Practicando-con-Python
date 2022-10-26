#ayudan a buscar elemntos que hayan en una lista rango de caracteres o numero 
import re


lista_nombres = ["Angie ","Camila ", "Santiago ", "Sandra","Rosa"]

for elemento in lista_nombres:
        if re.findall("[O-T]" , elemento):
            print(elemento)


lista_iniciales = ["An1 ","Ca1 ", "Sa2 ", "Sa3","Ro4"]

for elemento in lista_iniciales:
        if re.findall("Sa[0-3]" , elemento):
            print(elemento)