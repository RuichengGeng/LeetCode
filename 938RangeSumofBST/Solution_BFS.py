# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 22:17:48 2021

@author: Ruich
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        q = collections.deque()
        q.appendleft(root)
        _sum = 0
        while len(q) > 0:
            node = q.pop()
            if node.left is not None:
                q.appendleft(node.left)
            if node.right is not None:
                q.appendleft(node.right)
            
            if node.val >= low and node.val <= high:
                _sum += node.val
        return _sum
        