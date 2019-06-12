# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-01 20:42:50
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-01 21:12:10


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 记录最后一个节点前面一个节点
        pretail = node
        # 把要删除节点的值放到最后一节点
        while node.next:
            pretail = node
            node.val, node.next.val = node.next.val, node.val
            node = node.next
        # 删除嘴后一个节点
        temp = pretail.next
        del temp
        # 最后一个节点的前一个节点next指针置为None
        pretail.next = None
