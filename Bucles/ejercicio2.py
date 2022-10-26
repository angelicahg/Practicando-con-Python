# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

from re import I


edad = int(input("ingrese su esdad,para saber tus años : "))
i= 1

while i <= edad:
    print("has cumplido: {} añios".format(i))
    i += 1