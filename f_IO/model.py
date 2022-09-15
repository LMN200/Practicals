# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:05:44 2022

@author: gylmn
"""

import random
import operator
import matplotlib
import time
import agentframework
import csv

# start = time.process_time()   # //ds.leeds.ac.uk/student/student14/gylmn/"Leeds Module"/Practicals


random.seed(2)

#create the environment
environment = []
with open('in.txt', newline='') as f:
    dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset:
        rowlist = []
        for value in row:
            rowlist.append(value)
            # print(value)
        environment.append(rowlist)

# Test environment has loaded
# matplotlib.pyplot.imshow(environment)
# matplotlib.pyplot.show()



a = agentframework.Agent(environment)
print(type(a))
print(a)
# print(a.y, a.x) # 11 7
a.move()
# print(a.y, a.x) # 10 8



# def distance_between(agents_row_a, agents_row_b):
#     print(type(agents_row_a))
#     answer = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
#     print(answer)
#     return answer

def distance_between(a, b):
    """
    Calculates and returned the distance between a and b

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
    return (((a.x - b.x)**2) + ((a.y - b.y)**2))**0.5
   
    
agents = []
num_of_agents = 10
num_of_iterations = 10

# Initialise agents
for i in range(num_of_agents):
    #agents.append([random.randint(0,99), random.randint(0,99)])
    agents.append(agentframework.Agent(environment))
# print agents
for i in range(num_of_agents):
    print(agents[i].x, agents[i].y)

for j in range(num_of_iterations):
    # Move agents
    for i in range(num_of_agents):
        agents[i].move()
        # # create a torus allowing agents to leave top and cappear at the bottom,
        # # left to right etc.
        # if random.random() < 0.5:
        #     agents[i][0] = (agents[i][0] + 1) % 100
        # else:
        #     agents[i][0] = (agents[i][0] - 1) % 100
        
        # if random.random() < 0.5:
        #     agents[i][1] = (agents[i][1] + 1) % 100
        # else:
        #     agents[i][1] = (agents[i][1] - 1) % 100
        agents[i].eat()
    
    
print("After Move")
 # print the agents
for i in range(num_of_agents):
    print(agents[i].x, agents[i].y)
       
# Plot agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()
    
    
# # Plot the topmost agent pink 
# topmost = max(agents, key=operator.itemgetter(0))
# matplotlib.pyplot.scatter(topmost[1],topmost[0], c='PINK')
# # Plot the leftmost agent black 
# leftmost = min(agents, key=operator.itemgetter(1))
# matplotlib.pyplot.scatter(leftmost[1],leftmost[0], c='BLACK')
# # Plot the bottommost agent green 
# bottommost = min(agents, key=operator.itemgetter(0))
# matplotlib.pyplot.scatter(bottommost[1],bottommost[0], c='BLUE')
# # Plot the rightmost agent yellow
# rightmost = max(agents, key=operator.itemgetter(1))
# matplotlib.pyplot.scatter(rightmost[1],rightmost[0], c='YELLOW')
# matplotlib.pyplot.show()


for j in range(num_of_agents):
# Move agents
    for i in range(j + 1 , num_of_agents):
        distance = distance_between(agents[j], agents[i])
       # print(distance)

# end = time.process_time()

# print("time = " + str(end - start))

# press enter to stop kernel
# input("Press enter to exit ;)")







