# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:05:44 2022
@author: gylmn
"""
# Import packages
import random
import agentframework
import csv
import matplotlib.animation
import matplotlib.backends.backend_tkagg as tkagg
import matplotlib; matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import tkinter
import requests
import bs4

plt.interactive(False)

# set up webscrapping using beautiful soup - retrieve coordinates from webpage
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html',
                 verify=False)
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class": "y"})
td_xs = soup.find_all(attrs={"class": "x"})
print(td_ys)
print(td_xs)

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
    if i > max_number_of_rams-1:
        ram = False

    if (i >= len(td_ys)):
        y = random.randint(0, 99)
        x = random.randint(0, 99)
    else:
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
        print(f'({x}, {y})')
    agents.append(agentframework.Agent(i, environment, agents, ram=ram, x=x, y=y))

# print("Print out agents[1] from agents[0] as a test")

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

    # Stopping Condition - 90 counts yeilds roughly 80 agents (depending on last
    # breeding cycle number of lambs / distance of rams from ewes) + inital 10 agents
    stop = False
    count = 0
    for i in range(len(agents)):
        if len(agents) >= 10:
            count += 1   
        if count == 90:  # count can be increased here to run model for longer
            print("stopping condition at frame", frame_number)
            print(len(agents))
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
    canvas.draw()
    # exit(9)
    return

# use gen_function to start at frame 0 and add one each time to know what
# framenumber model finishes on
def gen_function(b=[0]):
    a = 0
    global carry_on
    while (a < 1000) & (carry_on):
        yield a  # Returns control and waits next call.

        a = a + 1

# run the animation
def run():
    print('we got into run')
    anim = matplotlib.animation.FuncAnimation(fig, animate, frames=gen_function, repeat=False)
    print('we got just before draw')
    canvas.draw()
    return

# Create GUI
root = tkinter.Tk()
root.wm_title("Model")

canvas = tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu = tkinter.Menu(root)  # set up menu
root.config(menu=menu)

model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)

model_menu.add_command(label="Run model", command=run())
print('we got this far')
canvas.draw()

tkinter.mainloop()

exit(9)

