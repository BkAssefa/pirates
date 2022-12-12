from game import event
import random
from game.combat import Combat
from game.combat import Scorpion
from game.display import announce
import game.config as config

class VenomousScorpions (event.Event):

    def __init__ (self):
        self.name = " scorpion attack"

    def process (self, world):
        result = {}
        result["message"] = "the scorpions are dead... They look pretty tasty"
        monsters = []
        n_appearing = random.randrange(4,8)
        n = 1
        while n <= n_appearing:
            monsters.append(Scorpion("Venomous scorpion "+str(n)))
            n += 1
        announce ("The crew is attacked by venomous scorpions!!")
        Combat(monsters).combat()
        if random.randrange(2) == 0:
            result["newevents"] = [ self ]
        else:
            result["newevents"] = [ ]
        config.the_player.ship.food += n_appearing*2
        
        return result

