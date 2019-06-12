# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-12 10:09:56
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-12 12:05:39


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        count = 1
        slow, fast = head, head.next
        while fast and fast.next:
            # 找到第一次相遇的节点
            if fast == slow:
                # 确定环中节点的个数
                fast = fast.next
                while fast and fast.next:
                    # 如果fast指针和slow指针相遇，说明环已经走完一趟
                    # 结束循环
                    if fast == slow:
                        break
                    # 否则count自增一次
                    count += 1
                    slow, fast = slow.next, fast.next.next
                # 重置slow和fast只想首节点
                slow, fast = head, head
                # 将fast往后移count-1个（即环中节点个数少一个节点）
                for _ in range(count - 1):
                    fast = fast.next
                while fast:
                    # 当fast.next 指向slow时，说明已经到达结尾
                    if fast.next == slow:
                        return slow
                    fast = fast.next
                    slow = slow.next
                return slow
            slow, fast = slow.next, fast.next.next
        # 如果遍历的所有节点fast和slow都不等，说明没有环
        return None
