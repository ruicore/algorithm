# LeetCode 260. Single Number III

## Description

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

## 描述

给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

### 实现

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-03 09:02:18
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-03 09:02:18


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0, 0]
        diff = 0
        for num in nums:
            diff ^= num
        # 制造分离因子
        diff = diff & (~(diff - 1))
        for num in nums:
            if (num & diff) == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-03-260-Single-Number-III.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-260-single-number-iii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
