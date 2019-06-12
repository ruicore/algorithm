# LeetCode 341. Flatten Nested List Iterator

## Description

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: \[\[1,1],2,\[1,1]]
Output: \[1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: \[1,1,2,1,1].
Example 2:

Input: \[1,\[4,\[6]]]
Output: \[1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: \[1,4,6].

## 描述

给定一个嵌套的整型列表。设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

列表中的项或者为一个整数，或者是另一个列表。

示例 1:

输入: \[\[1,1],2,\[1,1]]
输出: \[1,1,2,1,1]
解释: 通过重复调用 next 直到 hasNext 返回false，next 返回的元素的顺序应该是: \[1,1,2,1,1]。
示例 2:

输入: \[1,\[4,\[6]]]
输出: \[1,4,6]
解释: 通过重复调用 next 直到 hasNext 返回false，next 返回的元素的顺序应该是: \[1,4,6]。

### 思路

* 递归遍历，使用双端队列，取出每一个元素，放入到队列中
* 如果当前的元素是整型（使用自带的 isInteger 方法），将当前元素放入到队列中，如果是 List，递归调用当前函数。
* next 方法从队列中不断取出元素

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-08 14:01:53
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-08 14:45:23

from collections import deque


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = deque()
        # 遍历得到所有的元素
        self._get_elements(nestedList)
        # 统计元素的个数
        self.count = len(self.queue)

    def _get_elements(self, nestedList):
        for item in nestedList:
            # isInteger 方法是 NestedIterator 类提供的方法
            # 如果是整型，将该数组添加到双端队列中
            if item.isInteger():
                self.queue.append(item.getInteger())
                # 如果是一个 List ，递归调用 _get_elements
            else:
                self._get_elements(item.getList())
        return

    def next(self):
        """
        :rtype: int
        """
        hasnext = self.hasNext()
        if hasnext:
            self.count -= 1
            # 返回下一个元素
            return self.queue.popleft()
        return False

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.count > 0
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-04-08-341-Flatten-Nested-List-Iterator.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-341-flatten-nested-list-iterator/) ，作者信息和本声明.
