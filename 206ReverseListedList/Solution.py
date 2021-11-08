# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 17:08:06 2021

@author: Ruich
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return 
        else:
            Node = ListNode(head.val,None)
            
        thisNode = head.next
        while thisNode is not None:
            Node = ListNode(thisNode.val,Node)
            thisNode = thisNode.next
        return Node
            