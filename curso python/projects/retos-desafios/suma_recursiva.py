# -*- coding: utf-8 -*-

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1


    numero = numero * factorial(numero-1)
    return(numero)


def suma(numero):
    if numero == 0:
        return 0
        
    else:
        numero = numero + suma(numero - 1)
        return numero



if __name__ == "__main__":
    numero = int(input('Número: '))
    print(f'Suma recursiva de {numero} es ' + str(suma(numero)))
    print(f'Factorial de {numero} es ' + str(factorial(numero)))