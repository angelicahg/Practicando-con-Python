# Escribir una función que reciba un número entero positivo y devuelva su factorial.

from cgi import print_form


def factorial():
    from math import factorial
    num = int(input("ingrese numero enero y positivo: "))
    if num >0:
        print(factorial(num))
    else:
        print("el numero es negativo y no podemos seguir")
factorial()
