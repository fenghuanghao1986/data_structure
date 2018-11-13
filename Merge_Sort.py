# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 21:58:02 2018

@author: fengh
"""

# Merge Sort

def Merge(nums1, nums2):
    i = 0
    j = 0
    
    result = []
    
    while(i<len(nums1) and j<len(nums2)):
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        elif nums2[j] < nums1[i]:
            result.append(nums2[j])
            j += 1
    if i <= len(nums1) -1:
        for k in range(i,len(nums1)):
            result.append(nums1[k])
    if j <= len(nums2) -1:
        for k in range(j,len(nums2)):
            result.append(nums2[k])     
        
    return result

def Merge_Sort(nums):
    
    n = len(nums)
    
    if n <= 1:
        return nums
    
    nums1 = Merge_Sort(nums[0:n/2])
    nums2 = Merge_Sort(nums[n/2:n])
    
    return Merge(nums1, nums2)
    
if __name__ == "__main__":

    nums = [7,6,5,4,3,2,5,6,7,8,9,10,11,23,8]
#    print(nums[0:0])
#    print(nums[0:len(nums)/2])
#    print(nums[len(nums)/2:len(nums)])

    print(Merge_Sort(nums))