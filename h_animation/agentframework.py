import random

class Agent:
    
    def __init__(self, i, environment, agents):
        self.i = i
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
    
    def __str__(self):
        return "i=" + str(self.i) + ", store=" + str(self.store) \
            + ", x=" + str(self.x) + ", y=" + str(self.y)
        
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
        if self.store >= 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0
            
    def share_with_neighbours(self, neighbourhood):
        # sharing with neighbours
        # Loop through the agents in self.agents .
        for i in range(len(self.agents)):
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(self.agents[i]) 
            # If distance is less than or equal to the neighbourhood
            if distance <= neighbourhood:
                # Sum self.store and agent.store .
                # Divide sum by two to calculate average.
                ave = (self.store + self.agents[i].store) / 2
                self.store = ave
                self.agents[i].store = ave
                #print("sharing " + str(distance) + " " + str(ave))
     
    def distance_between(self, b):
          """
          Calculates and returned the distance between self and b

          Parameters
          ----------
          a : TYPE
              DESCRIPTION.
          b : TYPE
              DESCRIPTION.

          Returns
          -------
          TYPE
              DESCRIPTION.

          """
          return (((self.x - b.x)**2) + ((self.y - b.y)**2))**0.5