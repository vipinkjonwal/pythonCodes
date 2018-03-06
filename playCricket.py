import random

possibleScores = [1,2,3,4,5,6]
totalScore = 0

def playCricket(score):
    global totalScore
    totalScore += score
    return totalScore

countPenalty = 0

while(1):

    score = int(input('Hit run: '))
    if score > 6 or score <= 0:
        # global countPenalty6

        countPenalty += 1

        if countPenalty >= 3:
            print('6 run penalty.',end='')
            totalScore -= 6
        else:
            print('1 run penalty.',end='')
            totalScore -= 1

        if totalScore < 0:
            print('Hit Wicket - You lost.')
            break
        else:
            print('Your Score is ',totalScore)
    else:
        getScore = random.choice(possibleScores)
        if score != getScore:
            print(playCricket(score))
        else:
            if totalScore == 0:
                print('Duck - You\'re Out')
            else:
                print('You\'re Out, total score is ',totalScore)
                break

