# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 21:03:19 2021

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
            idx = nums2.index(i)
            flag = -1
            while flag == -1 and idx < len(nums2) - 1:
                idx += 1
                if nums2[idx] > i:
                    flag = nums2[idx]
            l.append(flag)
        return l