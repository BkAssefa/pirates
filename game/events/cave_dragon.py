from game import event
import random
from game.combat import Combat
from game.combat import Dragon
from game.display import announce
import game.config as config

class GiantCaveDragon (event.Event):

    def __init__ (self):
        self.name = " Final Boss:CaveDragon"

    def process (self, world):
        result = {}
        result["message"] = " Congratulations!!, The Giant Dragon is Defeated!!"
        monsters = []
        n_appearing = random.randrange(4,8)
        #n = 1
        #while n <= n_appearing:
        monsters.append(Dragon("Giant Cave Dragon "))
        #n += 1
        announce ("OH NO! You are attacked by a giant cave dragon!!")
        Combat(monsters).combat()
        if random.randrange(2) == 0:
            result["newevents"] = [ self ]
        else:
            result["newevents"] = [ ]
        config.the_player.ship.food += n_appearing*2
        
        return result
