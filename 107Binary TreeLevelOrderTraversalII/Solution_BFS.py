# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 22:47:34 2021

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
        q = collections.deque()
        q.appendleft(root)
        
        while len(q) > 0:
            count = len(q)
            temp = []
            for _ in range(count):
                node = q.pop()
                temp.append(node.val)
                
                if node.left is not None:
                    q.appendleft(node.left)
                if node.right is not None:
                    q.appendleft(node.right) 
            result.append(temp[:])
        return result[::-1]