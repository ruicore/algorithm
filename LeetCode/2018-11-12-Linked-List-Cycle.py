# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-12 14:14:34
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-12 14:42:45


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype
        """
        if  head == None or  head.next == None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if  fast == None or  fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True