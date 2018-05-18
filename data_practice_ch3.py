# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:40:49 2018

@author: fengh
"""

# queue practice

class Queue:
    def __init__(self):
        self.items = []
    # it gives me Queue object has no attribute 'items'
    # no matter if the object I created is empty or not.
    def isEmpty(self):
        return self.itmes == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
# hot potato
