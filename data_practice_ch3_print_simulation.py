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

# for more real simulation purpose, import random time for each task
import random

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)
    # get a timestamp when task come in 
    def getStamp(self):
        return self.timestamp
    # get page numbers of the task
    def getPages(self):
        return self.pages
    # calculate the time it may wait 
    def waitTime(self, currenttime):
        return currenttime - self.timestamp
    
from pythonds.basic.queue import Queue

import random
# define the simulation
def simulation(numSeconds, pagesPerMinute):
    # create a new printer object
    labprinter = Printer(pagesPerMinute)
    # create a queue object
    printQueue = Queue()
    # create a list type of object, for storing all waiting times for each task
    waitingtimes = []
    # unit is based on second, and numSeconds is the total time
    # for simulation, create a loop for simulation
    for currentSecond in range(numSeconds):
        # newprinttaask decides whether we want to create a new task
        # see detail in newPrintTask function defined later
        if newPrintTask():
            task = Task(currentSecond)
            # if there is a new task, put that new task to
            # the end of the queue
            printQueue.enqueue(task)    
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            # when printer is not busy or queue is empty
            # start to process next task from the top of the task queue
            nexttask = printQueue.dequeue()
            # meanwhile add the waiting time to the end of the time lise
            waitingtimes.append(nexttask.waitTime(currentSecond))
            # then start the next task pop out from the queue
            labprinter.startNext(nexttask)
        # keep counting the time till the end of the task    
        labprinter.tick()
        
    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,
                                                          printQueue.size()))
    
def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False
    
for i in range(10):
    simulation(3600, 5)
    
