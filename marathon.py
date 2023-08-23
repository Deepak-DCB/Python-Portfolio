
#MARATHON.PY

from players import Player, BluePlayer, RedPlayer, play_game as players_play_game

def play_game():
    """
    play_game creates three instances of each type of player, puts them in a list, then
    each player moves until one reaches over 1000
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
            if p.position > 1000:
                #once a player reaches over 100, game ends and winner/counter are returned as a tuple
                print(p.position)
                winner = p.name
                return (winner, counter)

if __name__ == "__main__":

    #comparing marathon and players play_game() function
    print("marathon: ")
    for i in range(5):
        print(play_game())

    print("\n Player's play_game:")
    for i in range(5):
        print(players_play_game())   