# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora():
    def __init__(self):
        self.num1= int(input("ingrese el primer valor: "))
        self.num2= int(input("ingrese el segundo valor: "))
    
    def suma(self):
        self.suma= self.num1 +self.num2
        print("la suma resultado de: ",self.suma)
    
    def resta(self):
        self.resta= self.num1 -self.num2
        print ("la resta resultado de: ",self.resta)
    
    def resta(self):
        self.resta= self.num1 -self.num2
        return"la resta resultado de: ",self.resta

    def multiplicacion (self):
        self.multiplicacion= self.num1 *self.num2
        return"la multiplicacion resultado de: ",self.multiplicacion

    def division (self):
        self.division= self.num1 / self.num2
        return"la division resultado de: ",self.division

calcular=Calculadora()
calcular.suma()
calcular.resta()
print(calcular.multiplicacion())
print(calcular.division())