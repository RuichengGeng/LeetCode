# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:29:02 2021

@author: Ruich
"""
from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.q = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)
        
        while (len(self.q) > 0 ) and (t - self.q[0] > 3000):
            self.q.popleft()
        
        return len(self.q)
        
