# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-23 17:06:54
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-23 19:49:13

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        isclear, pre, point = False, head, head.next
        if head.val == head.next.val:
            isclear = True
        while point and point.next:
            # 用于记录当前值是否需要清除
            if point.val == point.next.val:
                # 清除point后面所有和point相同值的元素
                while point.next and point.val == point.next.val:
                    # 指向需要删除的节点
                    temp = point.next
                    # 删除该节点
                    point.next = temp.next
                    temp.next = None
                # 清除point元素本身
                # pre的nexe指针指向point后面一个元素
                pre.next = point.next
                # point指向下一个元素
                point = point.next
                continue
            point = point.next
            pre = pre.next
        # 如果序列第一个元素和第二个元素相等，去掉这两个元素
        # 在上面的循环中，如果只有两个元素或者第三个元素与第二个元素不等，都会导致前两个相同的元素不被删除
        if head and head.next and head.val == head.next.val:
            return head.next.next
        # 在上面的循环中，如果第一个出现了重复，且重复次数超过2（即至少前三个元素相同），会把第一个元素后面重复的元素删除，其本身不会被删除
        elif isclear:
            return head.next
        # 其他情况，直接返回head
        else:
            return head


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(1)
    a.next = b
    c = ListNode(2)
    b.next = c
    c.next = None
    # d = ListNode(3)
    # c.next = d
    # e = ListNode(4)
    # d.next = e
    # f = ListNode(4)
    # e.next = f
    # g = ListNode(5)
    # f.next = g
    # g.next = None
    so = Solution()
    res = so.deleteDuplicates(a)
    head = res
    while head:
        print(head.val)
        head = head.next
