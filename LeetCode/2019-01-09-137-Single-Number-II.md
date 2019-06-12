# LeetCode 137. Single Number II

## Description

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-09 22:05:23
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-09 22:21:57


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two = 0, 0
        for num in nums:
            one = (one ^ num) & ~two
            two = (two ^ num) & ~one
        return one
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-09-137-Single-Number-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-137-single-number-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
