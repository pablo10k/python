# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    pablo = turtle.Turtle()

    make_square(pablo)

    turtle.mainloop()

def make_square(pablo):
    len = int(input('Tamaño de cuadrado: '))

    for i in range(4):
        make_line_and_turn(pablo, len)

def make_line_and_turn(pablo, len):
    pablo.forward(len)
    pablo.right(90)

if __name__ == '__main__':
    main()
