# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:16:39 2018

@author: fengh
"""   
from pythonds.basic.queue import Queue
# define a function take input of a list and step number
def hotPotato(namelist, num):
    # creating a Queue type object
    simqueue = Queue()
    # loop is based on names
    # since one name will be poped 
    # name list will be updated based on the number which given
    for name in namelist:
        
        simqueue.enqueue(name)
    # game will stop till there is only one name in the list    
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
            
        simqueue.dequeue()
        
    return simqueue.dequeue()

namelist = ["A", "B", "C", "D", "E"]
num = 7
print(hotPotato(namelist, num))    
    