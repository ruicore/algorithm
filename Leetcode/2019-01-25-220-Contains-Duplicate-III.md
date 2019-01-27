# LeetCode 220. Contains Duplicate III

## Description

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

## 描述

给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false

### 思路

* 这道题使用有序字典这种数据结构，使用桶排序的思想.
* 我们把把数字放到不同的桶内，桶的范围为i\*t~（i+1）\*t，于是差值为t的数一定出现在当前数字应该防止的桶内，当前桶的上一个桶，当前桶的下一个桶。我们把这三个桶的值和当前值做差，如果差值小于等于t说明存在满足题意的解，如果不存在则返回False.
* 由于所以相差为k，所以当字典中存储的数超过k个的时候，我们就可以把先插入的数字弹出.


```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-25 19:57:09
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-25 21:09:12

import collections


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or k <= 0 or t < 0: return False
        # 创建一个有序字典
        dic = collections.OrderedDict()
        for n in nums:
            # 这里使用了桶的思想
            key = n if not t else n // t
            for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            # False表示先进先出
            if len(dic) == k: dic.popitem(False)
            dic[key] = n
        return False
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-25-220-Contains-Duplicate-III.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-220-contains-duplicate-iii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
