# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 22:10:34 2021

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
        for i in nums:
            temp = []
            for res in result:
                r = res[:] ## copy in pythonic way
                r.append(i)
                temp.append(r)
            for t in temp:
                result.append(t)
        
        return result
