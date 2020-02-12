import random


def ordenamiento_por_insercion(lista):
    #lista[3,5,2]
    for indice in range(1, len(lista)):
        valor_actual = lista[indice] #valor_actual = 5
        
        posicion_actual = indice  #posicion_actual = 1
        
        # mientras posicion actual=1 sea mayor a 0 *+y** lista[posicion_actual - 1]=3 sea mayor a 5:
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1] # lista[posicion_actual](5) = lista[posicion_actual-1:pos0](3)
            posicion_actual -= 1 # poscion_actual -=1 (0)

        lista[posicion_actual] = valor_actual
    return lista

if __name__ == "__main__":    
    tamano_lista = int(input('De que tamano sera la lista?: '))

    lista = [random.randint(0,100) for i in range(tamano_lista)]
    print(lista)
    lista_ordenada = ordenamiento_por_insercion(lista)

   
    print(lista_ordenada)