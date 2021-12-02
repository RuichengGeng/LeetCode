# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:19:52 2021

@author: Ruich
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = int((left + right) / 2)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        
        if nums[left] < target:
            return left + 1
        else:
            return left