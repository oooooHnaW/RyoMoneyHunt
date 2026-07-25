class coin:
    def __init__(self, symbol, money, disappearTime, coords):
        self.name = "coin"
        self.symbol = symbol
        self.moneyChanged = money
        self.disappearTime = disappearTime # Time in seconds
        self.coord = coords