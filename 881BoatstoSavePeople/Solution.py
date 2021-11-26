# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 17:32:35 2021

@author: Ruich
"""


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        
        front = 0
        end = len(people) - 1
        num = 0
        
        while front < end :
            if people[front] +  people[end] > limit:
                end -= 1
                num += 1
            elif people[front] +  people[end] == limit:
                end -= 1
                front += 1
                num += 1
            elif people[front] +  people[end] < limit:
                
                end -= 1
                front += 1
                num += 1
            
        if front == end:
            num += 1
            
        return num