# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:58:32 2022

@author: gylmn
"""

import random
import operator
import matplotlib

random.seed(1)
agents = []

# Initialise agents
agents.append([random.randint(0,99), random.randint(0,99)])
agents.append([random.randint(0,99), random.randint(0,99)])
print(agents)

# Plot agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0], c='BLUE')
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], c='BLUE')
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



'''

print(agents)
print(agents[0])
print(agents[0][0])
print(agents[0][1])

agents.append([3,4])

print(agents)

print(agents[1][1])

agents.append([5,6])


# length
print(len(agents))
print(len(agents[0]))
agents.append([7,8,9])

print(agents)

print(agents[3])
agents[3].pop(2)
print(agents[3])
print(agents)
agents[3].remove(8)
print(agents[3])
'''