# -*- coding: utf-8 -*-

import random

#borrar pantalla
import os

def main():
    print('----ADIVINA BUEN ADIVINADOR-----\n')
    print('1-Facil')
    print('2-Dificil\n')

    dificult = input('Elige dificultad: ')
    if dificult == '1' or 'Facil' or 'facil':
        #produce el numero maximo de la generacion
        #haciendolo algo mas complejo
        range = random.randint(50,800)
    elif dificult == '2' or 'Dificil' or 'dificil' or 'dif':
        range = random.randint(250,1200)
    else:
        range = random.randint(50,800)

    run(range)

def run(range):
    number_found = False
    random_number = random.randint(1, range)
    count = 0
    while not number_found:
        count += 1
        if count == 10:
            print('\nGAME OVER alquornoque')
            print('El numero era el {}\n'.format(random_number))
            volver_jugar()
            exit()

        number = int(input('Intenta un número: '))

        if number == random_number:
            #borrar pantalla
            os.system('cls')

            print('\nFelicidades. Encontraste el número {} en {} intentos!!'.format(random_number,count))
            number_found = True
            volver_jugar()

        elif number > random_number:
            #borrar pantalla
            os.system('cls')

            print('Te quedan {} intentos'.format(10-count))
            print('El número es más pequeño')
        elif number < random_number:
            #borrar pantalla
            os.system('cls')

            print('Te quedan {} intentos'.format(10-count))
            print('El número es más grande')
        else:
            print('Opcion no valida')

def volver_jugar():
    again = input('Play Again?(yes/no)')
    if again == 'yes' or 'y' or 's':
        os.system('cls') #'clear' en caso de usar linux/mac
        main()
    else:
        os.system('cls')
        exit()
        
if __name__ == '__main__':
    main()
