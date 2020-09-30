import os
def Numeros():
    print("OPN")
    veces= int(input("Cuantos números desea ingresar?: "))
    pos=0
    neg=0
    cero=0
    for x in range(veces): 
        nume=int(input("Ingrese un número: "))
        if (nume>0):
            pos=pos+1
        elif(nume<0):
            neg=neg+1
        else:
            cero=cero+1 
    print("Cantidad de números positivos: " + str(pos)+ 
          "\n Cantidad de números negativos : "+ str(neg)+ 
          "\n Cantidad de números iguales a cero: " + str(cero))   
    pausa=input("Presione una tecla para continuar")
def Datos():
    print("OPD")
    pausa=input("Presione una tecla para continuar")
seguir=True
while (seguir):
    os.system('cls')
    print("1. Opcion Numeros ")
    print("2. Opcion Datos de Personas ")
    print("3. Finalizar ")
    op=int(input("Ingrese opción 1,2,3: "))
    if op==1:
        Numeros()
    if op==2:
        Datos()
    if op==3:
        seguir=False
        break        