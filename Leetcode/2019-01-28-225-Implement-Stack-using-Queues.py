# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-28 20:21:35
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-28 20:28:10

from collections import deque


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 声明两个队列，由于模拟栈
        self.queue1 = deque()
        self.queue2 = deque()
        # self._empty指向当前空的队列
        self._empty = self.queue1
        # self._filled指向当前有填充的队列
        self._filled = self.queue2

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        # 向有值的队列中添加值
        self._filled.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        # 检查是否有元素
        num = len(self._filled)
        if num == 0: return None
        # 我们从有值的队列中取出元素，使其只剩下一个元素
        for _ in range(num - 1):
            self._empty.append(self._filled.popleft())
        # 弹出剩下的一个元素
        item = self._filled.popleft()
        # 交换指向空队列和被填值队列的引用
        self._empty, self._filled = self._filled, self._empty
        return item

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty(): return None
        return self._filled[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self._filled) == 0
