# -*- coding: utf-8 -*-

import random

def binary_search(numbers, number_to_find, low, high):

    if low > high:
        return False #se cruzan los indices, o sea que esta desordenada la lista

    mid = (low + high) / 2

    if numbers[mid] == number_to_find:
        return True

    elif numbers[mid] > number_to_find:#numero de medio es mayor al a encontrar
        return binary_search(numbers, number_to_find, low, mid - 1) #mid -1 para que baje al indice anterior

    else:
        return binary_search(numbers, number_to_find, mid + 1, high)#mid + 1 ya que el numero a encontrar esta indices mas arriba

    #tanto elif como else aqui funcionan a base del if. haciendo modificacones al mid y comprobando desde el if



if __name__ == '__main__':
    numbers = []
    for i in range(1000):

        number_gen = random.randint(0,1000)
        numbers.append(number_gen)

    numbers.sort()
    print(numbers)
    while 10 > 1:

        number_to_find = int(input('Ingrese un número: '))

        result = binary_search(numbers, number_to_find, 0, len(numbers) -1) #len cuenta como humano 1,2,3,4  pero en la lista se cuenta desde 0, asi si tienes 14 elementos en lista en realidad son 13 para la maquina(cueenta desde 0)

        if result is True:
            print('Número existente')
        else:
            print('Número inexistente')
