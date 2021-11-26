# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 10:29:23 2021

@author: Ruich
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while slow is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next   
            if slow == fast:
                return True
            if fast is None:
                return False
        return False
        