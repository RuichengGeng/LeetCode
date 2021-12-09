# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 22:11:47 2021

@author: Ruich
"""


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        _sum = nums[l]
        _min = len(nums) + 1
        while r < len(nums) and l <= r:
            if _sum < target:
                r += 1
                if r < len(nums):
                    _sum += nums[r]
            if _sum >= target:
                if r - l + 1 < _min:
                    _min = r - l + 1
                _sum -= nums[l]
                l += 1

        if _min <= len(nums):
            return _min
        else:
            return 0