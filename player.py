RESETTEXT = "\001\033[0m\002"

class player:
    def __init__(self, name, money, coord):
        self.name = name
        self.money = money
        self.direction = 0 # 0=up, 1=right, 2=down, 3=left
        self.coord = coord
        self.symbol = "\001\033[1m\002\001\033[34m\002R"+RESETTEXT # First part is ANSI escape code for bold and second part is ANSI escape code for colours and finally the character "R"
    
    def movement(self, speed):
        if self.direction == 0:
            self.coord[1] -= speed
        elif self.direction == 1:
            self.coord[0] += speed
        elif self.direction == 2:
            self.coord[1] += speed
        elif self.direction == 3:
            self.coord[0] -= speed

        # Here, movement follows pygame coordinate conventions
        # Speed can be defined as movement per tick, tick should be limited to 60fps so speed pixels per tick basically.