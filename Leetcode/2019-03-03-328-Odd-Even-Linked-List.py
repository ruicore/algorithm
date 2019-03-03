# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-03-03 15:03:36
# @Last Modified by:   何睿
# @Last Modified time: 2019-03-03 15:59:29


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 少于两个节点的情况直接返回
        if not head or not head.next: return head
        # 记录下头节点
        oddhead, evenhead = head, head.next
        # 记录下尾节点，初始是头节点和尾节点是重合的
        oddtail, eventail = head, head.next
        node = head.next.next
        oddtail.next, eventail.next = None, None
        isodd = True
        while node:
            # 把当前节点挂到奇数链表后面
            if isodd:
                # 挂载当前节点
                oddtail.next = node
                # 剩余节点指针向后移动一个
                node = node.next
                # 尾节点向后移动一个
                oddtail = oddtail.next
                # 将尾节点的下一个节点置为空
                oddtail.next = None
                # 下一次将挂载到奇数节点后面
                isodd = False
            # 把当前节点挂到偶数节点后面
            else:
                # 挂载当前节点
                eventail.next = node
                # 剩余节点向后移动一个
                node = node.next
                # 尾节点向后移动一个
                eventail = eventail.next
                # 将尾节点的下一个节点置为空
                eventail.next = None
                # 下一次将挂载到偶数节点后面
                isodd = True
        # 偶数链将挂载到奇数链表后面
        oddtail.next = evenhead
        # 返回奇数链表的头节点
        return oddhead
