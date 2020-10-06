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
    #ingresar para n personas donde n es un número ingresado por teclado: nombre y edad. 
    #calcular y mostrar: cantidad de personas mayores de edad y cantidad de menores de edad. 
    #subir la modificar a github con el siguiente mensaje: "se programo la opción 2 del menú"
    #subir la modificación a github con el siguiente mensaje: "se programo la opción 2 del menú"
    npersonas=int(input("ingrese la cantidad de personas que desea ingresar: "))
    for x in range(npersonas):
        edad=int(input("Ingrese edad de la persona: "))
        if edad>=18:
            emayor=emayor+1
        else:
            emenor=emenor+1
    print("La cantidad de personas mayores de edad es de: "+str(emayor))
    print("La cantidad de personas menores de edad es de: "+str(emenor))            
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