

def first_not_repeating_char(char_sequence):
    seen_letters = {}

    for idx, letter in enumerate(char_sequence):
            #agrega a el dicc. seen_letters
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1) #el uno por la vez que se vio
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1) 
                                                                                #el +1 es porque ya se conoce la letra y se vio por 2da vez 
    final_letters = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append( (key, value[0]))
    #sorted() == ordenar
    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])
    #igual a:
    # def sort_list(value):
    #   return value[1]                                                                          
    ###difinir funcion con una linea es lambda            
    
    if not_repeated_letters:
        return not_repeated_letters[0][0]
        #si not_repeated_letters tiene algo envia de not_repeate_letters[0][0] lo que equivale a la 1°era letra
    else:
        return '_'
if __name__ == "__main__":
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracateres se repiten')
    else:
        print(f'El primer caracter no repetido es: {result}')