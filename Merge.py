# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 20:10:11 2018

@author: fengh
"""

# Merge Sort
# from low to high

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

if __name__ == "__main__":
    #nums1 = [1,2,3,4,5,6,7]
    #nums2 = [5,6,7,8,9,10,11,23]
    nums1 = [1]
    nums2 = [2]

    print(Merge(nums1, nums2))