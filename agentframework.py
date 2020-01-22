
"""
Created on Fri Nov  1 14:31:36 2019

@author: ml18a22a
"""
import random

""" this file it is an algorithm that can difend the  """            
class Agent:
    
    def __init__(self, x0, y0, home, enviroment):
        self.x = x0                               ### Determine the value of the x ###
        self.y = y0                               ### Determine the value of y ###
        self.home = home                          ### Determine the agents houses ###
        self.enviroment = enviroment              ### Determine the value of the environment ###
        
    def __str__(self):
        return "x=" + str(self.x) + ",y=" + str(self.y) + "home" + str(self.home)  
    
    def move(self):
        step = random.randint(10,20)                          # to define the 'step' is maen random valeu.

        if random.random() < 0.5:                             #Gives a movement condition to the left or right if the value is less than or more than
            self.x = (self.x + step) % len (self.enviroment)  # right movement

        else:
            self.x = (self.x - step) % len (self.enviroment)  # left movement
            
        if random.random() < 0.5:                             # Gives a condition to move up or down if the value is less than or more than
            self.y = (self.y + step)  % len (self.enviroment) # ### Move down ###    

        else:
            self.y = (self.y - step)  % len (self.enviroment) # ### Move up ###

                
    def in_home(self):                                        # to defined the agents (drunkers) in home 
        return (self.y, self.x) in self.home                  # the function that agents reach the y and x value for his house
    
