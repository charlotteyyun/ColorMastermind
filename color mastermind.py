def getGuessFromUser():
    userGuess = input("Guess: ")
    return userGuess

def displayFeedback(feedback):
    print("Feedback: {0}{1}{2}{3}".format(feedback[0], feedback[1], feedback[2], feedback[3]))

def errorMessage():
    print("Error")

def finalScoreCodebreaker(numOfTurns):
    print("Score: -{0}".format(numOfTurns))


def main():

    #Test program....
    secretCode = open("input.txt","r")
    colors = ["R", "G", "Y", "P", "B", "O"]

    def evaluation():
        line = secretCode.readline()
        while line:
            rounds = 0
            while rounds < 10:
                rounds += 1
                guess = getGuessFromUser()
                if not set(guess).issubset(set(colors)) or not len(guess) == 4:
                    errorMessage()
                    rounds -= 1

                elif set(guess).issubset(set(colors)) and len(guess) == 4:
                    feedback = ['_', '_', '_', '_']
                    eliminate = []
                    for index in range(4):
                        if guess[index] == line[index]:
                            feedback[index] = line[index]
                            eliminate.append(line[index])
                    else:
                        for ind in range(4):
                            if guess[ind] in line and guess[ind] not in feedback:
                                if guess not in eliminate:
                                    feedback[guess.index(guess[ind])] = "W"


                    "".join(feedback)
                    displayFeedback(feedback)
                    if set(feedback) == set(guess):
                        finalScoreCodebreaker(rounds)
                        rounds = 0
                        line = secretCode.readline()
                    if rounds == 10:
                        finalScoreCodebreaker(rounds)
                        exit()

    evaluation()

main()
