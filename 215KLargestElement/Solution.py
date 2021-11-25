# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 16:20:54 2021

@author: Ruich
"""

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        heapq.heapify(heap)
        for i in nums:
            heapq.heappush(heap,i)
        for i in range(len(heap) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)