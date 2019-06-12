# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-13 15:09:56
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-13 21:26:38

import math


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 如果为空或者只有一个元素则直接返回
        if not head or not head.next:
            return head
        # count表示节点个数
        count, node = 0, head
        # 获取节点的个数
        while node:
            count += 1
            node = node.next
        # res作为辅助节点
        res = ListNode(0)
        # 将res节点next指针指向头节点
        res.next = head
        tail, _next = None, None
        # 归并排序一共将执行log2(n)向上取整次
        for i in range(math.ceil((math.log(count, 2)))):
            # nums表示每次将排序的元素个数
            nums = 2**i
            # tail为辅助节点，表示已经排好序的末尾节点
            tail = res
            # _next初始化为head节点，表示下一次排序的起始节点
            _next = res.next
            while _next:
                # left 表示归并排序的第一个序列
                left = _next
                # right表示归并排序的第二个序列
                # nums为当前排序每个节点的个数
                right = self._depart(left, nums - 1)
                # _next表示下一次将要排序的起始位置
                _next = self._depart(right, nums - 1)
                # 对两个链表进行归并排序，并返回其首节点，尾节点
                sortedhead, sortedtail = self._merge(left, right)
                # 将上次排好序的尾节点与新排好序的尾节点相连
                tail.next = sortedhead
                # tail更新为新排好序的尾节点
                tail = sortedtail
        temp = res
        res = res.next
        # 删除刚才新建的辅助节点
        del temp
        return res

    def _depart(self, head, steps):
        # steps表示移动的步数
        # 对链表进行拆分操作
        node = head
        # 向后移动steps步
        while node and steps:
            node = node.next
            steps -= 1
        res = node.next if node else None
        # 切断链表
        if node: node.next = None
        # res表示下一个子链表排序的起始位置
        return res

    def _merge(self, left, right):
        # 声明一个辅助节点
        node = ListNode(0)
        tail = node
        # 当left和right都不为空才执行
        while left and right:
            # 我们让left始终指向较小值的节点
            if left.val > right.val: left, right = right, left
            # 更新tail节点的指向
            tail.next = left
            left = left.next
            tail = tail.next
        # 如果left 节点还有剩余，则将剩余节点添加到已经排序的节点末尾
        if left: tail.next = left
        # 如果right节点还有剩余，则将剩余节点添加到已经排序的节点末尾
        if right: tail.next = right
        res, tail = node.next, node
        while tail.next:
            tail = tail.next
        # 删除刚刚新建的辅助节点
        del node
        return res, tail
