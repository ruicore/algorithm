# LeetCode 284. Peeking Iterator

## Description

Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
You call next() the final time and it returns 3, the last element. 
Calling hasNext() after that should return false.
Follow up: How would you extend your design to be generic and work with all types, not just integer?

## 描述

给定一个迭代器类的接口，接口包含两个方法： next() 和 hasNext()。设计并实现一个支持 peek() 操作的顶端迭代器 -- 其本质就是把原本应由 next() 方法返回的元素 peek() 出来。

示例:

假设迭代器被初始化为列表 [1,2,3]。

调用 next() 返回 1，得到列表中的第一个元素。
现在调用 peek() 返回 2，下一个元素。在此之后调用 next() 仍然返回 2。
最后一次调用 next() 返回 3，末尾元素。在此之后调用 hasNext() 应该返回 false。
进阶：你将如何拓展你的设计？使之变得通用化，从而适应所有的类型，而不只是整数型？

### 思路

* 在继承了迭代器的基础上，我们需要记录当前迭代器的状态.
* 我们用self._hasNext来记录迭代器是否还有下一个值,用self._next来存储迭代器的下一个值，self._state来存储迭代器的状态.
* 根据题意，当调用PeekingIterator对象的peek函数的时候，我们需要返回当前的第一个元素，于是我们返回self._next，这时我们返回的仅仅是一个值，迭代器的状态并没有改变.
* 当调用PeekingIterator的next函数时，我们要返回迭代器当前的第一个元素，并且弹出第一个元素.为了达到这个效果，我们返回self._next，并且将迭代器向后移动一个.此时迭代器的状态改变，所以所有记录迭代其状态的值都要变.我们先更新self._hasNext，在self._hasNext为True的情况下，我们再更新self._next.
* PeekingIterator对象的hasNext函数直接返回self._hasNext即可.

```python
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
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-07-284-Peeking-Iterator.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-284-peeking-iterator/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
