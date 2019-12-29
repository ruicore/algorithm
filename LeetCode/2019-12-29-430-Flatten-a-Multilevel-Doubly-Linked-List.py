# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-12-29 10:57:03
# @Last Modified by:   何睿
# @Last Modified time: 2019-12-29 11:05:17


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        current = head
        while current:
            if current.child:
                _next = current.next  # 当前节点的后一个节点
                last = current.child  # 当前节点的自节点
                while last.next:
                    last = last.next  # 如果有子节点，找到子节点的最后一个节点
                current.next = current.child
                current.next.prev = current  # 将自节点向上提高一层
                current.child = None
                last.next = _next
                if _next:
                    _next.prev = last
            current = current.next

        return head
