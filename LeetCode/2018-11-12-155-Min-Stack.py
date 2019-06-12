# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-12 20:28:38
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-12 21:02:47


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curmin = self.getMin()
        if curmin == None or curmin > x:
            curmin = x
        self.stack.append((x, curmin))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """

        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack)-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack)-1][1]

