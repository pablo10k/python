
if __name__ == '__main__':


    print('Notas del semestre')
    print('')
    materia = str(input('Nombre de la materia: '))
    notas = float(input('Introduce tu nota: '))

    calificaciones = {}

    calificaciones['{}'.format(materia)] = '{}'.format(notas)


    print('Tus notas en {} son: {}'.format(materia, notas))
