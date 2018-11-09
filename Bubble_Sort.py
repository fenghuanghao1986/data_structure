# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 14:57:34 2018

@author: fengh
"""

# Bubble Sort Practice
# Sort from low to high

def Bubble_sort(nums):
    swap = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j-1] <= nums[i]:
                continue
            else:
                swap = nums[j-1]
                nums[j-1] = nums[i]
                nums[i] = swap
    return nums


if __name__ == "__main__":
    nums = [1,23,3,4,5,5,6,77,5,3,2,2,34,5,5,4,32,12,2]

    print(Bubble_sort(nums))