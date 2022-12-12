import random
class GuessingGame:
    def __init__(self):
        self.num = random.randint(1,10)
    def getRules(self):
        return " Enter a number from 1 to 10"
    def guessCorrect(self,guess):
        if guess == self.num:
            return True
        else:
            return False
    
    def checkGuess(self,guess):
        if guess > self.num:
            return 1
        elif guess < self.num:
            return -1
        else:
            return 0
    def playGame(self):
        print(self.getRules())
        tries = 0
        while tries <3:
            guess = int(input("Guess a number"))
            belay = self.checkGuess(guess)
            if belay == 1:
                print("Your guess is too high")
            elif belay == -1:
                print("Your guess is too low")
            else:
                print("You won")
            tries = tries + 1
        
        

    
    
    
