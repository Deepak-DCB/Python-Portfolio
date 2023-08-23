
class Car:
    """
    A class for a car that can turn left/right and move forward
    """
    def __init__(self): 
        """
        Initializes a Car object
        """
        self.x = 0
        self.y = 0
        self.heading = 'n'


    def turn(self, direction):
        """
        Turns the car left or right

        Args: direction (left or right)

        Affects the value of heading
        """
        
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
        """
        Moves the car forward
        
        Args: distance forward

        Affects the value of the x,y coordinates of the car
        """
        if self.heading == 'n': 
            self.y += distance
    
        elif self.heading == 's':
            self.y -= distance

        elif self.heading == 'e':
            self.x += distance

        elif self.heading == 'w':
            self.x -= distance


    def status(self):
        """
        Prints the coordinates and heading 
        """
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
