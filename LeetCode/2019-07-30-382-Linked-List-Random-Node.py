# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-07-30 07:41:23
# @Last Modified by:   何睿
# @Last Modified time: 2019-07-30 07:46:44

import random
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        head = self.head
        num = head.val
        node = head.next
        count = 1
        while node:
            count += 1
            if random.randint(1, count) % count == 0:
                num = node.val
            node = node.next

        return num
