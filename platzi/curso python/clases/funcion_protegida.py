#-*- coding: utf-8 -*-

def protected(función):
    
    def wrapper(password):
        if password == 'Platzi':
            return función()
            #llama a protected_func y este imprime lo password correcta
        else:
            print('Password incorrecta!!')
    
    return wrapper #llama a la funcion wrapper, si no se coloca no se ejecuta wrapper()

#al tener el @ se direcciona a protected(): con el parametro como protected_func()
@protected 
#este es el parametro "función"
def protected_func():
    print('Password Correcta!!')

if __name__ == "__main__":
    password = str(input('Introduce tu contraseña: '))
    #se pasa password a protected_func
    protected_func(password)