
while True:
    try:
        valor = int(input("Ingrese digitos"))
        print("su cifra tiene", len(str(valor)), "digitos")
    except ValueError:
        print("debe ingresar digitos")
    