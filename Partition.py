# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 15:23:54 2018

@author: fengh
"""

# Partition

def Partition(nums):
    temp = 0
    n = len(nums)
    i = 0
    while(i < n) :
        if nums[i] <= nums[n-1]:
            i += 1

        else:
            temp = nums[n-1]
            nums[n-1] = nums[i]
            nums[i] = temp
            temp = nums[n-2]
            nums[n-2] = nums[i]
            nums[i] = temp
            n -= 1

    return n-1


if __name__ == "__main__":
    
    nums = [7,6,5,4,3,2,5,6,7,8,9,10,11,23,8]
#    nums = [3,3,3,3,3,3,3,5,5,5,5,5,5,5,2,2,2,2,2,2]
#    nums = [10,9,8,7,6,5,4,3,2,1]
#    nums = [1]
#    nums = [3,3,3,5,2,2,2,2]
#    nums = [3,7,8,5,2,1,9,5,4]
    
    print(Partition(nums))