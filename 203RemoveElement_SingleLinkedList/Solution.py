# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:12:40 2021

@author: Ruich
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ## first remove all the head value
        if head is None:
            return
        while head.val == val:
            head = head.next
            if head is None:
                return 
            
        thisNode = head
        nextNode = head.next
        while nextNode is not None:
            if nextNode.val == val:
                thisNode.next = nextNode.next
                nextNode = nextNode.next
            else:
                thisNode = thisNode.next
                nextNode = thisNode.next
        return head
