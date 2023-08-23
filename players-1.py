

import random
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
class RedPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
    def walk(self):
        """
        Red players move between 1 to 10 spaces, random number is used to determine on each specific call
        """
        self.position += random.randint(1, 10)
class BluePlayer(Player):
    def __init__(self, name):
        super().__init__(name)
    def walk(self):
        """
        Blue players move between 4 to 8 spaces, random number is used to determine on each specific call
        """
        self.position += random.randint(4, 8)

def play_game():
    """
    play_game creates three instances of each type of player, puts them in a list, then
    each player moves until one reaches over 100
    """
    
    #three red players created, using i to determine which number is in name
    players = [RedPlayer("RedPlayer" + str(i + 1)) for i in range(3)]
    
    #list comprehension was not working with append, so i used a simple for loop instead
    for i in range(3):
        players.append(BluePlayer("BluePlayer" + str(i + 1)))
    

    #counter and winner hold the number of times iterated and name of winning instance respectively
    counter = 0
    winner = ""
    #infinite while loop, so that the for loop can run as many times as needed until reaching 100
    while True:
        counter += 1
        for p in players:
            p.walk()
            if p.position > 100:
                #once a player reaches over 100, game ends and winner/counter are returned as a tuple
                print(p.position)
                winner = p.name
                return (winner, counter)




if __name__ == "__main__":
    print(play_game())
