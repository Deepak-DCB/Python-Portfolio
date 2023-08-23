
endG = False

while not endG:
    
#Game titles
    print("Rock Paper Scissors")

    print("Rock = r, Paper = p, Scissors = s")

#Player Decision
    player1 = input("Player 1, r, p, or s?")
    player2 = input("Player 2, r, p, or s?")
    
#Outcome
    if (player1 == player2):
        print ("Tie!")


    elif (player1 == 'r' and player2 == 's'):
        print ("Player 1 wins!")

    elif (player1 == 'p' and player2 == 'r'):
        print ("Player 1 wins!")

    elif (player1 == 's' and player2 == 'p'):
        print ("Player 1 wins!")


    elif (player1 == 's'and player2 == 'r'):
        print ("Player 2 wins!")

    elif (player1 == 'r' and player2 == 'p'):
        print ("Player 2 wins!")

    elif (player1 == 'p' and player2 == 's'):
        print ("Player 2 wins!")


    else:
        print ("One or more players did not pick a valid option")


#Prompt to end the game
    endPrompt = input("Do you want to play again? Y/N")

    if (endPrompt == 'Y'):
        endG = False

    elif (endPrompt == 'N'):
        endG = True

    else:
        endG = True
    

print("Goodbye!")