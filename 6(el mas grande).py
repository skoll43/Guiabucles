
grande = 0
num = 0
salir = 0
print("Ingrese numeros\nIngrese espacio vacio para terminar")
while salir != 1:
    num = input("")
    if num == " ":
        break
    else:
        if int(num) > int(grande):
            grande = num
print(grande, "Es el mas grande")