# -*- coding: utf-8 -*-
        
def choose_ex(type):
    print('1-Dolar')
    print('2-Euro')
    print('3-Peso Argentino ')
    print('4-Peso Colombiano')
    print('5-Peso Mexicano')
    
    clp_to_ex = str(input('Ingrese  la opcion a convertir: ')
    if clp_to_ex == '1' :
    	type = 770.5
        return type
        
    if clp_to_ex == '2' :
    	type = 857.6
        return type
        
    else:
    	print('Opcion no valida')
    	
        

def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte de CLP a otras divisas')
    print('')
    
    result* = choose_ex(type)
    
    ammount = float(input('Ingresa cantidad a convertir (clp): '))

    result = foreign_ex(ammount)

    print('${} pesos chilenos son ${} pesos colombianos'.format(ammount, result))


def foreign_ex(ammount):
    clp_to_cop = ammount * 4.22

    return clp_to_cop



if __name__ == '__main__':
    run()
