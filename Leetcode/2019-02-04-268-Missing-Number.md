# LeetCode 268. Missing Number

## Description

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

## 描述

给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

### 思路

#### 1.异或运算
* [亦或运算](https://baike.baidu.com/item/%E5%BC%82%E6%88%96).
* 由于亦或运算相同为0，不同为1，那么一个数字自己和自己做异或运算结果为0，即偶数个相同的数亦或为0，奇数个相同的数亦或为本身.
* 给定的数从0到n一共n个数（丢失了一个），我们在加一个辅助变量i从0到n，让给定的所有数和0到n的所有数字做亦或运算，则相同的数两两配对亦或为0，丢失的数只会在i中出现了一次，于是会被保留.
* 为了方便，我们让i从0到n-1,另res初始化为n，所以结果 res = nums[0] \^ nums[1] ... \^ nums[n-1] \^0 \^1 \^ ...^n,即 res ^= nums[0] ^nums[1] ... ^nums[n-1] ^0 ^1...^n-1'
  
#### 2.求和

* 0到n的和为n\*(n+1)/2,用这个和与原数组的和做差记为缺少的数字.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-04 15:30:54
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-04 16:05:54


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 位运算  0^0^1^2^2^3^3^4^4 = 1
        # 即偶数次亦或结果为0，奇数次为本身
        # 给定的数范围从0到n共n个（丢失了一个），我们然i从0自增到n-1，另res初始化为n。
        # 对所有的数进行异或运算，重复出现的数字两两配对，抑或的结果为0
        # 落单的数字亦或会被保留
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-04-268-Missing-Number.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-268-missing-number/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
