# LeetCode 119. Pascals Triangle II

## Description

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?

## 描述

给定非负索引k，其中k≤33，返回Pascal三角形的第k个索引行。

请注意，行索引从0开始。

### 思路

* 此题同[118](https://leetcode.com/problems/pascals-triangle)非常类似，只是这一题只需要返回某一行就行.
* 我们用pre存储上一行的信息，res表示当前要计算的行即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-01 12:35:48
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-01 12:50:51


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        # pre用来存储上一行的信息
        pre = [1, 1]
        if rowIndex == 1:
            return pre
        for i in range(2, rowIndex+1):
            res = [1 for _ in range(i+1)]
            for j in range(1, i):
                res[j] = pre[j]+pre[j-1]
            # 更新上一行的信息，用于下一次计算
            pre = res
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-01-119-Pascals-Triangle-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-119-pascals-triangle-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
