import math
from decimal import *

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
cifra = []

def cifrado(letra):
    cifra.clear()
    for k in range(0, len(letra)):
        for j in range(0, len(abecedario)):
            if abecedario[j] == letra[k]:
                cifra.append(j)
    return cifra

def operaciones(arg):
    c = 0
    
    cifrado(arg)
    #print(cifra)
    longAbecedario = len(abecedario)
    
    for i in range(0,len(cifra)):
        #print("k",longAbecedario**(k+1-(i+1)))
        c += cifra[i]*longAbecedario**(k+1-(i+1))
        
    mu = [0,1]
    
    Y = (n1-1)*(n2-1)
    #print(Y)

    opera = [Y,e]
    #Calculo inverso
    aux = False
    resto = 2

    #while aux == False:
        #numerador = opera[len(opera)-2]
        #divisor = opera[len(opera)-1]
        #division = math.trunc(numerador/divisor)
        #resto = numerador%divisor
        #opera.append(resto)
    
        #print("D:",division,"e:",resto)
    
        #muNueva = mu[len(mu)-2]-(division*mu[len(mu)-1])

        #mu.append(muNueva)

        #aux = es_primo(resto)
    #Calculo inverso de e mod Y
    inverso = pow(e, -1, Y)
    
    #print("i", inverso)
    #print("m",mu[len(mu)-1])
    #print("c",c)
    #Calculo c elevado a d mod n con APM
    resultadoExponente = pow(c,inverso,n)
    
    #inverso = pow(e, -1, Y)
    #print("r",resultadoExponente)
    aux2 = False
    resultadoCociente = [resultadoExponente]
    resultadoResto = []
    g=0
    #Aqui se hace la division
    while aux2==False:
        #print("R", resultadoCociente[len(resultadoCociente)-1], "L", longAbecedario)
        #aux3 = resultadoExponente
        #print(aux3)
        #print("R",resultadoCociente[len(resultadoCociente)-1], "l", longAbecedario)

        resultadoResto.append((resultadoCociente[len(resultadoCociente)-1]%longAbecedario))
        resultadoCociente.append(math.trunc(Decimal(resultadoCociente[len(resultadoCociente)-1])/Decimal(longAbecedario)))
        
        #print("D",resultadoResto[len(resultadoResto)-1])
        
        #g+=1
        if (resultadoCociente[len(resultadoCociente)-1]/longAbecedario) < 1:
            #print("a")
            aux2 = True
        g +=1
        #for q in range(0, len(resultadoResto)):
            #print("R",resultadoResto[q])

        #print("C",resultadoCociente[len(resultadoCociente)-1])
        #print("D", math.trunc(resultadoExponente/longAbecedario), "r", resultadoExponente%longAbecedario)
    
    arrayResultado = []
    
    #print(arrayResultado[0])
   
    for z in range(0, len(resultadoResto)):
        arrayResultado.append(resultadoResto[z])
        #print("a",arrayResultado)
    
    arrayResultado.append(resultadoCociente[len(resultadoCociente)-1])
    
    resultado = []
    aux4 = ""
    z = len(arrayResultado)-1
    while z >=0:
        aux3 = arrayResultado[z]
        print(abecedario[aux3])
        aux4 += abecedario[aux3]
        z-=1
    #for z in range(len(arrayResultado)-1, 0):
        #for b in range(0, longAbecedario):
        #if(arrayResultado[z] == abecedario[b]):
        #print (z)
        
        #resultado.append(abecedario[aux3])
    
    #resultado.append(aux4[::1])
    


    for z in range(0, len(resultado)):
        print(resultado[z])



    

print("Introduce el alfabeto")
abecedario = input()

print("Introduce n")
n = int(input())

print("Introduce e")
e = int(input())

print("Introduce p")
n1 = int(input())

print("Introduce q")
n2 = int(input())

print("Introduce el mensaje cifrado")
mensajeC = input()



#Calculo de k
k = math.trunc(math.log(n, len(abecedario)))
#print(k, "a", len(abecedario))


#Dividir en bloques de k
aux = int(len(mensajeC)/3)
mensajeK = []
for i in range(0,aux):
    #print(mensajeC[0:k+1])
    operaciones(mensajeC[0:k+1])
    mensajeC = mensajeC[k+1:len(mensajeC)]
