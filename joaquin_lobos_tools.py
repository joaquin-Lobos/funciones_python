import random


def imprimir_nombre(nombre, apellido):
    print(nombre, apellido)
    # En este lugar debe colocar el "print" e imprimir
    # en pantalla el nombre y apellido que vienen por parámetro
    # print(.....)


def promedio(numeros):
    if len(numeros) > 0:
        promedio = sum(numeros) / len(numeros)
        return promedio
    else:
        return
    # Alumno:
    # 1) calcule el promedio
    # 2) use "return" para retornar ese valor
    # Cuando termine de implementar está función borrar "pass"

def ordenar(numeros):
    numeros.sort()
    return 

def lista_aleatoria(inicio, fin, cantidad):
    contador = 0
    lista_random = []
    while contador != cantidad:
        contador += 1
        numero = random.randrange(inicio, fin+1)
        lista_random.append(numero)

    return lista_random

def contar(lista, numero):
    return lista.count(numero)
