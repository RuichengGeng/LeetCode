# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 21:58:24 2021

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
        if root is None:
            return 0
        leftSum = self.rangeSumBST(root.left,low, high)
        rightSum = self.rangeSumBST(root.right,low, high)
        _sum = leftSum + rightSum
        if root.val >= low and root.val <= high:
            _sum += root.val
        return _sum