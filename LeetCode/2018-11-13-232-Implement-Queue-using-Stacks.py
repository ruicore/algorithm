# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-13 20:24:25
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-13 20:45:35


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack = []
        self.outstack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.instack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.instack:
            self.outstack.append(self.instack.pop())
        res = self.outstack.pop()
        while self.outstack:
            self.instack.append(self.outstack.pop())
        return res

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.instack[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (not self.instack) and (not self.outstack)



