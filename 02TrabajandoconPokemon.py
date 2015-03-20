
# Asignatura: Sistemas Distribuidos
# Alumno: Castro Monterrosa, Edson


#Funcion recursiva en la cual busca la coincidencia con la primera letra de las palabras de la lista.
def funrecursiva(pivote, lista):
    cuenta = 0  
    i=0
    while (i < len(lista)):#Se recorre la lista completa para buscar coincidencias.
        palabra=lista[i]
        if pivote[-1] != palabra[0]:#Si son diferentes pasa
            pass
        else:#Si son iguales aumenta la cuenta en 1, y llama a la funcion cambiando la palabra pivote.
            cuenta = cuenta + 1            
            print "palabra encontrada y a buscar su ultima letra: ",palabra
            if (lista[i] != lista[-1]):#Para evitar recursividad infinita vemos si la palabra buscada es la ultima.
                cuenta = cuenta + funrecursiva(palabra,lista)  
        i = i + 1    
    return cuenta


############################# Inicio del programa #############################33
fichero = open("pokemon2.txt", "r") #Abriendo fichero para lectura
cuenta = 0
cuentaux = 0

lista = fichero.readline()#Leyendo fichero linea por linea y concatenando.
lista = lista.rstrip('\n')
for linea in fichero:    
    linea = linea.rstrip('\n')    
    lista = lista  + linea
lista = lista.split(" ")


for pal in lista:# for que recorre todas las palabras a buscar en la lista.
    print "Ultima letra de la palabra: ",pal 
    cuenta = funrecursiva(pal, lista)#Funcion recursiva que tiene como parametros la palabra buscada y la lista.
    if cuenta < cuentaux:
        cuenta = cuentaux
    else:
        cuentaux = cuenta
print "El numero maximo de palabras encontras es de: ", cuenta