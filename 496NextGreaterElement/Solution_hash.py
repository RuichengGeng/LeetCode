# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 10:33:31 2021

@author: Ruich
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = [] 
        d = {}
        for ele in nums2:
            continu = True
            while len(stack) > 0 and continu:
                if ele > stack[-1]:
                    d[stack.pop()] = ele
                else:
                    continu = False
            stack.append(ele)
        while len(stack) > 0:
            d[stack.pop()] = -1
        
        l = []
        for i in nums1:
            l.append(d[i])
        return l
