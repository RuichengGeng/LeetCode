# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 23:24:16 2021

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
        res = self.fib(n - 1) + self.fib(n - 2)
        return res