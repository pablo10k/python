# -*- coding: utf-8 -*-

KEYS = {
    'a': '!',
    'b': '¶',
    'c': '¾',
    'd': '/',
    'e': 'H',
    'f': '¤',
    'g': '¢',
    'h': '+',
    'i': 'R',
    'j': '±',
    'k': 'S',
    'l': '~',
    'm': '8',
    'n': '®',
    'ñ': '1',
    'o': '½',
    'p': '4',
    'q': '"',
    'r': '5',
    's': '£',
    't': '6',
    'u': '$',
    'v': '2',
    'w': '3',
    'x': '@',
    'y': '9',
    'z': '0',
    'A': '§',
    'B': 'p',
    'C': 'l',
    'D': '¬',
    'E': 'm',
    'F': '&',
    'G': 'g',
    'H': '×',
    'I': '-',
    'J': 'r',
    'K': 'µ',
    'L': 'd',
    'M': '¥',
    'N': 'v',
    'Ñ': 'Æ',
    'O': '¦',
    'P': 'c',
    'Q': '#',
    'R': 'x',
    'S': '¼',
    'T': 'z',
    'U': '?',
    'V': '÷',
    'W': '©',
    'X': 'a',
    'Y': '%',
    'Z': 'q',
    '0': 'co',
    '1': 'uo',
    '2': 'ds',
    '3': 'ts',
    '4': 'cr',
    '5': 'cc',
    '6': 'ss',
    '7': 'se',
    '8': 'oo',
    '9': 'ne',
    '.': 'po',
    ',': 'ca',
    '?': 'pa',
    '!': 'an',
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


def descifrar(message):
    words = message.split(' ')
    decipher_message = []

    for word in words:
        decipher_word = ''

        for letter in word:

            for key, value in KEYS.items():
                if value == letter:
                    decipher_word += key
        
        decipher_message.append(decipher_word)
    
    return ' '.join(decipher_message)


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
            message = str(input('Escribe tu mensaje cifrado: '))
            decypher_message = descifrar(message)
            print(decypher_message)

        else:
            print('COMANDO NO ENCONTRADO! ')

if __name__ == '__main__':
    run()
