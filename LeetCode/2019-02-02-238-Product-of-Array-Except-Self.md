# LeetCode 238. Product of Array Except Self

## Description

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

## 描述

给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

### 思路

* 声明一个结果数组res，用于返回结果.
* 我们首先正向遍历数组，获取当前位置左边的数的所有乘积，即 $$ res[i] = \prod_{j=0}^{i-1} num[j] $$ 也就是  $$ res[i] = res[i-1]*nums[i-1] $$ 
* 我们声明一个辅助变量_product用于记录当前位置右边的所有数字的乘积，于是根据定义，位置i的值为（i左边所有数的乘积）与（i右边所有数的乘积）的乘积.
* 所以res\[i]= res\[i](i左边所有数的乘积\)*_product(i右边所有数的乘积\),然后我们更新_product *= nums\[i].

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-02 08:52:08
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-02 09:01:08


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 声明结果数组，第一个位置（索引0）一定要初始化为1
        res = [1 for _ in range(len(nums))]
        # 辅助变量
        _product = nums[-1]
        # 正向遍历，获取当前位置左边的所有数字乘积的值
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        # 反向遍历，_product表示当前位置右边的数所有乘积的值
        for i in range(len(nums) - 2, -1, -1):
            # 当前位置的值等与当前位置左右两边所有数的乘积
            res[i] = _product * res[i]
            _product *= nums[i]
        # 返回结果
        return res
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-02-238-Product-of-Array-Except-Self.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-238-product-of-array-except-self/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
