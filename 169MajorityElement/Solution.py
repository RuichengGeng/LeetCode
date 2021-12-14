# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 23:15:57 2021

@author: Ruich
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = int(len(nums) / 2) 
        d = {}
        for i in nums:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
            
            if d[i] > num:
                return i