# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:23:10 2021

@author: Ruich
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(','[','{']
        right = [')',']','}']
        stack = []
        for i in s[::-1]:
            if i in right:
                stack.append(i)
            elif i in left:
                indexL = left.index(i)
                if len(stack) != 0:
                    indexR = right.index(stack.pop())
                else:
                    return False
                if indexL != indexR:
                    return False
        if len(stack) != 0:
            return False
        return True