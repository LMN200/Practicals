# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:05:44 2022
@author: gylmn
"""
# Import packages
import random
import agentframework
import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.interactive(False)

# calculate/define calculation for distance
def distance_between(a, b):
    x_distance = abs(a.x - b.x)  # default
    y_distance = abs(a.y - b.y)  # default

    # Due to torus, distance can be calculated in both directions to
    # ensure smallest distance
    if x_distance > 50:
        x_distance = 100 - x_distance

    if y_distance > 50:
        y_distance = 100 - y_distance

    round((float((x_distance ** 2) + (y_distance) ** 2)) ** 0.5, 2)

# create the environment - open list of lists
with open('in.txt', newline='') as f:
    dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = [line for line in dataset]

# # Test environment has loaded
#plt.imshow(environment)


# create agents list
agents = []

# set limits/ assign values for all functions and classes
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
breeding_distance = 10
max_number_of_rams = 2

# create figure with size limits
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# plot environment
im = ax.imshow(environment)

# Initialise agents
for i in range(num_of_agents):
    ram = True
    if i > max_number_of_rams:
        ram = False
    agents.append(agentframework.Agent(i, environment, agents, ram=ram))

print("Print out agents[1] from agents[0] as a test")

carry_on = True

# Make animation containing move, eat, share, breed
def animate(frame_number):
    print("iteration", frame_number)
    fig.clear()
    global carry_on

    # Move agents first then eat, share and breed
    for i in range(len(agents)):
        agents[i].move()  # agents can move in all directions across torus

    for i in range(len(agents)):
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood, breeding_distance)
        agents[i].age += 1

    # Stopping Condition - 90 counts yeilds roughly 90 agents (depending on last
    # breeding cycle number of lambs / distance of rams from ewes) + inital 10 agents
    stop = False
    count = 0
    for i in range(len(agents)):
        if len(agents) >= 10:
            count += 1   
        if count == 90:  # count can be increased here to run model for longer
            print("stopping condition at frame", frame_number)
            print("total number of agents =", len(agents))
            carry_on = False

    # print("After Move")
    #  # print the agents
    # for i in range(num_of_agents):
    #     #print(agents[i].x, agents[i].y)
    #     print(agents[i])

    # Plot agents onto figure - blue for rams, red for ewes (all other agents)
    plt.ylim(0, 99)
    plt.xlim(0, 99)
    plt.imshow(environment)

    for i in range(len(agents)):
        if agents[i].ram:
            c = "blue"
        else:
            c = "red"
        plt.scatter(agents[i].x, agents[i].y, c=c)
    im.set_array(environment)
    return im,


# use gen_function to start at frame 0 and add one each time to know what
# framenumber model finishes on
def gen_function(b=[0]):
    a = 0
    global carry_on
    while (a < 1000) & (carry_on):
        yield a  # Returns control and waits next call.
        a = a + 1

animation = FuncAnimation(fig, animate, frames=gen_function, repeat=False)
plt.show()

