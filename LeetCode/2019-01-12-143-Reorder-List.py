# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-12 13:02:30
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-12 18:36:00


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # 如果head为空，或者只有一个节点，或者只有两个节点都不用进行交换
        if not head or not head.next or not head.next.next:
            return
        # 第一部分：找到链表的中间值
        middle, fast = head, head
        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next

        # 第二部分将链表中间值后面的指针反转
        Head, HeadNext = None, middle.next
        middle.next = None
        while HeadNext:
            Head = HeadNext
            HeadNext = HeadNext.next
            Head.next = middle
            middle = Head
            
        # 第三部分交换指针
        node, pre = head, Head
        while pre.next:
            pre = Head.next
            Head.next = node.next
            node.next = Head
            node = Head.next
            Head = pre
        return