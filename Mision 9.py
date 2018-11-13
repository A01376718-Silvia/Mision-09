# encoding = UTF-8
# Autor: Silvia Ferman
# Mision 9

from math import sqrt

# Función que recibe una lista de números enteros y regresa una nueva que contiene solo los valores pares
def extraerPares(listaUno):
     listaNueva = []
     for valor in listaUno:
         if valor % 2 == 0:
             listaNueva.append(valor)
     return listaNueva


# Funcion que recibe una lista y regresa una nueva con los valores que son mayores a un elemento previo.
def extraerMayoresPrevio(listaDos):
    listaNueva = []
    n = len(listaDos)
    for valor in range(1, n):
        if listaDos[valor] > listaDos[valor-1]:
            listaNueva.append(listaDos[valor])
    return listaNueva


# Funcion que recibe una lista y regresa una nueva con cada pareja de datos intercambiada
def intercambiarParejas(listaTres):
    listaNueva = []
    n = len(listaTres)
    if n == 0:
        return listaNueva
    if n % 2 != 0:
        for dato in range(0, n - 1, 2):
            listaNueva.append(listaTres[dato + 1])
            listaNueva.append(listaTres[dato])
        listaNueva.append(listaTres[-1])
        return listaNueva
    if n % 2 == 0:
        for dato in range(0, n, 2):
            listaNueva.append(listaTres[dato + 1])
            listaNueva.append(listaTres[dato])
        return listaNueva


# Funcion que recibe una lista de valores e intercambia el valor menor / mayor
def intercambiarMM(listaCuatro):
    if len(listaCuatro) < 2:
        listaCuatro = []
    else:
        valorMenor = min(listaCuatro)
        valorMayor = max(listaCuatro)
        menor = listaCuatro.index(valorMenor)
        mayor = listaCuatro.index(valorMayor)
        listaCuatro[menor] = valorMayor
        listaCuatro[mayor] = valorMenor
    return listaCuatro


# Funcion que recibe una lista de valores enteros y regresa el promedio 'centro' de los valores
# promedio 'centro' --> promedio entero (SIN considerar el mayor/menor)
def promediarCentro(listaCinco):
    listaCinco.sort()
    n = listaCinco[1:len(listaCinco) - 1]
    if len(n) > 0:
        promedioCentro = sum(n) // len(n)
        return promedioCentro
    else:
        return 0


# Funcion que recibe una lista de numeros y regresa una dupla con la media y la desviacion estandar
def calcularEstadistica(listaSeis):
    n = len(listaSeis)
    dupla = (0,0)
    if n == 0:
        return dupla
    if n != 0:
        x = sum(listaSeis) / n
    else:
        x = 0
    if n > 1:
        suma = 0
        for valor in listaSeis:
            suma += (valor - x) ** 2
        desviacion = sqrt((suma) / (n - 1))
    else:
        desviacion = 0
    return x, desviacion


# Funcion que recibe una lista y regresa la suma de los valores de la lista
def calcularSuma(listaSiete):
    n = len(listaSiete)
    suma = 0
    if n == 0:
        return suma
    if n == 1:
        suma += listaSiete[0]
        return suma
    if listaSiete[0] != 13:
        suma += listaSiete[0]
    for valor in range(1, n - 1):
        if listaSiete[valor] != 13 and listaSiete[valor + 1] != 13 and (listaSiete[valor - 1]) != 13:
            suma += listaSiete[valor]
        if listaSiete[0] and listaSiete[1] != 13:
            suma += listaSiete[0]
        if listaSiete[-1] and listaSiete[-2] != 13:
            suma += listaSiete[1]
    return suma

# FUNCION PRINCIPAL
def main():
    listaA = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    listaB = [5, 7, 3]
    listaC = []
    listaD = [5, 4, 3, 2]
    listaE = [1, 2, 3]
    listaF = [7]
    listaG = [5, 9, 3, 22, 19, 31, 10, 7]
    listaH = [70, 80, 90]
    listaI = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85,]
    listaJ = [20, 55, 30, 5, 55, 5]
    listaK = [5, 9, 1, 8]
    listaL = [5, 8]
    listaM = [1]
    listaN = [1, 2, 3, 4, 5, 6]
    listaO =[13, 49]
    listas = [listaA, listaB, listaC, listaD, listaE, listaF, listaG, listaH, listaI, listaJ, listaK, listaL, listaM, listaN, listaO]
    print("Problema 1. Regresa una lista con los valores pares de la lista original.")
    for lista1 in listas:
        a = extraerPares(lista1)
        print("Con la lista", lista1, ", regresa", a)
    print()  # Espacio entre ejercicios
    print("Problema 2. Regresa una lista con los valores que son mayores a un elemnto previo.")
    for lista2 in listas:
        b = extraerMayoresPrevio(lista2)
        print("Con la lista", lista2, ", regresa", b)
    print()  # Espacio entre ejercicios
    print("Problema 3. Regresa una lista con cada pareja de datos intercambiada.")
    for lista3 in listas:
        c = intercambiarParejas(lista3)
        print("Con la lista", lista3, ", regresa", c)
    print()  # Espacio entre ejercicios
    print("Problema 4. Regresa una lista que intercambia el valor menor y mayor.")
    for lista4 in listas:
        d = intercambiarMM(lista4)
        print("Con la lista", lista4, "al regresarla es", d)
    print()  # Espacio entre ejercicios
    print("Problema 5. Regresa el promedio 'centro' de los valores.")
    for lista5 in listas:
        e = promediarCentro(lista5)
        print("Con la lista", lista5, "regresa", e)
    print()  # Espacio entre ejercicios
    print("Problema 6. Regresa el promedio 'centro' de los valores.")
    for lista6 in listas:
        f = calcularEstadistica(lista6)
        print("Con la lista", lista6, "regresa", f)
    print()  # Espacio entre ejercicios
    print("Problema 7. Regresa el promedio 'centro' de los valores.")
    for lista7 in listas:
        g = calcularSuma(lista7)
        print("Con la lista", lista7, "regresa", g)
    print()  # Espacio entre ejercicios


# Se llama a la función principal
main()