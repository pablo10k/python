# -*- coding: utf-8 -*-

def palindromo(word):
    check_palindromo = word[::-1]
    if check_palindromo == word:
        return True
    return False


if __name__ == '__main__':
    word = input('Comprobar si es un palindromo: ')

    result = palindromo(word)

    if result is True:
        print('{} es un palíndromo!!'.format(word))
    else:
        print('{} NO es un palíndromo!!'.format(word))
