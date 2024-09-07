'''this is a game where you can play upto 4 people
so this game is basically on luck if your dice got 0 your score will be reseted to 0
whoever reaches the score of 50 wins the match'''

import random 

def roll():
    minimum = 1
    maximum = 6
    roll = random.randint(minimum, maximum)

    return (roll)

while True:
    player = input ("Enter the number of players (2 - 4): ")
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print ("Must be between 2 - 4 players")
    else:
        print ("Invalid, Try again.")

maxscore = 50
playerscores = [ 0 for i in range(player)]

while max(playerscores) < maxscore:
    for playeri in range(player):
        print ("\nplayer", playeri + 1, "Its your turn")
        print ("you total score is: ", playerscores[playeri], "\n")
        currentscore = 0 

        while True:
            option = input ("You wanna roll or skip (y/n): ")
            if option.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                currentscore = 0
                print ("you rolled a 1, your score reseted")
                break
            else: 
                print ("you rolled a ", value)
                currentscore += value

            print ("your score is :", currentscore, "\n")

        playerscores[playeri] += currentscore
        print("Your current score is :", playerscores[playeri])

maxscored = max(playerscores)
winner = playerscores.index(maxscored)
print ("the winner is player", winner +1, "with a maximum score of", maxscore, "\n")