# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-20 21:12:46
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-20 21:23:10


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 添加一个辅助节点
        node = ListNode(0)
        node.next = head
        res = node
        while node and node.next:
            if node.next.val == val:
                temp = node.next
                node.next = temp.next
                del temp
            else:
                node = node.next
        return res.next
