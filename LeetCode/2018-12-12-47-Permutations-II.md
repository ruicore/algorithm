# LeetCode 47. Permutations II

## Description

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

## 描述

给定一组可能有重复元素不同的整数，返回所有可能的排列（不能包含重复）。

### 思路

[递归](https://baike.baidu.com/item/%E9%80%92%E5%BD%92%E5%87%BD%E6%95%B0)

* 此问题同[46题](https://www.ruicore.cn/leetcode-46-permutations/)思路，条件基本一致，只是给定的数组中可能有重复值，需要去掉.
* 假设数组A\[10],我们在遍历每个元素A\[i]的时候，都检查A\[i]是否在A\[1:i]中出现过，如果曾经出现，则直接跳过

``` python

class Solution:
    def permuteUnique(self, nums):
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
            # 检查元素是否已经出现过，若是，则直接进入下一层循环
            if i != 0 and num in nums[0:i]:
                continue
            # 去掉已经遍历的元素
            subnum = nums[:i]+nums[i+1:]
            # 去掉元素nums[i],假设子问题subnum的所有组合已经拿到，把num[i]和所有可能的组合相加，得到结果
            for subres in self.permuteUnique(subnum):
                res.append([num]+subres)
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-12-47-Permutations-II.py)
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-46-permutations/)，欢迎转载，转载需保留文章来源，作者信息和本声明.