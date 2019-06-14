# LeetCode 368. Largest Divisible Subset

## Description

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

```py
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
```

Example 2:

```py
Input: [1,2,4,8]
Output: [1,2,4,8]
```

## 描述

给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。

如果有多个目标子集，返回其中任何一个均可。

示例 1:

```py
输入: [1,2,3]
输出: [1,2] (当然, [1,3] 也正确)
```

示例 2:

```py
输入: [1,2,4,8]
输出: [1,2,4,8]
```

### 思路

* 这道题目的做法借鉴了第 300 题 [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence) 的思路。
* 对数组从小到大排序；
* 我们首先求得在给定的数组中，满足条件的数构成的新数组的长度；然后再去求得对应的数组是什么；
* 声明一个 count 数组，count\[i] 表示给定数组 num 中，以数字 num\[i] 作为结尾能够形成的满足条件的最大数组长度； 
* 声明一个 path 数组，用于记录数字 num\[i] 的上一个有效数字的索引；
* 因为在求 count\[i] 时，我们会遍历 num\[i-1] 到 num\[0], 如果 num\[i] % num\[j] ==0 (j 的范围是 \[i-1,0]); 那么 count\[i] = max(count\[i],count\[j]+1)；并且如果 count\[j]+1 更大，说明 nums\[i] 可以追加到 num\[j] 后面，于是更新 path\[i]=j;

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-14 11:17:30
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-14 13:09:36

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []

        # max_count 用于记录满足条件的数构成的数组的最大长度
        # end 用于记录满足条件的数的最后一个数的索引
        max_count, end = 1, 0
        count, path = [1] * len(nums), [0] * len(nums)

        nums.sort()
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                # 确定数字num[i] 可以追加到前面的哪一个数字中
                if nums[i] % nums[j] == 0 and count[j] + 1 > count[i]:
                    count[i] = count[j] + 1
                    path[i] = j
            # 如果当前的数比 max_count,说明 nums[i] 是的需要的结果数组扩大了
            # 记下 i 的位置
            if count[i] >= max_count:
                max_count = count[i]
                end = i

        res = []
        for _ in range(max_count):
            res.append(nums[end])
            end = path[end]

        return res
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-06-14-368-Largest-Divisible-Subset.py) 。
©本文首发于 [何睿的博客](https://www.ruicore.cn/leetcode-368-largest-divisible-subset/) ，欢迎转载，转载需保留 文章来源 ，作者信息和本声明.
