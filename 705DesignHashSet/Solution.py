# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 09:41:27 2021

@author: Ruich
"""


class MyHashSet(object):

    def __init__(self):
        self.set = [False] * int(1000000 + 1)

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.set[key] = True
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.set[key] = False
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.set[key]