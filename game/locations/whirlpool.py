
''' A place of danger for the ship, player decides whether to face danger '''

from game import location
from game.context import Context
from game.display import announce
from game.player import Player
import game.config as config
from game.events import *
from game.items import Sword

import random

class Whirlpool (Context, location.Location):

    def __init__ (self, x, y, w):
        Context.__init__(self)
        location.Location.__init__(self, x, y, w)
        self.verbs['flee'] = self
        self.verbs['stay'] = self
        self.name = "whirlpool"
        self.ship = None
        self.symbol = "?"
        self.locations = {}
        self.locations["room1"] = Room1(self)
        self.locations["room2"] = Room2(self)
        self.locations["room3"] = Room3(self)
        self.locations["room4"] = Room4(self)
        self.locations["room5"] = Room5(self)
        self.starting_location = self.locations["room5"]
    def enter (self, ship):
        self.symbol = "W"
        self.ship = ship
        self.go = False
        while (self.go == False):
            print ("you have found a whirlpool, what is your command?")
            Player.get_interaction ([self])


    def visit (self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()


    def process_verb (self, verb, cmd_list, nouns):

        if (verb == "flee"):
            ''' moved to a random location in the area '''
            destx = random.randrange (-2,3) + self.x
            desty = random.randrange (-2,3) + self.y
            if (destx < 0):
                destx = 0
            if (destx >= self.world.worldsize):
                destx = self.world.worldsize - 1
            if (desty < 0):
                desty = 0
            if (desty >= self.world.worldsize):
                desty = self.world.worldsize - 1

            new_loc = self.world.get_loc (destx, desty)
            self.ship.set_loc (new_loc)
            s = self.ship
            self.ship = None
            new_loc.enter (s)
            self.go = True

        elif (verb == "stay"):
            
            if random.randint(1,3) == 3:
                config.the_player.gameInProgress = False
                config.the_player.kill_all_pirates("Drowned in the whirlpool")
                print ("The ship was destroyed in the whirlpool")
            else:
                announce ("Your ship is destroyed but you are now at a mysterious cave ")
                announce ("There is no way backward so you and your crew choose to move forward and find a way out!!")
                self.ship.process_verb ("anchor", cmd_list, nouns)
                self.ship.get_loc ().visit()
            self.go = True
            
    
    def start_day (self):
        if (self.ship != None):
            self.go = False
            while (self.go == False):
                print ("you are still at the whirlpool, what is your command?")
                Player.get_interaction ([self])
                    
class Room1(location.SubLocation):
    def __init__ (self,m):
         super().__init__(m)
         self.name = "room1"
         self.verbs['forward'] = self
         #self.verbs['back'] = self
         self.event_chance = 100
         self.events.append (venomous_scorpions.VenomousScorpions())
    def enter (self):
        announce (" You arrive at a dark passageway. You feel a tingly feeling as if you are watched by something.....")
         
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "forward"):
            config.the_player.next_loc = self.main_location.locations["room2"]

class Room2(location.SubLocation):
    def __init__ (self,m):
        super().__init__(m)
        self.name = "room2"
        self.verbs['forward'] = self
        #self.verbs['back'] = self
        self.event_chance = 100
        self.events.append (RockPaperScissorsGame.RockPaperScissors())
    def enter(self):
        announce ("You are now at a gate guarded by a dungeon master. The dungeon master won't let you in unless you best him in a game of Rock Paper Scissors")
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "forward"):
            config.the_player.next_loc = self.main_location.locations["room3"]
class Room3(location.SubLocation):
    def __init__ (self,m):
        super().__init__(m)
        self.name = "room3"
        self.verbs['forward'] = self
        #self.verbs['back'] = self
        self.event_chance = 100
        self.events.append (ThreeGames.ThreeGuessingGame())
    def enter(self):
        announce ("You arrive at a passageway lit by torches, you should probably keep going")
        announce ("OH NO! Your way is blocked by a giant gate and it requires a code to get through")
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "forward"):
            config.the_player.next_loc = self.main_location.locations["room4"]
class Room4(location.SubLocation):
    def __init__ (self,m):
        super().__init__(m)
        self.name = "room4"
        self.verbs['forward'] = self
        #self.verbs['back'] = self
        self.event_chance = 100
        self.events.append (cave_dragon.GiantCaveDragon())
    def enter(self):
        announce ("You see a light at the end of the cave, maybe you and your crew have hope after all")
        announce ("But Wait! You hear a gurgling sound.....")
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "forward"):
            config.the_player.next_loc = self.main_location.locations["room5"]
class Room5(location.SubLocation):
    def __init__ (self,m):
        super().__init__(m)
        self.name = "room5"
        self.verbs['sail'] = self
        self.item_in_treasure = Sword()
        #self.verbs['back'] = self
        #self.event_chance = 100
        #self.events.append (cave_dragon.GiantCaveDragon())
    def enter(self):
        announce ("Congarats, You and your crew have safely made it to the end of the cave")
        announce ("You have acquired a new ship and a new sword.")
        announce (" All you have go to do now is sail foward and leave this wretched cave!!!")
        #self.item_in_treasure = Sword()
        if self.item_in_treasure != None:
            config.the_player.add_to_inventory([self.item_in_treasure ])
            self.item_in_treasure = None       
        
       
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "sail"):
            #announce ("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
            config.the_player.go = True
            ''' moved to a random location in the area '''
            destx = random.randrange (-2,3) + self.main_location.x
            desty = random.randrange (-2,3) + self.main_location.y
            if (destx < 0):
                destx = 0
            if (destx >= self.main_location.world.worldsize):
                destx = self.main_location.world.worldsize - 1
            if (desty < 0):
                desty = 0
            if (desty >= self.main_location.world.worldsize):
                desty = self.main_location.world.worldsize - 1

            new_loc = self.main_location.world.get_loc (destx, desty)
            self.main_location.ship.set_loc (new_loc)
            s = self.main_location.ship
            self.main_location.ship = None
            new_loc.enter (s)
            
            
            
#Could I add a process verb here that makes them pick the item that I code.
        
        
        
        

    
