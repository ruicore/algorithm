# LeetCode 225. Implement Stack using Queues

## Description

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false

## 描述

使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。

### 思路

* 我们使用两个队列来模拟栈,一个标记为空队列，一个标记为被填值队列.
* 当要取栈顶元素的时候，我们将被填值队列的元素取出放到空队列中，使其只剩下一个元素，这个元素就是栈顶元素，同时我们交换指向空队列和被填值队列的引用.
* 判断是否为空我们只需要检查当前被填值的队列是否为空即可.

```python
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
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-28-225-Implement-Stack-using-Queues.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/225-implement-stack-using-queues/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
