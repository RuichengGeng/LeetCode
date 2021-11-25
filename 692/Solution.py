# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 19:31:11 2021

@author: Ruich
"""

import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = {}
        for i in words:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        
        heap = []
        for key,value in d.items():
            thisEle = element(key,value)
            heapq.heappush(heap,thisEle)
            if len(heap) > k :
                heapq.heappop(heap)
        
        res = []
        while len(heap) > 0:
            res.append(heapq.heappop(heap).key)
        return res[::-1]
        
        


class element:
    def __init__(self,key,count):
        self.key = key
        self.count = count
    
    def __lt__(self,ele):
        if self.count < ele.count:
            return True
        elif self.count > ele.count:
            return False
        elif self.key < ele.key:
                return False
        else:
            return True
