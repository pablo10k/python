import random

def busquda_lineal(lista, objetivo, count):
    match = False

    for e in lista:
        if e == objetivo:
            match = True
        print(f'Pasos:{count}')
        count += 1
    return match

if __name__ == "__main__":
    tamano_lista = int(input('Tamano de la lista: '))
    objetivo = int(input('Numero a encontrar: '))

    lista = [random.randint(0,1000000) for i in range(tamano_lista)]

    encontrado = busquda_lineal(lista, objetivo, count=1)
    #print(lista)

    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')