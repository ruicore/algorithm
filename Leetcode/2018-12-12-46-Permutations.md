# LeetCode 46. Permutations

## Description

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

## 描述

给定一组不同的整数，返回所有可能的排列。

### 思路

[递归](https://baike.baidu.com/item/%E9%80%92%E5%BD%92%E5%87%BD%E6%95%B0)

* 写好递归函数的要点是：1.确定递归关系式 2. 确定递归结束条件 3.A问题可以分解成B,C,D···Z几个子问题，假设子问题已经解决，在此情况下来解决A问题
* 此题目中，假设有一个数组A\[10],我们拿出A\[1],假设A\[1:10]\(两端的值都可以取到)组成的所有序列都已经取到，我们把A\[1]和所有的组合相加，就得到了
* 以A\[1]为首的所有可能组合
* 同理，我们把A\[2]拿出来，把A\[1]+A\[3:10]组成一个新的数组，假设此数组的所有排列组合和已经取到，再把A\[2]和它们相加，就得到了以A\[2]为首的所有组合

``` python

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 递归返回条件：只有一个值，直接返回
        if len(nums) == 1:
            return [nums]
        # 声明最终需要返回的答案
        res = []
        # 遍历数组中的元素
        for i, num in enumerate(nums):
            # 去掉已经遍历的元素
            subnum = nums[:i]+nums[i+1:]
            # 去掉元素nums[i],假设子问题subnum的所有组合已经拿到，把num[i]和所有可能的组合相加，得到结果
            for subres in self.permute(subnum):
                res.append([num]+subres)
        # 返回
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-12-46-Permutations.py)
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-46-permutations/)，欢迎转载，转载需保留文章来源，作者信息和本声明.