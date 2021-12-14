# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:26:30 2021

@author: Ruich
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if len(s) == 1 or len(s) == 0:
            return s
        left = 0
        right = len(s) - 1
        while right - left >= 1:
            s[right],s[left] = s[left],s[right]
            right -= 1
            left += 1
        return s