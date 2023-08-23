
class Car:

    def __init__(self): 
        self.x = 0
        self.y = 0
        self.heading = 'n'


    def turn(self, direction):
        
        if direction == 'l':
            if self.heading == 'n':
                self.heading = 'w'
            elif self.heading == 'w':
                self.heading = 's'
            elif self.heading == 's':
                self.heading = 'e'
            elif self.heading == 'e':
                self.heading = 'n'

        elif direction == 'r':
            if self.heading == 'n':
                self.heading = 'e'
            elif self.heading == 'e':
                self.heading = 's'
            elif self.heading == 's':
                self.heading = 'w'
            elif self.heading == 'w':
                self.heading = 'n'
     


    def drive(self, distance = 1):
        if self.heading == 'n': 
            self.y += distance
    
        elif self.heading == 's':
            self.y -= distance

        elif self.heading == 'e':
            self.x += distance

        elif self.heading == 'w':
            self.x -= distance


    def status(self):
        print("Coordinates: (" + str(self.x) + ',' + str(self.y) + ')')
        print("Heading: " + self.heading)


#USE_CAR, COPY AND PASTE ONTO NEW SCRIPT
from car import Car

def main():
    """ Using car class"""
    c = Car()
    c.turn('r')
    c.status()
    c.drive()
    c.turn('r')
    c.drive()
    c.drive()
    c.drive()
    c.drive()
    c.drive()
    c.drive()
    c.drive()
    c.drive()
    c.status()
    c.turn('r')
    c.drive()
    c.status()
    c.drive()
    c.turn('l')
    c.turn('l')
    c.status()
    c.status()


if __name__ == "__main__":
     main()
