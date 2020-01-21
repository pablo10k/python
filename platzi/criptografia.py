# -*- coding: utf-8 -*-

KEYS = {
    'a' : 'q',
    's' : 'w',
    'd' : 'e',
    'f' : 'r',
    'g' : 't',
    'h' : 'y',
    'j' : 'u',
    'k' : 'i',
    'l' : 'o',
    'ñ' : 'p',
    'q' : 'z',
    'w' : 'x',
    'e' : 'c',
    'r' : 'v',
    't' : 'b',
    'y' : 'n',
    'u' : 'm',
    'i' : ',',
    'o' : '.',
    'p' : '-',
    'z' : 'A',
    'x' : 'B',
    'c' : 'C',
    'v' : 'D',
    'b' : 'E',
    'n' : 'F',
    'm' : 'G',
    ',' : 'H',
    '.' : 'J',
    '-' : 'K',
}


def cifrar(msj):
    #split separa las palabras mediante ' ' y espacios
    words = msj.split(' ')
    print(words)
    msj_cifrado = []

    for word in words:
        palabra_cifrada = ''
        for letter in word:
            palabra_cifrada += KEYS[letter]

        msj_cifrado.append(palabra_cifrada)
        #join junta
    return ' '.join(msj_cifrado)


def descifrar():
    pass

def run():
    while True:
        com = print('[DES]CIFRADOR 3000')
        com1 = input('''
        [c]ifrar
        [d]escifrar
        [s]alir

        ''')

        if com1 == 'c':
            msj = input('Mensaje a cifrar: ')
            msj_cifrado = cifrar(msj)
            print(msj_cifrado)

        if com1 == 'd':
            descifrar()

        else:
            print('COMANDO NO ENCONTRADO! ')

if __name__ == '__main__':
    run()
