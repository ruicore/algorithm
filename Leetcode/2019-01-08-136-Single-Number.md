# LeetCode 136. Single Number

## Description

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

## 描述

### 思路

* [异或运算](https://zh.wikipedia.org/zh-hans/%E9%80%BB%E8%BE%91%E5%BC%82%E6%88%96).
* 0或1和0做异或仍然保持不变，和1做异或变为1，我么初始化为res = 0，更新res ^=i ,如果i出现了偶数次异或会的到res = 0，奇数次会得到该数本身.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-08 09:48:14
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-08 10:18:15

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res =0
        for num in nums:
            res ^=num
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-08-136-Single-Number.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-136-single-number/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
