
class Pizza():

    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
    """
    Checks number of toppings, then adds if num of toppings is valid
    """
        if len(self.toppings) == 7:
            print("Sorry, you can only have a maximum of 7 toppings")
        else:
            self.toppings.append(topping)

class Topping():

    def __init__(self, name, num_pieces):
        self.name = name
        self.num_pieces = num_pieces

    def __repr__(self):
        return "{} pieces of {}".format(self.num_pieces, self.name)


"""
Testing Pizza
"""
p1 = Pizza()
p1.add_topping("Pepperoni")
p1.add_topping("Cheese")
p1.add_topping("Mushrooms")
p1.add_topping("Beef")
p1.add_topping("Ham")
p1.add_topping("Spinach")
p1.add_topping("Garlic")

p2 = Pizza()
p2.add_topping("Pepperoni")
p2.add_topping("Cheese")
p2.add_topping("Mushrooms")
p2.add_topping("Beef")
p2.add_topping("Ham")
p2.add_topping("Spinach")
p2.add_topping("Garlic")
p2.add_topping("Mozzarella")