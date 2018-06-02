# -*- coding: utf-8 -*-
"""
Created on Wed May 30 12:23:09 2018

@author: fengh
"""

from pythonds.basic.deque import Deque

def palchecker(aString):
    # create a deque object
    chardeque = Deque()
    # create a loop feed string to deque object
    # one char after another from the back
    # to have O(1) time
    for ch in aString:
        chardeque.addRear(ch)
    # make it true for now as initial status    
    stillEqual = True
    # loop to compare first letter and last letter
    while chardeque.size() > 1 and stillEqual:
        # pop out letters from both ends of the deque
        # compare first and last letters
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        # once find difference
        # end loop and return False to the program
        # meaning it is not a pal letter
        if first != last:
            stillEqual = False
            
    return stillEqual
# test samples
print(palchecker("lsdkjfskf"))
print(palchecker("radar"))