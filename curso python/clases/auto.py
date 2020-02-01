# -*- coding: utf-8 -*-

class Car:
    _CARS = ['''
      ______
     /|_||_\`.__
    (   _    _ _)
    =`-(_)--(_)-' 
    
    ''', 
    '''
           ______
    -   --/|_||_\`.__
    ---  (   _    _ _)
    --  =`-(_)--(_)-' 
    ''']

    def __init__(self, stopped):
        self._stopped = stopped
        self._image()

    def turn_on(self):
        self._stopped = False
        self._image()

    def turn_off(self):

        self._stopped = True
        self._image()

    def _image(self):
        if self._stopped:
            print(self._CARS[0])
        else:
            print(self._CARS[1])

def run():
    car = Car(stopped=True)
    
    cm = input('''
    BIENVENiDO A TU AUTO 3000
    
        [e]ncender
        [a]pagar
        [i]ncendiar
        
        ''')
    if cm == 'e':
        car.turn_on()

    elif cm == 'a':
        car.turn_off()
    
    else:
        print('''
                                      _.-="_-         _
                         _.-="   _-          | ||"""""""---._______     __..
             ___.===""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __'
      __.--""     __        ,'                   o \           __        [__|
 __-""=======.--""  ""--.=================================.--""  ""--.=======:
]       [w] : /        \ : |========================|    : /        \ :  [w] :
V___________:|          |: |========================|    :|          |:   _-"
 V__________: \        / :_|=======================/_____: \        / :__-"
 -----------'  "-____-"  `-------------------------------'  "-____-" ''')
        


if __name__ == "__main__":
    run()