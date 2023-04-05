# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:17:45 2023

@author: ASUS
"""

import random
import matplotlib
matplotlib.use('TkAgg')
import tkinter as tk
from matplotlib import pyplot as plt
import operator
import my_modules.io as io
import my_modules.agentframework as af
import my_modules.geometry as gm
import imageio
import os
import matplotlib.animation as anim
import requests
import bs4

#%%FUNCTIONS

#Define a function to calcuate the max distance
def get_max_distance():
    '''
    Calculate the max distance among these points
    
    Parameters
    ----------
    agents: list
        The list which contains ten dots coordinate pair

    Returns
    -------
    max_distance: Number
        The max distance between two farest points

    '''
    max_distance = 0 # initialise the max_distance variable
    for i in range(len(agents)): # a loop to split agents' line list
        a = agents[i] #a is a list
        for j in range(len(agents)): # a loop to split value in line
            b = agents[j] #b is a number variable
            distance = gm.get_distance(a.x, a.y, b.x, b.y) # calculation
            max_distance = max(max_distance, distance) # update max_distance
    #print("max_distance", max_distance)
    return max_distance

#Define a function to add up the total environment 
def addup_environment():
    '''
    

    Returns
    -------
    sum_env : float
        A number variable to show total environment.
    '''
    sum_env = 0 #initialise sum_env: the total environment
    for i in range(len(environment)): # locate the row number 
        for j in range(len(environment[i])): # locate the column number 
            sum_env += environment[i][j] # extend total: sum = sum + number
    return sum_env

#Define a function to add up the total agents' store
def addup_store():
    '''
    

    Returns
    -------
    sum_store : float
        A number variable to show total agents' store.

    '''
    sum_store = 0 # initialise sum_store: the total agents' store
    for i in range(len(agents)): # locate agents index
        sum_store += agents[i].store #extend the sum_store: sum = sum + number
    return sum_store

#Define a function to plot
def plot():
    '''
    

    Returns
    -------
    fig :  `~matplotlib.figure.Figure`
         The figure object used to get needed events, such as draw or resize.

    '''
    fig.clear() # clear fig
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max) #set the axes/ x-y axis
    plt.imshow(environment) #show the environment image (something like DEM)
    for i in range(n_agents):# plot agents points
        plt.scatter(agents[i].x, agents[i].y, color='black')
    # Plot the coordinate with the largest x red
    lx = max(agents, key=operator.attrgetter('x'))
    plt.scatter(lx.x, lx.y, color='red')
    # Plot the coordinate with the smallest x blue
    sx = min(agents, key=operator.attrgetter('x'))
    plt.scatter(sx.x, sx.y, color='blue')
    # Plot the coordinate with the largest y yellow
    ly = max(agents, key=operator.attrgetter('y'))
    plt.scatter(ly.x, ly.y, color='yellow')
    # Plot the coordinate with the smallest y green
    sy = min(agents, key=operator.attrgetter('y'))
    plt.scatter(sy.x, sy.y, color='orange')
    #save the images
    global ite
    filename = '../../data/output/images/image' + str(ite) + '.png' 
    plt.savefig(filename)#export the output image
    plt.show()#demostrate the image in plots pane or in pop-up windows
    images.append(imageio.imread(filename))#store the image in list'images[]'
    return fig 
    
#Difine a function to update(move) agents
def update(frames):
    '''
    

    Parameters
    ----------
    frames : int
        A variable to define the number of iterations.

    Returns
    -------
    None.

    '''
    global carry_on #'carry_on' is a bool variable used to determine whether 
                    #the iteration should go on
    print("Iteration", frames)#frames is the number of this iteration
    # Move agents
    print("Move and eat")
    for i in range(len(agents)):# every agents point do move and eat
        agents[i].move(x_min, y_min, x_max, y_max)
        agents[i].eat()
        #print(agents[i])
    # Share store
    print("Share")
    # Distribute shares
    for i in range(n_agents):
        agents[i].share(neighbourhood)
    # Add store_shares to store and set store_shares back to zero
    for i in range(n_agents):
        #print(agents[i])
        agents[i].store = agents[i].store_shares
        agents[i].store_shares = 0
    #print(agents)
    # Print the maximum distance between all the agents
    print("Maximum distance between all the agents", get_max_distance())
    # Print the total amount of resource
    sum_as = addup_store()
    print("sum_agent_stores", sum_as)
    sum_e = addup_environment()
    print("sum_environment", sum_e)
    print("total resource", (sum_as + sum_e))

    # Stopping condition
    # Random
    #if random.random() < 0.1:
    #Alter the stopping condition so that the model stops when the average 
    #agent store is greater than 80.
    if sum_as / n_agents > 80:
        carry_on = False
        print("stopping condition")

    # Plot
    global ite
    plot()
    #ite = ite + 1
    
#Define a generator function
def gen_function():
    '''
        This function is used as a generator in matplotlib.FunAnimation.
        
        Process: 
            1.The first thing is to check whether should program enter while 
            loop. 
            2.As the conditions are met, the 'ite'(the variable behind 'yield') 
            returns to the main function and then the main function runs. 
            3. After runing the main function, the program comes back to while 
            loop and continue to run the next line below 'yield', which is 
            'ite + 1' in this generator. 
            4.As completing the assignment, the while loop check the conditions
            again.
            5.So the loop runs again and again until the conditions are not met.
        
        When the loop is over, the programme runs next lines and stop this
        generator function.

    '''
    global ite
    global carry_on
    while (ite <= n_iterations) & (carry_on) :
        yield ite # Returns control and waits next call.
        ite = ite + 1
    global data_written
    if data_written == False:
        # Set the Write data menu to normal.
        menu_0.entryconfig("Write data", state="normal")
        data_written = True
        
def run(canvas):
    animation = anim.FuncAnimation(fig, update, init_func=plot, frames=gen_function, repeat=False)
    animation.new_frame_seq()
    canvas.draw()
    
def output():
    # Write data
    print("write data")
    io.write_data('../../data/output/out.txt', environment)
    imageio.mimsave('../../data/output/out.gif', images, fps=3)   
    
def exiting():
    """
    Exit the program.
    """
    root.quit()
    root.destroy()
    #sys.exit(0)

    
#%% mainbody
if __name__ == '__main__':
    #%%INPUT
    #read the data from local path
    n_rows,n_cols,environment=io.read_data('../../data/input/in.txt')

    #%%VARIABLES INITIALISE
    # Set the pseudo-random seed for reproducibility
    random.seed(0)

    # A variable to store the number of agents
    n_agents = 10

    # A variable to store the number of iterations
    n_iterations = 10

    # Variables for constraining movement.
    # The minimum x coordinate.
    x_min = 0
    # The minimum y coordinate.
    y_min = 0
    # The maximum an agents x coordinate is allowed to be.
    x_max = n_cols - 1
    # The maximum an agents y coordinate is allowed to be.
    y_max = n_rows - 1

    # A variable to store the constraint of neighbours
    neighbourhood = 50

    #%%AGENTS INITIALISE
    # Initialise agents

    url = 'https://agdturner.github.io/resources/abm9/data.html'
    r = requests.get(url, verify=False)
    content = r.text
    soup = bs4.BeautifulSoup(content, 'html.parser')
    td_ys = soup.find_all(attrs={"class" : "y"})
    td_xs = soup.find_all(attrs={"class" : "x"})
    print(td_ys)
    print(td_xs)
    agents = []
    for i in range(n_agents):
        # Create an agent
        y = int(td_ys[i].text) + 99
        x = int(td_xs[i].text) + 99
        agents.append(af.Agent(agents, i, environment, n_rows, n_cols, x, y))
        print(agents[i].agents[i])

   
    #%% MOVE AGENTS
    #Create directory to write images to
    try:
        os.makedirs('../../data/output/images/')
    except FileExistsError: #if the directory has already existed
        print("path exists")
    global ite                    
    ite = 0 #initialise ite as 0
    images = [] #create a list to store generated plots
     # Animate
     # Initialise fig and carry_on
    #for ite in range(n_iterations):
    fig = matplotlib.pyplot.figure(figsize=(7, 7)) #define the plot size as 7*7 inches
    ax = fig.add_axes([0, 0, 1, 1])
    carry_on = True
    data_written = False
    # GUI
    root = tk.Tk()
    root.wm_title("Agent Based Model")
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    menu_0 = tk.Menu(menu_bar)
    menu_bar.add_cascade(label="Model", menu=menu_0)
    menu_0.add_command(label="Run model", command=lambda: run(canvas))
    menu_0.add_command(label="Write data", command=lambda: output())
    menu_0.add_command(label="Exit", command=lambda: exiting())
    menu_0.entryconfig("Write data", state="disabled")
    # Exit if the window is closed.
    root.protocol('WM_DELETE_WINDOW', exiting)
    tk.mainloop()
    '''
    anim.FuncAnimation(fig, update, frames=gen_function, init_func=plot, repeat=False):
        Process:
            1.init_function=plot: generate the first image (ite = 0).
            2.frames=gen_function: ite = 1
            3.update: agents move once, a plot with movement is exported
            4.frames=gen_function: ite = 2
            5.update: agents move once more, a plot with movement is exported 
            ...
            Program meets stopping conditions so gen_function stops while loop.
            gen_function exports txt file and a gif.
    '''



