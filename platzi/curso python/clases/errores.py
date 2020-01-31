# -*- coding: utf-8 -*-

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31,
}

while True:
    country = str(input('De donde eres?: ')).lower()
    try:
        print(f'La poblacion de {country} es {countries[country]} millones')

    except KeyError:
        print(f'No disponemos la informacion de {country.capitalize()}')
    
