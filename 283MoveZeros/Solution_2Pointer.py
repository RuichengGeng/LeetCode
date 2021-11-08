# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:11:12 2021

@author: Ruich
"""

class Solution(object):
    def first_zero_index(self,nums,start = 0):
        while start < len(nums):
            if nums[start] == 0:
                return start
            else:
                start += 1
        if start == len(nums):
            return None
        
    def first_afterzero_nonzeroindex(self,nums,firstZeroIndex):
        if firstZeroIndex is None:
            return None
        firstNoneZeroIndex = firstZeroIndex + 1
        if firstZeroIndex >= len(nums):
            return None
        while firstNoneZeroIndex < len(nums):
            if nums[firstNoneZeroIndex] != 0:
                return firstNoneZeroIndex
            else:
                firstNoneZeroIndex += 1
        if firstNoneZeroIndex == len(nums):
            return None
    
    def swap(self,nums,i,j):
        nums[i],nums[j] = nums[j],nums[i]

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        firstZeroIndex = self.first_zero_index(nums)
        if firstZeroIndex is None:
            return
        firstNoneZeroIndex = self.first_afterzero_nonzeroindex(nums,firstZeroIndex)
        if firstNoneZeroIndex is None:
            return 
        
        while firstZeroIndex is not None and firstNoneZeroIndex is not None:
            if firstNoneZeroIndex > firstZeroIndex:
                self.swap(nums,firstZeroIndex,firstNoneZeroIndex)
            firstZeroIndex = self.first_zero_index(nums,firstZeroIndex + 1)
            firstNoneZeroIndex = self.first_afterzero_nonzeroindex(nums,firstZeroIndex)
        return nums
            