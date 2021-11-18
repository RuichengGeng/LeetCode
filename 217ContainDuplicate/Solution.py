# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 09:41:57 2021

@author: Ruich
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in nums:
            if d.get(i) is None:
                d[i] = True
            else:
                return True
        return False