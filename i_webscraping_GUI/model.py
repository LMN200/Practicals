# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:05:44 2022

@author: gylmn
"""
import random
import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
import tkinter
import requests
import bs4

# //ds.leeds.ac.uk/student/student14/gylmn/"Leeds Module"/Practicals
random.seed(2)

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html', verify=False)
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)


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
num_of_agents = 101
num_of_iterations = 100
neighbourhood = 20


# Initialise agents
for i in range(num_of_agents):
    #agents.append([random.randint(0,99), random.randint(0,99)])
    #agents.append(agentframework.Agent(i, environment, agents))
    if (i>= len(td_ys)):
        y = random.randint(0,99)
        x = random.randint(0,99)
    else:
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
    agents.append(agentframework.Agent(i, environment, agents, y, x))

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
    # matplotlib.pyplot.show()
    canvas.draw()


def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

# animation = matplotlib.animation.FuncAnimation(
    # fig, update, interval=1, repeat=False, frames=num_of_iterations)
# animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

# Animation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Create GUI
root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu = tkinter.Menu(root) # set up menu
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop()

for j in range(num_of_agents):
# Move agents
    for i in range(j + 1 , num_of_agents):
        distance = distance_between(agents[j], agents[i])
        # print(distance)

tkinter.mainloop()

# press enter to stop kernel
# input("Press enter to exit ;)")







