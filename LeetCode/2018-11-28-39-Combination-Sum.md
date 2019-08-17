# LeetCode 39. Combination Sum

## Description

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

```py
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```

Example 2:

```py
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

## 描述

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

```py
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
```

示例 2:

```py
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 使用深度优先搜索，进行遍历。如果路径的和为 target ，就此路径的值添加到结果数组中。
* 为了表示路径和为 target，我们将每次的 target 减去当前遍历的元素，那么当 target 为 0 时遍历走过的路径就时题意所求。
* 首先对给定的数组进行排序，由于元素可以被重复使用，所以下一次遍历的开始位置为当前位置 i，而不是 i +1。
* 由于数组已经排序，所以如果当前元素大于 target，那么可以直接返回。
* 结束条件为 targe 为 0。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-28 18:20:58
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-18 07:11:56


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, index, path, res):

        if target == 0:
            res.append(list(path))

        for i in range(index, len(candidates)):
            if candidates[i] > target:
                return

            path.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, path, res)
            path.pop()

```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2018-11-28-39-Combination-Sum.py) 。
©本文是原创文章，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-39-combination-sum/) ，作者信息和本声明.
