import random

class Agent:
    
    def __init__(self, environment):
        self.environment = environment
        self.store = 0
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
    
        
        
    def move(self):
        # change x coordinate
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
        # change y coordinate
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
            
            
    def eat(self):
        # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
                                                   