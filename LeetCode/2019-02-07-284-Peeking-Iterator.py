# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-07 14:54:12
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-08 19:00:48


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        # 我们需要用值来记录当前iterator的状态
        # self._hasNext 用于记录当前迭代器是否还有下一个值
        self._hasNext = iterator.hasNext()
        # self._next用于获取当前位置的下一个值
        self._next = iterator.next()
        # self._state存储迭代器的状态
        self._state = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        # 调用peek函数，返回迭代器第一个值
        return self._next

    def next(self):
        """
        :rtype: int
        """
        # 调用next函数，我们需要返回迭代器第一个元素
        # 并且将迭代器向后移一个来达到弹出上一个元素的效果
        current = self._next
        # 弹出迭代器的第一个元素之后，我们需要更新self._hasNext的状态
        self._hasNext = self._state.hasNext()
        # 如果还有下一个值，我们调用迭代器本身的next获取下一个值
        if self._hasNext:
            self._next = self._state.next()

        return current

    def hasNext(self):
        """
        :rtype: bool
        """
        # 返回记录当前是否有下一个值的self._hasNext
        return self._hasNext
