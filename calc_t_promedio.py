# -*- coding: utf-8 -*-

def aver_temps(temps):
    suma_temp = 0

    for t in temps:
        suma_temp += t

    return suma_temp / len(temps)



if __name__ == '__main__':
    temps = [21, 24, 24, 22, 20, 23, 24]

    res = aver_temps(temps)
    print('La T° promedio es {}'.format(res))
