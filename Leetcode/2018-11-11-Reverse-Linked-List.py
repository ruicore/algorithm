# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-11 16:22:54
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-11 16:22:54

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        new_head = None
        head_next = head.next
        while head and head_next :
            head.next = new_head
            new_head = head
            head = head_next
            head_next = head_next.next
        head.next = new_head
        new_head = head
        return new_head