
import random


class Vehicle:

    def __init__(self, brand, model, color, d_id):
        self.brand = brand
        self.model = model
        self.color = color
        self.d_id = d_id


class Car:
    
    def __init__(self):
        self.cars = []

    def addCar(self, brand, model, color, d_id):
        car = Vehicle(brand, model, color, d_id)
        self.cars.append(car)
    
    def showCars(self):
        for car in self.cars:
            self._printCar(car)

    def _printCar(self, car):
        print('ø-ø-ø-ø-ø     ø-ø-ø-ø-ø-')
        print('Brand: {}'.format(car.brand))
        print('Model: {}'.format(car.model))
        print('Color: {}'.format(car.color))
        print('ID-Car: {}'.format(car.d_id))
        print('''           
            __    _
           / l    \~-_
    ,----~~~~--+-----`--~----____
    @   /~_~\  | ~      |   /~_~\~~~-,
    \_ ( (_) )  \_______|  ( (_) )_-~
      ~~\___/~~~~~~~~~~~~~~~\___/~ 
  ''')
        print('ø-ø-ø-ø-ø     ø-ø-ø-ø-ø-\n')
        
    def drive(self):
        self.showCars()
        IdCar = str(input('Input the ID-Car to drive: '))
        for car in self.cars:
            if car.d_id == IdCar:
                    print('Todoo bien!')
                    return self.turnOn()
                 
            else:
                print('ID-Car wrong or invalid, don\'t forget the revalide your document every year >>:)')
             
    def turnOn(self):
        print('Turning On the beast!')
        command = str(input('Before boot, you want to turn the radio?: (y/n) '))
        if command == 'y':
            pass    
        else:
            print('I Don\'t have written these lines of code for nothing, bruh')
            
        
        return self.radio()
 
    def radio(self):
        stations = {'80.3': 'EDM Station',
                        '77.5': 'Lo-Fi Station',
                        '45.3': 'Rock & Roll Station', 
                        '67.6': 'Comedy Station',
                        '23.8': 'Tech Podcast Station'}

        print('\n++++++PANASONIC 6KLJ+++++++\n')
        for _station, name in stations.items():
            print(f'     {_station} {name}')
            
        station = str(input('\nChoose the station: '))
        for stat in stations:
            if stat.lower() == station.lower():
                print('Listenting the {}'.format(stat))
            
        print('++++++PANASONIC 6KLJ+++++++\n')
        
        self.driving()
    
    def driving(self):

        GAME_OVER = ['''
+++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++''','''
                        END GAME
            END GAME
END GAME
        END GAME             END GAME
                END GAME
    END GAME        END GAME
   END GAME   END GAME       END GAME
         END GAME      END GAME

 END GAME   END GAME    END GAME''']


        ART = ['''
++++++++++++++/       / o     /++++++++
+++++++++++++/       / /|\   /+++++++++
++++++++++++/       /  / \  /++++++++++
+++++++++++/       /       /+++++++++++
++++++++++/       /       /++++++++++++
+++++++++/       /       /+++++++++++++
++++++++/       /       /++++++++++++++
+++++++/       / o·-·o /+++++++++++++++
++++++/       / /'='/ /++++++++++++++++
+++++/       / o·-·o /+++++++++++++++++''',
'''
++++++++++++++/       /       /++++++++
+++++++++++++/       /       /+++++++++
++++++++++++/       / o     /++++++++++
+++++++++++/       / /|\   /+++++++++++
++++++++++/       /  / \  /++++++++++++
+++++++++/       /       /+++++++++++++
++++++++/       /       /++++++++++++++
+++++++/       / o·-·o /+++++++++++++++
++++++/       / /'='/ /++++++++++++++++
+++++/       / o·-·o /+++++++++++++++++
''',
'''
++++++++++++++/       /       /++++++++
+++++++++++++/       /       /+++++++++
++++++++++++/       /       /++++++++++
+++++++++++/       /       /+++++++++++
++++++++++/       /       /++++++++++++
+++++++++/ o·-·o / o     /+++++++++++++
++++++++/ /'='/ / /|\   /++++++++++++++
+++++++/ o·-·o /  / \  /+++++++++++++++
++++++/       /       /++++++++++++++++
+++++/       /       /+++++++++++++++++
''',
'''
++++++++++++++/       /       /++++++++
+++++++++++++/       /       /+++++++++
++++++++++++/       /       /++++++++++
+++++++++++/ o·-·o /       /+++++++++++
++++++++++/ /'='/ /       /++++++++++++
+++++++++/ o·-·o /       /+++++++++++++
++++++++/       / o     /++++++++++++++
+++++++/       / /|\   /+++++++++++++++
++++++/       /  / \  /++++++++++++++++
+++++/       /       /+++++++++++++++++
''',
'''
++++++++++++++/       /       /++++++++
+++++++++++++/ o     /       /+++++++++
++++++++++++/ /|\   /       /++++++++++
+++++++++++/  / \  /       /+++++++++++
++++++++++/       /       /++++++++++++
+++++++++/       /       /+++++++++++++
++++++++/       /       /++++++++++++++
+++++++/ o·-·o /       /+++++++++++++++
++++++/ /'='/ /       /++++++++++++++++
+++++/ o·-·o /       /+++++++++++++++++
''',
'''
++++++++++++++/       /       /++++++++
+++++++++++++/       /       /+++++++++
++++++++++++/       /       /++++++++++
+++++++++++/ o     /       /+++++++++++
++++++++++/ /|\   /       /++++++++++++
+++++++++/  / \  /       /+++++++++++++
++++++++/       /       /++++++++++++++
+++++++/ o·-·o /       /+++++++++++++++
++++++/ /'='/ /       /++++++++++++++++
+++++/ o·-·o /       /+++++++++++++++++
''',
'''
+++++++++++++/       /       /+++++++++
++++++++++++/       /       /++++++++++
+++++++++++/       /       /+++++++++++
++++++++++/       /       /++++++++++++
+++++++++/       /       /+++++++++++++
++++++++/ o     / o·-·o /++++++++++++++ 
+++++++/ /|\   / /'='/ /+++++++++++++++
++++++/  / \  / o·-·o /++++++++++++++++
+++++/       /       /+++++++++++++++++
++++/       /       /++++++++++++++++++
''']
        print('Press letter a for left and d for right')
        ART[0]
        
           

    def alcornoque():
            print('Are you stupid???')
            print('You almost explode the system')
            print('GOODBYE FRIEND!')
            for _ in range(100000000):
                __ = _ + _ + _
            






if __name__ == "__main__":
    car = Car()
    
    while True:    
        print('\n+++++++++WELCOME TO YOUR GARAGE+++++++++++')
        command = str(input('''
        [d]rive 
        [v]iew cars
        [n]ew car
        e[x]it 
                        
        '''))

        if command == 'd':
            car.drive()

        elif command == 'v':
            car.showCars()
            
        elif command == 'n':
            brand = str(input('Choose a brand: '))
            model = str(input('Choose a model: '))
            color = str(input('Choose a color: '))
            
            for i in range(100,150):
                d_id = str(i) + brand[:2]
            
            car.addCar(brand, model, color, d_id)
        

            
    
        

        
