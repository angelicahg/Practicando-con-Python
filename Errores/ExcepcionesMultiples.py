while True:
    try:
        edad:int(input("ingrese su edad"))
        print("Tu edad es: ", edad )
        break
    except ValueError:
        print("Ingreso un valor erroneo")

  
while True:
    try:
        edad:int(input("ingrese su edad"))
        print("Tu edad es: ", edad )
        break
    except KeyboardInterrupt:
        print("has cancelado la ejecucion")
        break
  