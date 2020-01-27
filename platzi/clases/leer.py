

def run(archivo, palabra):
    count = 0
            #en español se agrega 'encoding=utf8'
    with open(archivo) as f:
        for line in f:
            count += line.count(palabra)
    
    print(f'{palabra} se encuentra implicitamente {count} veces en el texto')

if __name__ == "__main__":
    print('El archivo debe estar en el mismo directorio que este script')
    archivo = str(input('Ingrese el nombre del archivo en el cual buscar: '))
    palabra = str(input('Ingrese la palabra a buscar: '))
    
    
    
    run(archivo, palabra)
