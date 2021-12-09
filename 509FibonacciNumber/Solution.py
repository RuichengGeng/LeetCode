# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 23:36:20 2021

@author: Ruich
"""


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        res = [0,1]
        for _ in range(n - 1):
            res.append(res[0] + res[1])
            res = res[1:]
        return res[-1]