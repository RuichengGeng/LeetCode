# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:16:56 2021

@author: Ruich
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1,n + 1)]
        
        result = []
        self.backtracking(nums,result,k,0,[])
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