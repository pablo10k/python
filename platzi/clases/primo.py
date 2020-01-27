# -*- coding: utf-8 -*-


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
        
    else:
        for z in range(3,number):
            if number % z == 0:
                return False

    return True

def run():
    number = int(input('Type a number: '))
    result = is_prime(number)
    if result is True:
        print('Tu numero es primo')
    else:
        print('Tu numero no es primo')

if __name__ == '__main__':
    run()
