# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 23:23:16 2021

@author: Ruich
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        visited = {
        }
        for i in nums:
            visited[i] = False
            
        self.backtracking(nums,result,visited,[])
        
        return result
    
    def backtracking(self,nums,result,visited,subset):
        if len(subset) == len(nums):
            result.append(subset[:])
            return
        for i in nums:
            if not visited[i]:
                subset.append(i)
                visited[i] = True
                
                self.backtracking(nums,result,visited,subset)
                
                subset.pop()
                visited[i] = False