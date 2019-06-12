# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-25 09:44:39
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-25 11:27:30

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # 此题目是快速排序分区部分的实现，即给定一个枢纽，将数组（链表）分成左右
        # 两个部分，使得左边部分小于枢纽，右边部分大于等于枢纽
        # 数据结构为为指针的形式
        # 我们声明一个辅助的头节点
        pre = ListNode(-1)
        # 让辅助的头节点指向head头节点
        # point指向需要判断的节点，pre指向point前面一个节点
        pre.next, point = head, head
        # res用于存储结果，inplace表示已到达最终位置节点的最后一个节点
        res, inplace = pre, pre
        # 当point不为空，继续执行
        while point:
            # 如果当前位置小于枢纽，且当前位置是已经到达最终位置的节点
            # 继续执行
            if point.val < x and inplace == point or point.val >= x:
                point = point.next
                pre = pre.next
            # 如果当前位置小于枢纽，且没有到达最终位置
            else:
                # temp指向需要交换位置的节点
                temp = point
                # pre指向需要被交换节点的后面一个节点
                pre.next = temp.next
                # 被交换的节点next指针指向已经到达最终位置节点的后面一个节点
                temp.next = inplace.next
                # 已经到达最终位置的最后一节点指向被交换的节点
                inplace.next = temp
                # 记录已经到达最终位置节点的值向后挪一位
                inplace = temp
                point = pre.next

        return res.next
