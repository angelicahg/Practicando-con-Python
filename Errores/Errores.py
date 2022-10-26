while True:
    try:
        edad:int(input("ingrese su edad"))
        print("Tu edad es: ", edad )
        break
    except:
        print("Ingreso un valor erroneo")
    finally:
        print("jecucion ha finalizado")