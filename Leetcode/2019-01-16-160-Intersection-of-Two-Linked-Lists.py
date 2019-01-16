# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 09:55:59
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 10:10:29


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        # 获取链表的长度
        lena, lenb = self._lenList(headA), self._lenList(headB)
        a, b = headA, headB
        # 移动起始位置到节点个数相同的第一个点
        if lena > lenb:
            for _ in range(lena - lenb):
                a = a.next
        elif lenb > lena:
            for _ in range(lenb - lena):
                b = b.next
        # 同时往后面走
        while a != b:
            a, b = a.next, b.next
        return a

    # 辅助函数，获取链表的长度
    def _lenList(self, Node):
        res = 0
        while Node:
            res += 1
            Node = Node.next
        return res

    def getIntersectionNode2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        a, b = headA, headB
        # 另一种写法，为了达到从相同个数启起点，我们把a链表添加到b链表前面
        # 把b链表添加到a链表前面
        while a != b:
            if not a:
                a = headB
            elif not b:
                b = headA
            else:
                a, b = a.next, b.next
        return a
