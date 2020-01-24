# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 17:31:45 2019

@author: a7md_

"""
"""                                              1- to call the packeges form python library                                             """
import matplotlib.pyplot                        # for graphics 
from agentframework import Agent                # for call agentframework file 
from matplotlib.animation import FuncAnimation  # to be able to create an animation graphics by import it 
from timeit import default_timer as t           # the codes from this line to line 23 from this web side:	https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python :
start = t()                                     # this code have been used to timed the cods 
end = t()
print(end - start)

"""                                              2- Creat lists  for every variable we need to bulit the project                                             """
agents = []                                  # this list is represent the Drunkers. 
enviroment = []                              # thislist represent the map. 
houses = {num:[]for num in range(10,260,10)} # this dictonary which have key for every house and that represent the drunks houses ever, and  drunker have a spesific house in the map.
in_home_agents= []                           # evey agent reach his house will be add in this list. 
fig = matplotlib.pyplot.figure()
carry_on = True


"""                                              3- Locate the Pub and Houses, and that can be work if we bulit the list and defind  the value 1 is the
                                                    pub by writing the next function and the values btween 10 to 260 mark it as house for rvery value                                              """

################################################## Locate the Pub ##################################################
with open ("drunk.plan") as file:  # to open this file we do the next :
    for y, row in enumerate(file): # the 'y' represent the lines in the raster file and  the function of 'enumerate'  to give number for every line and the general mening for this line is for every line in the row:
        row=list (eval(row))       # 'eval' function to change the line from text to number and all this line mean make list of the values in the row :
        enviroment.append(row)     # add the value in the enviroment list :
        if 1 in row:               # if the value in the row is the number 1 : 
            pub = (y,row.index(1)) # that mean every value in raster file have number 1 is pub.
    
################################################## Locate the agents(drunks) Houses ##################################################
    for y, row in enumerate(enviroment):    # the same explanation in the line 36 in this screen
        for x , value in enumerate(row):    # the 'x' represent the columns in the raster file and  the function of 'enumerate'  to give number for every columns and the general mening for this line is for every column in the columns:
            if value in houses:             
                houses[value].append((y,x)) # add the value in the list 

"""                                              4- to create the drunkers (agents) and the number of the agents should be the same number of the houses                                              """

for i in range(10,260,10):                                    # of the range for each houes 
    agents.append(Agent(pub[0],pub[1], houses[i],enviroment)) # to create agents and define a house for each agent and the start point from pub and (Agent(pub[0],pub[1], houses[i],enviroment) is to refer to the class agent in agentframework file in the def __init__. .

               

"""                                             5- Movement function                                                                      """
"""                          the coding below is to make agent move in insied the enviroment                                              """
def update(f):      # to defined the movement fumction 
    global carry_on # to refear to the 'carry_on in line line 28 in this screen 
    fig.clear()     # remove the old drawing    

     
    for agent in agents:                      # this mean for every agent in agents list 
        if enviroment[agent.y][agent.x]<=256: # if the any agent staed in the aera with a value less than 256 :
            enviroment[agent.y][agent.x]+=1   # give the area one exstra value 
        agent.move()                          # function move 
        
        if agent.in_home():              # to give a condition if the agent (drunkr) at home 
            in_home_agents.append(agent) # add the agent the  in_home_agents list
            agents.remove(agent)         # remove the agent from the old list which is it agents 
            
#######################################    the drow an colored the agents and the pub     #######################################         
             
    for agent in (agents + in_home_agents):                          # for evey agents in both lists 
        matplotlib.pyplot.scatter(agent.x, agent.y,color = "yellow") # to drow the points that represent the agents colored them in yellow. 
 
    for int in (pub):  
         matplotlib.pyplot.scatter(pub[0],pub[1],color = "red") # to drow the pointn that represent pub colored it in red 
    matplotlib.pyplot.imshow(enviroment)                             # drow the map  

    if len (agents) ==0:  # this function mean if all agents (drunks) arrive to there houses:
        carry_on = False  # give the continutiy command to stop 
     
"""                                        6-Continuity function                                                                      """  
        
def gen_function(): # to defined the iteration function 
    while carry_on: #  as long as the continutiy work : 
        yield 1     # give one movement
################################################## to save the  enviroment      
    with open ("output.txt", "w") as file: # open a new file and write :
        for row in enviroment:             # in each row in the enviroment:
            for value in row:              # for each value in the row:
                file.write(f"{value},")    # type the value in the file:
            file.write("\n")               # and create in a new row after finshing adding the row
            
            
"""                                     7- To run the animation                                                                        """                                                                                      
matplotlib.pyplot.xlim(0, len(enviroment) - 1)  #  the limit of the X in the enviroment
matplotlib.pyplot.ylim(0, len(enviroment) - 1)  #  the limit of the X in the enviroment                   
animation = FuncAnimation(fig, update, interval = 100, frames=gen_function, repeat=False ) # call the movement function to start the movements
matplotlib.pyplot.show()                        # show the plot


"""                                                 THE END                                                  """  


