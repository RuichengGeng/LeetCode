# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 09:50:52 2021

@author: Ruich
"""


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counts = {}
        for i in s:
            if counts.get(i) is None:
                counts[i] = 1
            else:
                counts[i] += 1
        
        for i in t:
            if counts.get(i) is None:
                return i
            else:
                counts[i] -= 1
                if counts[i] < 0:
                    return i