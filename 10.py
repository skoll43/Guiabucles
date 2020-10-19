a=0
divisor=0

while True:
    numero=int(input("Ingrese numero (0 para salir): "))
    divisor+=1
    a=a+numero

    if numero==0:
        divisor=divisor-1
        break
print("El promedio de estos números es: ",a/divisor)