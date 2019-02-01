# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-01 12:53:35
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-01 14:29:28


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 用两个栈来模拟队列
        self.instack = []
        self.outstack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        # 插入队列时，我们将值放入instack栈顶
        self.instack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # 需要弹出队首的元素时
        # 我们先将instack中所有的元素弹出到outstack中
        while self.instack:
            self.outstack.append(self.instack.pop())
        # 我们取outstack中的最后一个元素
        res = self.outstack.pop()
        # 然后我们将所有outstack所有的元素放回
        while self.outstack:
            self.instack.append(self.outstack.pop())
        return res

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        # 返回栈底元素
        return self.instack[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        # 检查instack是否为空
        return not self.instack