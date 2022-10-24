# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:05:44 2022

@author: gylmn
"""
import random
import operator
import matplotlib
import agentframework
import csv

# //ds.leeds.ac.uk/student/student14/gylmn/"Leeds Module"/Practicals
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
num_of_iterations = 100
neighbourhood = 20

# Animation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Initialise agents
for i in range(num_of_agents):
    #agents.append([random.randint(0,99), random.randint(0,99)])
    agents.append(agentframework.Agent(i, environment, agents))
# print agents
for i in range(num_of_agents):
    #print(agents[i].x, agents[i].y)
    print(agents[i])

print("Print out agents[1] from agents[0] as a test")
[print(agents[0].agents[1])]

carry_on = True	

# Move agents
def update(frame_number):
    
    print("iteration", frame_number)
    fig.clear()
    global carry_on
    #random.shuffle(agents) # shuffle agents
    # Move agents first then eat and share
    for i in range(num_of_agents):
        agents[i].move()
        # # create a torus allowing agents to leave top and appear at the bottom,
        # # left to right etc.
    for i in range(num_of_agents):
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    
    # # Stopping condition - Random
    # if random.random() < 0.1:
    #     carry_on = False
    #     print("stopping condition")
    
    
    # Stopping Condition - All agents food store > 20
    stop = False
    count = 0
    for i in range(num_of_agents):
        if (agents[i].store > 80):
            count = count + 1
    if count == len(agents):
        print("stopping condition at frame", frame_number)
        carry_on = False
    
    # print("After Move")
    #  # print the agents
    # for i in range(num_of_agents):
    #     #print(agents[i].x, agents[i].y)
    #     print(agents[i])
        
        
    # Plot agents
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

# animation = matplotlib.animation.FuncAnimation(
   # fig, update, interval=1, repeat=False, frames=num_of_iterations)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()


for j in range(num_of_agents):
# Move agents
    for i in range(j + 1 , num_of_agents):
        distance = distance_between(agents[j], agents[i])
       # print(distance)

# press enter to stop kernel
# input("Press enter to exit ;)")







