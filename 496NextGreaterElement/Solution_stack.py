# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 21:18:54 2021

@author: Ruich
"""


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l = []
        for i in nums1:
            temp = []
            encounterI = False
            _max = -1
            while (len(nums2) > 0) and (not encounterI):
                t = nums2.pop()
                if t == i:
                    encounterI = True
                elif t > i:
                    _max = t
                temp.append(t)
                
            l.append(_max)
            while len(temp) > 0:
                nums2.append(temp.pop())
        return l
                    