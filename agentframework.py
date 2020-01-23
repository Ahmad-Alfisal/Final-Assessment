
"""
Created on Fri Nov  1 14:31:36 2019

@author: ml18a22a
"""
import random

          """ 1-  this file it is an algorithm that can difend the the object we will used in the model   """            
class Agent:
    
    def __init__(self, x0, y0, home, enviroment):
        self.x = x0                               ### Determine the value of the x ###
        self.y = y0                               ### Determine the value of y ###
        self.home = home                          ### Determine the agents houses ###
        self.enviroment = enviroment              ### Determine the value of the environment ###


 
                                   """ 2- function description of the agents """
    def __str__(self):
        return "x=" + str(self.x) + ",y=" + str(self.y) + "home" + str(self.home)  
    

                       """ 3- This function is to make the movement for the agents (drunks) and will be as random  movement  """
    def move(self):                         
        step = random.randint(10,20)                          # To define the 'step' is maen random valeu.

        if random.random() < 0.5:                             # Gives a movement condition to the left or right if the value is less than or more than
            self.x = (self.x + step) % len (self.enviroment)  # Right movement

        else:
            self.x = (self.x - step) % len (self.enviroment)  # Left movement
            
        if random.random() < 0.5:                             # Gives a condition to move up or down if the value is less than or more than
            self.y = (self.y + step)  % len (self.enviroment) # Move down # 

        else:
            self.y = (self.y - step)  % len (self.enviroment) # Move up #

                      """ 4- To defined the agents (drunks) function if the arrive to thier home  """
    def in_home(self):                                         
        return (self.y, self.x) in self.home                  # The function that agents reach the y and x value for his house
    
