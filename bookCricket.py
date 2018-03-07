import random

def playerTurn():
    playerScore = 0
    individualScore = []
    i = 1
    while (i < 11):
        randomNumber = random.choice(range(0, 10, 2))

        if randomNumber == 0:
            print('Player ',i,' is Out.','\n')
            print('Score: ',playerScore)
            individualScore.append(playerScore)
            print(individualScore)
            i += 1
        else:
            print('Scored ',randomNumber,' runs.')
            playerScore += randomNumber

    return playerScore

p1Score = playerTurn()
p2Score = playerTurn()

print('Player One Score: ',p1Score)
print('Player Two Score: ',p2Score)

if p1Score > p2Score:
    print('Player One Wins by ',p1Score - p2Score,' runs.')
elif p2Score > p1Score:
    print('Player Two Wins by ',p2Score - p1Score,' runs.')
else:
    print('Match Tied')

