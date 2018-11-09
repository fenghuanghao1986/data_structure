# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:23:26 2018

@author: fengh
"""

# Insertion Sort
# From low to high

def Insertion_sort(nums):
    temp = 0
    for i in range(len(nums)):
        for j in range(i):
            temp = nums[i]
            if temp >= nums[j]:
                continue
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            
    return nums

if __name__ == "__main__":
    nums = [1,23,3,4,5,5,6,77,5,3,2,2,34,5,5,4,32,12,2]

    print(Insertion_sort(nums))