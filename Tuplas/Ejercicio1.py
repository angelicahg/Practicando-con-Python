# Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla

tupla = ("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

OpcionesMes= int(input("ingrese el numero del mes: "))
# OpcionesMes -=1
# # print("tu mes es: ", tupla[OpcionesMes])

print("tu mes es: ", tupla[OpcionesMes-1])


