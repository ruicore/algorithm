# LeetCode 347. Top K Frequent Elements

## Description

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## 描述

给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

### 思路

* 使用字典，统计每个元素出现的次数，元素为键，元素出现的次数为值。
* 然后以元素出现的次数为值，统计该次数下出现的所有的元素。
* 从最大次数遍历到 1 次，若该次数下有元素出现，提取该次数下的所有元素到结果数组中，知道提取到 k 个元素为止。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-09 12:37:36
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-09 15:57:00

from collections import Counter


class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        # 桶
        bucket = dict()
        # 构建字典，键位数字，值为该数字出现过的次数
        table = Counter(nums)
        result, count = [], 0
        # 以元素出现的次数位键，该次数下的所有元素构成的 List 为值
        for num, times in table.items():
            if times not in bucket: bucket[times] = []
            bucket[times].append(num)
        # 出现的最大次数
        maxtime = max(table.values())

        for time in range(maxtime, 0, -1):
            # 如果该次数下有元素
            if time in bucket:
                # 提取当前次数下的所有元素到结果中
                result.extend(bucket[time])
                count += len(bucket[time])
            if count == k: break
        return result
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-04-09-347-Top-K-Frequent-Elements.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-347-top-k-frequent-elements/) ，作者信息和本声明.
