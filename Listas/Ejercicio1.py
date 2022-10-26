#En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar: [20, 50, "Curso", 'Python', 3.14]

lista = [20, 50, "Curso", 'Python', 3.14]
print("estos son los valores actuales de la lista")

palabra1= input("ingrese el primer valordesustituir en el estapacio1: ")
palabra2= input("ingrese el segundo valordesustituir en el estapacio2: ")

lista[0] = palabra1
lista[1] = palabra2

palabra1= input("el nuevo valor de la lista es : {}".format(lista))