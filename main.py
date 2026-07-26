from player import player
from npc import mob, friendly
from entities import coin
import os
from time import sleep, perf_counter
import keyboard
from random import randint

# Constants

coordPlaceHolder = [0,0]

W = "x" # Wall
B = " " # Blank space
RESETTEXT = "\001\033[0m\002"

WIDTH = 19
HEIGHT = 19

# Map will be 3D array 20x20?

# Map will be customisable
gameMap = [[W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
       [W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W]]

# Initialisation of characters/entities

Ryo = player("Ryo", 0, coordPlaceHolder)

mobs = [mob("Nijika", -Ryo.money, "WHY DO YOU KEEP BORROWING MONEY FROM YOUR FRIENDS???", coordPlaceHolder, "\001\033[1m\002\001\033[33m\002N"+RESETTEXT), # Ryo.money is a placeholder that means take all of Ryo's money away :)
        mob("Hiroi", -10, "heh heh, can I please borrow 10 dollars?", coordPlaceHolder, "\001\033[1m\001\033[38;2;153;0;153m\002H"+RESETTEXT)]

friendlies = [friendly("Bocchi", 10, "Ummmm, I guess it's fine if I borrow you 10 dollars?", coordPlaceHolder, "\001\033[1m\002\001\033[38;2;255;0;255m\002B"+RESETTEXT),
              friendly("Kita", 20, "OF COURSE!!! I'LL DO ANYTHING FOR RYO-SENPAI!!!", coordPlaceHolder, "\001\033[1m\002\001\033[31m\002K"+RESETTEXT)]
# Coordinates of entities are currently occupied by coordinate placeholders, will implement random selection of coordinates later on.

entities = [coin(".", 1, 60, coordPlaceHolder)] # Time in seconds

# System/Game procedures

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ms_sleep(ms):
    sleep(ms/1000)

def placeInMap(map, item):
    Coord = item.coord
    map[Coord[1]][Coord[0]] = item.symbol

def printMap(map, coins):
    for row in map:
        for element in row:
            if type(element) == str:
                print(element, end="")
            else:
                print(element.symbol)
        print()
    
    print(f"Money:${coins}")

def collideDetect(gameMap, entity, direction):
    coords = entity.coord
    if direction == "w":
        if gameMap[coords[1]-1][coords[0]] == W:
            pass
        else:
            entity.coord[1] -= 1

    elif direction == "a":
        if gameMap[coords[1]][coords[0]-1] == W:
            pass
        else:
            entity.coord[0] -= 1

    elif direction == "s":
        if gameMap[coords[1]+1][coords[0]] == W:
            pass
        else:
            entity.coord[1] += 1

    elif direction == "d":
        if gameMap[coords[1]][coords[0]+1] == W:
            pass
        else:
            entity.coord[0] += 1

def randomGeneration(map):
    y = 0
    x = 0
    y = randint(0, len(map)-1)
    x = randint(0, len(map[0])-1)
    return [x, y]

def resetMap(map):
    coords = Ryo.coord
    for row in range(len(map)-1):
        for element in range(len(map[0])-1):
            if element != coords[0] and row != coords[1] and map[row][element] == Ryo.symbol:
                map[row][element] = B

# Main game
game = True

start = perf_counter()

def randomChecker(): # Test function
    coords = randomGeneration(gameMap)
    while gameMap[coords[1]][coords[0]] != B:
        coords = randomGeneration(gameMap)

    return coords

def itemDisplay():
    placeInMap(gameMap, Ryo)
    for item in friendlies:
        placeInMap(gameMap, item)

    for item in mobs:
        placeInMap(gameMap, item)

    for item in entities:
        placeInMap(gameMap, item)

Ryo.coord = randomChecker()
for item in friendlies:
    item.coord = randomChecker()
for item in mobs:
    item.coord = randomChecker()
for item in entities:
    item.coord = randomChecker()

itemDisplay()

KeyPress = False

printMsg = ""

while game:
    if KeyPress == False:
        if keyboard.is_pressed("q"): # Detects if you want to exit
            # print(f"time elapsed: {end-start}") # Testing
            game = False
            KeyPress = True

        if keyboard.is_pressed("w"): # Movement
            KeyPress = True
            collideDetect(gameMap, Ryo, "w")

        elif keyboard.is_pressed("s"):
            KeyPress = True
            collideDetect(gameMap, Ryo, "s")
        
        # Currently - if it ain't broke, don't fix it. Will have to make it so it can detect the width of the map as well later on.
        elif keyboard.is_pressed("a"):
            KeyPress = True
            collideDetect(gameMap, Ryo, "a")
            
        elif keyboard.is_pressed("d"):
            KeyPress = True
            collideDetect(gameMap, Ryo, "d")

    # Timer

    end = perf_counter()
    try:
        time = int(end-start)
    except:
        pass

    if time == 1: # 1Hz refresh rate

        # Check collisions
        for entity in mobs:
            if Ryo.checkCollision(entity):
                entity.coord = randomChecker()
                printMsg = entity.msg
        for entity in friendlies:
            if Ryo.checkCollision(entity):
                entity.coord = randomChecker()
                printMsg = entity.msg
        for entity in entities:
            if Ryo.checkCollision(entity):
                entity.coord = randomChecker()
            
        KeyPress = False
        itemDisplay()
        resetMap(gameMap)
        clearscreen() # Clears screen
        printMap(gameMap, Ryo.money)
        print(printMsg)
        start = perf_counter()

# Initialisation

# printMap(gameMap, Ryo.money)