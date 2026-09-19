'''The game()function in a program lets a user play a game and returns the score as an integer.
You need to read a file 'Hi-score.txt' which is either blank or containes the previous Hi-score.
You need to write a program to update the hi_score whenever the game ()function breaks the 
Hi-score '''

import random
def game():
    print("You are playing game")
    score = random.randint(1,62)

    with open("highscore.txt") as f:
        highscore = f.read()
        if (highscore!=""):
            highscore = int(highscore)
        else:
            highscore= 0
    print(f"Your score:{score}")
    if(score>highscore):
        with open("Highscore.txt","w") as f:
            f.write(str(score))
        return
game()

