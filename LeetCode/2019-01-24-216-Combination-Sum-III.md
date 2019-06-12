# LeetCode 216. Combination Sum III

## Description

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: \[\[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: \[\[1,2,6], \[1,3,5], \[2,3,4]]

## 描述

找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: \[\[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: \[\[1,2,6], \[1,3,5], \[2,3,4]]

### 思路

* 这道题使用递归求解，在元素1-9中，假设从2-8所有数中选出不重复的组合使其和为n-1的结果已经找到，我们将1放到所有的解中即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-24 06:37:54
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-26 20:38:26


class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.recursion([i for i in range(1, 10)], k, n)

    def recursion(self, nums, k, _sum):
        if k <= 0: return
        if k == 1:
            if _sum in nums: return [[_sum]]
            else: return []
        res = []
        # 递归求解
        for i in range(len(nums)):
            # 从当前元素后面位置中寻找解
            # 假设从数组nums[i + 1:]中选取k - 1个数并且使其和为_sum - nums[i]的所有组合已经找到
            # 我们将当前元素添加到结果中即可
            for item in self.recursion(nums[i + 1:], k - 1, _sum - nums[i]):
                res.append(item + [nums[i]])
        # 返回结果
        return res
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-24-216-Combination-Sum-III.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-216-combination-sum-iii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
