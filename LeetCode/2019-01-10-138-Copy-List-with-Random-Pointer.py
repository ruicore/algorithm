# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-10 10:00:04
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-10 10:24:55

# Definition for singly-linked list with a random pointer.


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # 为空则直接返回
        if not head:
            return None
        # 用一个字典记录对应关系
        copydict, node = {}, head
        # 声明一个辅助头节点
        before = RandomListNode(0)
        while node:
            # 产生新的节点
            newnode = RandomListNode(node.label)
            # 将上一个节点指向当前节点
            before.next = newnode
            # 确定新旧节点之间的对应关系
            copydict[node] = newnode
            before = newnode
            # 指向下一个节点
            node = node.next
        # 为random赋值
        for key, value in copydict.items():
            value.random = copydict.get(key.random, None)
        return copydict[head]
