import random
import time

def cpuChoice(): #determines the Computer's choice, returns 0,1/2
    choice = random.randint(0,2)
    return choice

def playerChoice(): #asks for the player's choice, returns r,p/s
    choiceMade = False
    while choiceMade == False:
        choice = str(input('Please enter your choice (r/p/s): '))
        if choice == 'r' or choice == 'p' or choice == 's':
            choiceMade = True
            return choice
        else:
            print('You have made an incorrect input!')

def theFight(user, pc): #Takes the two choices and decides who wins the round
    if user == 'r' and pc == 0: #rock and rock
        print('You both go rock! The boulders smash against each other, neither prevails!')
        winner = 0
    elif user == 'p' and pc == 1: #paper and paper
        print('You both went paper! The papers feebly battle, none doing any damage!')
        winner = 0
    elif user == 's' and pc == 2: #scissors and scissors
        print('You both choose scissors! Sparks fly as your steel blades slash against each other, neither wins!')
        winner = 0
    elif user == 'r' and pc == 2: #rock beats scissors
        print("Nice one! Out emerges your rock and you beat the opponent's scissors into dust!")
        winner = 1
    elif user == 'p' and pc == 0: #paper beats rock
        print("Excellent! The enemy shows his rock, only to be smothered by you all encompassing paper! He's powerless!")
        winner = 1
    elif user == 's' and pc == 1: #scissors beats paper
        print('Yes! Your opponent pulls out his paper, only to be slashed to pieces by your sneaky scissors!')
        winner = 1
    elif user == 'r' and pc == 1: #rock loses to paper
        print("Oh no! You take out your rock, only to be covered by the enemy's paper!")
        winner = 2
    elif user == 'p' and pc == 2: #paper loses to scissors
        print("Wrong! Your opponent chose scissors! He slices your paper to smithereens!")
        winner = 2
    elif user == 's' and pc == 0: #scissors loses to rock
        print("Oops! Your scissors are broken and mangled by the opponent's rock!")
        winner = 2
    else:
        winner = 0
    return winner

def scoreBoard(point): #adds 1 point to the round winner and decides if the game is over.
    global playerScore
    global cpuScore
    if point == 1:
        playerScore += 1
    elif point == 2:
        cpuScore += 1

    if playerScore == 3:
        winner = 1
    elif cpuScore == 3:
        winner = 2
    else:
        winner = 0
    return winner

matchWinner = 0 #Who wins the whole match. 1 is player, 2 is CPU
winFight = 0 #Who wins the round, 1 is player, 2 is CPU
playerScore = 0 #Global player score
cpuScore = 0 #Global CPU score

print('Welcome to Rock Paper Scissors!')
while matchWinner == 0: #While there is no overall winner
    while winFight == 0: #While there is no round winner
        print (f'Your score: {playerScore}     CPU score: {cpuScore}')
        userChoice = playerChoice()
        pcChoice = cpuChoice()
        winFight = theFight(userChoice, pcChoice)

    matchWinner = scoreBoard(winFight)
    winFight = 0

if matchWinner == 1:
    print("Congrats! You have vanquished your foe!")
elif matchWinner == 2:
    print("You lose! You could have at least tried!")
print('Thanks for playing!')
time.sleep(10)