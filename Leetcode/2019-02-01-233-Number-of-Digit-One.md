# LeetCode 233. Number of Digit One

## Description

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

## 描述

使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
说明:

你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。

### 思路

* 使用两个栈来模拟一个队列，我们使用instack来存储值，使用outstack来辅助取出值.
* 当要存储值时，我们将值压入instack栈顶.
* 当要取出队首值时，我们将instak中的所有值压入outstack中，取出outstack的栈顶值记为res，然后将outstack中的所有值在压会instack中.
* 访问队首值时，返回元素instack\[0].
* 检查队列是否为空，我们只需要检查instack是否为空.

```python
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
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-01-232-Implement-Queue-using-Stacks.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-233-number-of-digit-one/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
