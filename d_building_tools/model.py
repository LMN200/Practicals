# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:05:44 2022

@author: gylmn
"""

import random
import operator
import matplotlib

random.seed(1)
agents = []
num_of_agents = 10
num_of_iterations = 100

# Initialise agents
for i in range(num_of_agents):
    agents.append([random.randint(0,99), random.randint(0,99)])
print(agents)

for j in range(num_of_iterations):
    # Move agents
    for i in range(num_of_agents):
        # create a torus allowing agents to leave top and cappear at the bottom,
        # left to right etc.
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
    print(agents)
  
 
    '''
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)
    '''
    
    
    # Plot agents
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    for i in range(num_of_agents):
        #matplotlib.pyplot.scatter(agents[i][1],agents[i][0], c='BLUE')
        matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
    # Plot the topmost agent pink 
    topmost = max(agents, key=operator.itemgetter(0))
    matplotlib.pyplot.scatter(topmost[1],topmost[0], c='PINK')
    # Plot the leftmost agent black 
    leftmost = min(agents, key=operator.itemgetter(1))
    matplotlib.pyplot.scatter(leftmost[1],leftmost[0], c='BLACK')
    # Plot the bottommost agent green 
    bottommost = min(agents, key=operator.itemgetter(0))
    matplotlib.pyplot.scatter(bottommost[1],bottommost[0], c='GREEN')
    # Plot the rightmost agent yellow
    rightmost = max(agents, key=operator.itemgetter(1))
    matplotlib.pyplot.scatter(rightmost[1],rightmost[0], c='YELLOW')
    matplotlib.pyplot.show()
