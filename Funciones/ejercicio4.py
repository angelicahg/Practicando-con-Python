# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

from calendar import month
from re import I
from time import monotonic


def total():
    monto = float(I("ingrese vlor del producto :"))
    iva = int(input("ingrese valor del iva:"))
    if iva != 0:
      if iva >0:
        totalPagar = ((monto *iva)/100)+monto
        return totalPagar
      else:
        return("El monto de IVA es negativo.No se puede avanzar ")
    else:
        totalPagar = (monto * 0.21)+monto
        return totalPagar
print("el total es :", total)