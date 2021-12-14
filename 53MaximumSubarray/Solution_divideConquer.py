# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 23:02:48 2021

@author: Ruich
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.get_max(nums,0,len(nums) - 1)
    
    def get_max(self,nums,left,right):
        if left == right:
            return nums[left]
        mid = int((left + right) / 2)
        leftMax = self.get_max(nums,left,mid)
        rightMax = self.get_max(nums,mid + 1,right)
        crossMax = self.get_crossmax(nums,left,right)
        return max(leftMax,rightMax,crossMax)
    
    def get_crossmax(self,nums,left,right):
        mid = int((left + right) / 2)
        leftMax = nums[mid]
        leftSum = nums[mid]
        l = mid - 1
        while l >= left:
            leftSum += nums[l]
            l -= 1
            if leftSum > leftMax:
                leftMax = leftSum
            
        rightMax = nums[mid + 1]
        rightSum = nums[mid + 1]
        r = mid + 2
        while r <= right:
            rightSum += nums[r]
            r += 1
            if rightSum > rightMax:
                rightMax = rightSum
        return rightMax + leftMax