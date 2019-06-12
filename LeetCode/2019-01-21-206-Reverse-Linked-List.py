# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-21 12:02:31
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-21 20:17:25


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:return None
        new_head = None
        head_next = head.next
        while head and head_next:
            head.next = new_head
            new_head = head
            head = head_next
            head_next = head_next.next
        head.next = new_head
        new_head = head
        return new_head