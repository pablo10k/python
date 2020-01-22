

def first_not_repeating_char(char_sequence):
    
                
    
if __name__ == "__main__":
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracateres se repiten')
    else:
        print(f'El primer caracter no repetido es: {result}')