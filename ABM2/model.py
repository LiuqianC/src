import random
import math
import matplotlib
from matplotlib import pyplot as plt
import operator

# Set the pseudo-random seed for reproducibility
random.seed(0)

#Create a list to store agents
agents=[]
#set a variable called n_agents
n_agents=10
#create a For loop to create 10 agents
for i in range(10):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
print(agents)
#%% set x0,y0
'''
# Initialise variable x0
x0 = random.randint(0, 99)
print("x0", x0)
# Initialise variable y0
y0 = random.randint(0, 99)
print("y0", y0)
agents.append([x0,y0])#Append to the list agents

# Change x0 and y0 randomly
rn = random.random()
print("rn", rn)
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print("x0", x0)
rn = random.random()
print("rn", rn)
if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print("y0", y0)
'''
#%% set x1,y1
'''
# Initialise variable x1
x1 = random.randint(0, 99)
print("x1", x1)
# Initialise variable y1
y1 = random.randint(0, 99)
print("y1", y1)
agents.append([x1,y1])#Append to the list agents

# Change x1 and y1 randomly
rn = random.random()
print("rn", rn)
if rn < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print("x1", x1)
rn = random.random()
print("rn", rn)
if rn < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
print("y1", y1)
'''
#%% calculate the Euclidean distance
'''
# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4
x0 = 0
y0 = 0
x1 = 3
y1 = 4
# Calculate the difference in the x coordinates.
dx = x0 - x1
# Calculate the difference in the y coordinates.
dy = y0 - y1
# Square the differences and add the squares
ssd = (dx * dx) + (dy * dy)
print("ssd", ssd)
# Calculate the square root
distance = ssd ** 0.5
print("distance", distance)
distance = math.sqrt(ssd)
print("distance", distance)
'''
#%% plot 2 dots
#Plot the agents
plt.scatter(agents[0][0], agents[0][1], color='black')
plt.scatter(agents[1][0], agents[1][1], color='black')
#Find the largest x coordinate
largest_x=agents[0][0]
red_dot=agents[0]
for point in agents:
    if point[0]> largest_x:
        largest_x=point[0]
        red_dot=point
plt.scatter(red_dot[0], red_dot[1], color='red')
plt.show()
#Get the coordinates with the largest x-coordinate
print(max(agents, key=operator.itemgetter(0)))
#%% plot 10 dots and ensure the red dot with the highest x value
#plot 10 dots
for i in range(0, 10):
    plt.scatter(agents[i][0], agents[i][1], color='black')
#Find the dot with highest x value
#initialiase max_x and red_dot
max_x=agents[0][0] #the highest x value
red_dot=agents[0] #the dot with max_x
for dot in agents: #dot = agents[i]
    if dot[0]>max_x: #dot[0] = agents[i][0]
        max_x=dot[0] #transfer the higher value to max_x
        red_dot=dot #red_dot is the dot with highest x value
plt.scatter(red_dot[0], red_dot[1], color='red') # draw the dot with red colour
#plt.show()

#%% draw blue dot which has min_x
min_x=agents[0][0]
blue_dot=agents[0]
for dot in agents:
    if dot[0]<min_x:
        min_x=dot[0]
        blue_dot=dot
plt.scatter(blue_dot[0], blue_dot[1], color='blue')
#plt.show()
#%%draw yellow dot which has max_y
max_y=agents[0][1]
yellow_dot=agents[0]
for dot in agents:
    if dot[1]>max_y:
        max_y=dot[1]
        yellow_dot=dot
plt.scatter(yellow_dot[0], yellow_dot[1], color='yellow')
#plt.show()
#%% draw green dot which has min_y
min_y=agents[0][1]
green_dot=agents[0]
for dot in agents:
    if dot[1]<min_y:
        min_y=dot[1]
        green_dot=dot
plt.scatter(green_dot[0], green_dot[1], color='green')
plt.show()