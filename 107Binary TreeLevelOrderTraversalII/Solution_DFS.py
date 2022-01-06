# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:33:39 2021

@author: Ruich
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is None:
            return []

        self.dfs(root,result,0)
        
        return result[::-1]
    
    def dfs(self,root,result,level):
        if root is None:
            return
        if level > len(result) - 1:
            result.append([])
        result[level].append(root.val)
        
        self.dfs(root.left,result,level + 1)
        self.dfs(root.right,result,level + 1)