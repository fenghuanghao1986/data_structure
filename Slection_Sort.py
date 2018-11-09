# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:29:38 2018

@author: fengh
"""

# Selection Sort
#From low to high

def Selection_sort(nums):
    temp = 0
    i = 0
    while(i < len(nums)):
        temp = nums[i]
        for j in range(i, len(nums)):
            if temp <= nums[j]:
                continue
            else:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp

        i += 1
    return nums

if __name__ == "__main__":
    nums = [1,23,3,4,5,5,6,77,5,3,2,2,34,5,5,4,32,12,2]

    print(Selection_sort(nums))
                