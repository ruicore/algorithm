# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-12 14:46:42
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-12 14:46:42



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head
        slow, fast = head, head
        while True:
            if fast.next == None:
                return slow
            if fast.next.next == None:
                return slow.next
            slow = slow.next
            fast = fast.next.next

        return True
