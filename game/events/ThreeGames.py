from game.events import GameOfGuess
import game.config as config
import time

class ThreeGuessingGame:
    def __init__(self):
        numberOfGames = 4
        numberOfFinishedGames = 4
        self.game = [None]*numberOfGames
        self.game_finished = [None]*numberOfFinishedGames
        for i in range(len(self.game)):
            self.game[i] = GameOfGuess.GuessingGame()
        for i in range(len(self.game_finished)):
            self.game_finished[i] = False
        
       
    def getRules(self):
        return "Try to guess the correct four digit code to get through"
    def allGamesDone(self):
        
        for i in range(len(self.game_finished)):
            if self.game_finished[i] == False:
                return False
        
        return True
            
        #return self.game_finished[0] and self.game_finished[1] and self.game
    def printGuessFeedback(self, guess, last_guess):
        for i in range(len(self.game)):
            if self.game_finished[i] == False:
                if self.game[i].checkGuess(guess) == 0:
                    print("That number is correct ")
                    self.game_finished[i] = True
                if self.allGamesDone() == False and last_guess == 5:
                    break
                elif self.game[i].checkGuess(guess) == 1:
                    print("Aim a little lower for this one")
                elif self.game[i].checkGuess(guess) == -1:
                    print("Aim a little higher for this one")
        
    def process(self,world):
        result = {}
        result["message"] = " THE GATE IS NOW OPEN"
        combination = []
        b = self.getRules()
        print(b)
        tries = 0

        while tries < 6 and self.allGamesDone() == False:
            guess = int(input("Make a guess: "))
            self.printGuessFeedback(guess,tries)
            if tries == 5 and self.allGamesDone() == False:
                print("You have lost, time to DIE!!")
                config.the_player.gameInProgress = False
                config.the_player.kill_all_pirates("Killed after incorrectly guessing the code to a gate")
            tries += 1
    #What values will go into our loop? or list?
        for i in range(len(self.game)):
            combination.append(self.game[i].num)

        if self.allGamesDone() == True:
            print("Congratulations! You have found the correct combination which is " ,combination)
        result["newevents"] = [ ]
        return result
  
#game = ThreeGuessingGame()
#game.playGame()
    
    
