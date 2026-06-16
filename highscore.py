highScoreFile = "items.txt"
highScore = 0

#grabs the highscore from itmes.txt
def getHighScore():
    global highScore
    with open(highScoreFile, 'r') as file:
        highScore = file.read()


def newHighScore(newScore):
    with open(highScoreFile, 'w') as file:
        file.write(newScore)