# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-06 20:01:53
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-06 20:01:53

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        if not head.next:
            return True
        slow, fast, before, last = head, head, head, head.next
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = last
            last = last.next
            slow.next = before
            before = slow
        if not fast.next:
            slow = slow.next
        while last:
            if not slow.val == last.val:
               return False
            slow = slow.next
            last = last.next
        return True


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    # head.next.next = ListNode(2)
    # head.next.next.next = None
    print(Solution().isPalindrome(head))
