# LeetCode 40. Combination Sum II

## Description

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

## 描述

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

```py
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```
示例 2:

```py
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
```
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 使用深度优先搜索，进行遍历。如果路径的和为 target ，就此路径的值添加到结果数组中。
* 首先对给定的数组进行排序，为了去重复，每一层，相同的数字我们只允许使用一次。
* 结束条件为 targe 为 0。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-30 18:26:44
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-30 22:57:55

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.__dfs(0, [], res, target, candidates)
        return res

    def __dfs(self, start, path, res, target, candidates):

        # target 为 0 说明当前路径的和为目标值。
        if target == 0:
            res.append(list(path))
            return

        # 深度优先搜索，从 start 位置开始遍历。
        for i in range(start, len(candidates)):

            # 对于重复的元素，直接跳过
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            num = candidates[i]
            if num > target:
                return
            path.append(num)
            self.__dfs(i + 1, path, res, target - num, candidates)
            path.pop()

```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2018-11-30-40-Combination-Sum-II.py) 。
©本文是原创文章，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-40-combination-sum-ii/) ，作者信息和本声明.
