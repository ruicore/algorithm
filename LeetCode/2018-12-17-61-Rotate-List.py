# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-17 12:23:54
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-17 13:01:56

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 如果head指向空或者k==0则直接返回
        if not head or k == 0:
            return head
        count, before, last = 1, head, head
        # 统计一共有多少个元素
        while before.next:
            count += 1
            before = before.next
        # before重新回到起始位置
        before = head
        # 对k进行求模运算，避免重复搬运
        k = k % count
        # 如果k求模运算结果为0，则仍然直接返回
        if k == 0:
            return head
        # last指向编号为k的元素
        for _ in range(k):
            last = last.next
        # 找到倒数第k+1个元素
        while last and last.next:
            last = last.next
            before = before.next
        # 将倒数第k+1个元素指向元素的引用赋值给res，改变倒数第k+1个元素的指向为None，将原本的last.next指向头节点
        res = before.next
        before.next = None
        last.next = head
        return res
