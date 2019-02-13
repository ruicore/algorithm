# LeetCode 307. Range Sum Query - Mutable

## Description

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

```py
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
```

Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

## 描述

update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。

示例:

```py
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
```

说明:

数组仅可以在 update 函数下进行修改。
你可以假设 update 函数与 sumRange 函数的调用次数是均匀分布的。

### 思路

* 这道题使用线段树，有关线段树的内容请参考[这里](https://en.wikipedia.org/wiki/Segment_tree).
```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-12 10:38:03
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-12 11:05:30


class NumArray:
    def __init__(self, nums: 'List[int]'):
        # 声明一个线段树
        self.segtree = None
        # 给定数组元素的个数
        self.size = len(nums)
        if self.size:
            # 线段树个数为原数组的两倍
            self.segtree = [0] * (self.size * 2)
            # 生成线段树
            self.__build(nums)

    def update(self, i: 'int', val: 'int') -> 'None':
        # 获取元素的真实索引
        i += self.size
        # 更新给定元素的值
        self.segtree[i] = val
        while i > 0:
            # 获取叶节点的左右节点
            left, right = i, i
            # 如果当前节点是左节点
            if i % 2 == 0:
                # 右节点是当前节点的右边一个
                right = i + 1
            # 如果当前是右节点
            else:
                # 左节点是当前节点的左边一个
                left = i - 1
            # 更新父节点
            self.segtree[i // 2] = self.segtree[left] + self.segtree[right]
            i //= 2

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        # 获取元素在树中的索引
        i += self.size
        j += self.size
        res = 0
        while i <= j:
            # 如果i是右节点
            if i % 2 != 0:
                # 加上右节点的值
                res += self.segtree[i]
                # i 指向左节点
                i += 1
            # 如果j是左节点
            if j % 2 != 1:
                # 加上左节点的值，
                res += self.segtree[j]
                # 更新j指向右节点
                j -= 1
            # i，j指向其父节点
            i //= 2
            j //= 2
        return res

    def __build(self, nums):
        # 构造线段树的函数
        for i in range(self.size):
            self.segtree[i + self.size] = nums[i]
        for i in range(self.size - 1, -1, -1):
            self.segtree[i] = self.segtree[2 * i] + self.segtree[2 * i + 1]
        return
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-12-307-Range-Sum-Query-Mutable.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-307-range-sum-query---mutable/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
