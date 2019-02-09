# LeetCode 295. Find Median from Data Stream

## Description

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
\[2,3,4], the median is 3

\[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.

## 描述

中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

\[2,3,4] 的中位数是 3

\[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

### 思路

* 使用python的bisect库，维护一个有序的数组.
* 每次我们返回中间值即可

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-08 13:58:09
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-08 13:58:09

# 二分搜索库
import bisect


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 声明一个数组
        self.list = []
        # 数组中元素的个数
        self.count = 0

    def addNum(self, num: 'int') -> 'None':
        # 将元素个数自增一次
        self.count += 1
        # 插入新元素
        bisect.insort_left(self.list, num)

    def findMedian(self) -> 'float':
        # 如果是奇数，返回中间值
        if self.count % 2:
            return self.list[self.count // 2]
        else:
            # 如果是偶数，返回中间两个数的平均值
            num1 = self.count // 2
            return (self.list[num1] + self.list[num1 - 1]) / 2
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-08-295-Find-Median-from-Data-Stream.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-295-find-median-from-data-stream/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
