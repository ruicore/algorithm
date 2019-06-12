# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-01 14:30:29
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-01 14:43:18


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 如果为空或者只有一个节点，说明是回文链表
        if not head or not head.next: return True
        # 新链表1的头节点，fast指针一次走两步，新链表1的头节点，链表二的头节点
        head1, fast, before, head2 = head, head, head, head.next
        # 我们将链表的前半部分反转
        while fast and fast.next and fast.next.next:
            # fast一次走两步
            fast = fast.next.next
            # 将前面链表的节点指向链表二头节点
            head1 = head2
            # 将链表二头节点往后挪一个
            head2 = head2.next
            # 将当前节点作为链表1的头节点
            head1.next = before
            # befor指向头节点
            before = head1
        # 如果是奇数个节点，原链表的中间节点不需要匹配
        if not fast.next:
            head1 = head1.next
        while head2:
            # 只要有一个节点的值不等就返回False
            if not head1.val == head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        # 如果能够通过上面的判断，返回True
        return True
