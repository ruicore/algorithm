# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-13 14:03:46
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-13 14:49:30


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 空节点或者只有一个节点直接返回
        if not head or not head.next:
            return head
        # 使用一个辅助节点
        newhead = ListNode(0)
        # 辅助节点指向头节点
        newhead.next = head
        tail, node = head, head.next
        while node:
            compare = newhead
            # 从头开始遍历找到插入的位置，插入排序是稳定的排序算法，如果节点不需要移动则不移动节点
            while compare.next.val <= node.val and compare.next != node:
                compare = compare.next
            # 移动节点
            if compare.next != node:
                tail.next = node.next
                node.next = compare.next
                compare.next = node
            # 如果当前节点不需要移动，则当前节点是尾节点，更新tail=node
            else:
                tail = node
            node = tail.next

        return newhead.next
