# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:58:46 2021

@author: Ruich
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        result.append([])
        
        for i in range(1,len(nums) + 1):
            self.backtracking(nums,result,i,0,[])
            
        return result
    
    def backtracking(self,nums,result,length,index,subset):
        if len(subset) == length:
            temp = subset[:]
            result.append(temp)
            return
        
        for i in range(index,len(nums)):
            subset.append(nums[i])
            self.backtracking(nums,result,length,i + 1,subset)
            subset.pop()
            