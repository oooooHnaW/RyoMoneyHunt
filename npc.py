from random import randint

class mob:
    def __init__(self, name, money_taken, msg, coord, symbol):
        self.name = name
        self.moneyChanged = money_taken
        self.msg = msg
        self.direction = 0 # 0=up, 1=right, 2=down, 3=left
        self.coord = coord
        self.symbol = symbol

    def movement(self):
        pass

class friendly:
    def __init__(self, name, add_money, msg, coord, symbol):
        self.name = name
        self.moneyChanged = add_money
        self.msg = msg
        self.direction = 0 # 0=up, 1=right, 2=down, 3=left
        self.coord = coord
        self.symbol = symbol
    
    def movement(self):
        pass

# Checks

def checkWall(object, direction):
    pass

# NPC behaviour

# Algorithmic selection of direction
def mobBehaviour(object):
    turns = 0
    turned = False
    if checkWall(object, object.direction):
        if turns == 3:
            turned = not turned
            turns = 0
        if not turned:
            object.direction += 1
            turns += 1
        else:
            object.direction -= 1
            turns += 1
# Maybe random is better?

# Random selection of direction
def mobRandomBehaviour(object):
    if checkWall(object, object.direction):
        object.direction = randint(0, 3)