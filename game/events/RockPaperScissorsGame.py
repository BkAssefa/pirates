import random
from game.display import announce
import game.config as config
class RockPaperScissors:
    def __init__(self):
        self.computer_won = 0
        self.player_won = 0
    def getRules(self):
        announce ("Let's start this game shall we. If you win you pass, If you lose you DIE!!")

    def check(self, player, opponent):
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True
        return False
    def process(self,world):
        result = {}
        result["message"] = "You have bested the dungeon master, you can go through now"
        tries = 0
        self.getRules()
        while tries < 3:
            computer = random.choice(['r', 'p', 's'])
            player = input(" What is your choice?\n'r' for rock, 'p' for paper, 's' for scisssors\n")
            if computer == player:
                print("It's a tie")
                continue
            elif (player != 'r' ) and (player != 's') and (player != 'p'):
                print("That is not a valid")
                continue
            elif self.check(player, computer):
                print("You won this time")
                self.player_won += 1
           
            else:
                print("You lose this time")
                self.computer_won += 1
            
            tries += 1


        if self.player_won > self.computer_won:
            print("You have won,Congratulations!")
        elif self.computer_won > self.player_won:
            print("You lose,time to DIE!!")
            config.the_player.gameInProgress = False
            config.the_player.kill_all_pirates("Killed after loosing a game of rock paper scissors")
        result["newevents"] = [ ]
        return result
                
             

#game = RockPaperScissors()
#game.playGame()
        
        
  
