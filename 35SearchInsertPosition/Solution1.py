# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:12:35 2021

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
        
        while left <= right:
            mid = int((left + right) / 2)

            if target == nums[mid]:
                return mid
            elif left == right:
                if target > nums[right]:
                    return left + 1
                if target < nums[right]:
                    return left
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        return mid