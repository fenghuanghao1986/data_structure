# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:08:31 2018

@author: fengh
"""
# define a printer object
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    # create a tick object, to control whether currentTask is over    
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    # simply check if there is a task running            
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    # start the new task based on pagerate which been given as ppm    
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate
        

    