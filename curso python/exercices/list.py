# -*- coding: utf-8 -*-

def read():
    pass

def writer(word_letter, times, name, formato):
    if formato == '1':
    with open('{}'.format(name), 'w') as txt:
        txt.write(word_letter * times)

    
if __name__ == "__main__":
    print('E S C R I T O R   M A G I C O')
    command = str(input('''
        [r]epetir caracteres
        [c]opiar caracteres
        [b]orrar caracters
        
        '''))
    if command == 'r':
        
        word_letter = str(input('Seleccione la letra/palabra a repetir: '))
        times = int(input('Veces a a repetir la letra/palabra: (solo números) '))
        name = str(input('Nombre del archivo: '))
        formato_op = str(input(''' 
        1-Todo en un sola linea
        2-Todo en columnas
        '''))
        if formato_op == '1':
            formato = 0
        else formato_op == '2':
            formato = 1
        writer(word_letter, times, name, formato)