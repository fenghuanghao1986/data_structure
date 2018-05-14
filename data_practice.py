# -*- coding: utf-8 -*-
"""
Created on Fri May 11 21:48:49 2018

@author: fengh
"""
import time

def sumOfN(n):
    start = time.time()
    
    theSum = 0
    for i in range(1, n + 1):
        theSum = theSum + i
        
    end = time.time()
        
    return theSum, end-start
    
for i in range(5):
    print("Sum is %d required %10.7f seconds"%sumOfN(10000))
    

def sumOfN3(n):
    start = time.time()
    end = time.time()
    return (n*(n+1))/2, end-start

print("Sum is %d required %10.7f seconds"%sumOfN3(100000000000000000))

# this code is to use for identy whether a char in string 1
# is in string 2
def anagramSolution1(s1, s2):
    # convert string 2 to a list type of object
    # for compare one char to another
    alist = list(s2)
    # initial the position nmuber for s1
    pos1 = 0
    # as long as stillok is true, loop continues
    # which means char from s1 is in s2
    stillOK = True
    # start to compare chars one after another
    while pos1 < len(s1) and stillOK:
        # position 2 is to control the char position in s2
        pos2 = 0
        # to tell if it can find the char from s1 in s2
        found = False
        # start to compare
        while pos2 < len(alist) and not found:
            # compare char in s1 at pos1 and char in s2 at pos2
            # if not found go next pos in s2
            # if found get out from inner loop
            # go to outer loop
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1
                
        # put None to the list, i ma not sure about the size
        # so I print the len of alist, and also print the list
        # to see what does the program does
        if found:
            alist[pos2] = None
            print(len(alist))
            print(alist)
        # as long as it found the difference
        # change stillOK to Fallse, so it will no longer
        # continue the outer loop, which means two strings
        # are different
        else:
            stillOK = False
        # then position 1 should move on to the next char    
        pos1 += 1
    # once it     
    return stillOK

print(anagramSolution1('abcd', '1cba'))

def anagramSolution4(s1, s2):
    # 这个方程好牛逼！！ 感觉太妙了！
    c1 = [0] * 26
    c2 = [0] * 26
    
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
        
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1 
        
    print(c1)
    print(c2)  
     
    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOK = False
            
    return stillOK

print(anagramSolution4('asdfghjj', 'asdfghj'))
        
def test1():
    l = []
    for i in range(10000):
        l = l + [i]
        
def test2():
    l = []
    for i in range(10000):
        l.append(i)
        
def test3():
    l = [i for i in range(10000)]
    
def test4():
    l = list(range(10000))

# How to use object Timer????
t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=10000), "milliseconds")


