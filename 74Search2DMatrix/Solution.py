# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:05:03 2021

@author: Ruich
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        column = len(matrix[0])
        left = 0 
        right = row * column - 1
        while left <= right:
            mid = int((left + right) / 2)
            i,j = (mid // column) , (mid % column) 
            if target > matrix[i][j]:
                left = mid + 1
            elif target < matrix[i][j]:
                right = mid - 1
            else:
                return True
        return False
        