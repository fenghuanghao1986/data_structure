# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 22:17:02 2018

@author: fengh
"""

# Quick sort

#def Swap(a, b):
#    temp = a
#    a = b
#    b = temp
#    return (a, b)

def Partition(nums, begin, end):
    temp = 0
    pivot = nums[end]
    
    while(begin < end) :
        if nums[begin] < pivot:
            begin += 1           
        else:
            temp = nums[end]
            nums[end] = nums[begin]
            nums[begin] = temp
        
            temp = nums[end-1]
            nums[end-1] = nums[begin]
            nums[begin] = temp
            
            print(nums[end])
#            Swap(nums[begin], pivot)
#            Swap(nums[begin], nums[end-1])
            
            end -= 1
            
    i = end
#    print(i)
#    print(nums)
    return i

def Quick_Sort(nums, begin, end):
    if begin <= end:
        p = Partition(nums, begin, end)
        Quick_Sort(nums, begin, p-1)
        Quick_Sort(nums, p+1, end)
        
    
if __name__ == "__main__":
    
    nums = [7,6,5,4,3,2,5,6,7,8,9,10,11,23,8]
#    nums = [3,3,3,3,3,3,3,5,5,5,5,5,5,5,2,2,2,2,2,2]
#    nums = [10,9,8,7,6,5,4,3,2,1]
#    nums = [1]
#    nums = [3,3,3,5,2,2,2,2]
    
    begin = 0
    end = len(nums) - 1
    Quick_Sort(nums, begin, end)
    print(nums)
    
    
    
    