# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 12:14:21 2018

@author: fengh
"""

# Binary Search
    
def Binary_Search(nums, target, L, R):

    mid = (L+R)/2
    
    if L > R:
        return None
    if target == nums[mid]:
        return mid
    elif target > nums[mid]:
        L = mid
        return Binary_Search(nums, target, L+1, R)
    elif target < nums[mid]:
        R = mid
        return Binary_Search(nums, target, L, R-1) 
    
if __name__ == "__main__":
    
    nums = [1,2,3,4,5,6,7,8,9,11,22,33,44,55]
    target = 11
    L = 0
    R = len(nums) - 1
    print(Binary_Search(nums, target, L, R))