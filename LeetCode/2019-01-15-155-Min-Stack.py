# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-15 16:40:08
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-15 17:49:45

class MinStack(object):
    # 栈中存储的是元组（当前位置的值，当前位置到栈底所有值的最小值）
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
        # 获取最小值
        curmin = self.getMin()
        if curmin == None or curmin > x:
            curmin = x
        # 存入元组
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
