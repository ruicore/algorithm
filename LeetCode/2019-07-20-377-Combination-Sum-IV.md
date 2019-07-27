# LeetCode 377. Combination Sum IV

## Description

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

```py
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
```

## 描述

给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:

```py
nums = [1, 2, 3]
target = 4

所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

请注意，顺序不同的序列被视作不同的组合。

因此输出为 7。
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 这道题采用动态规划。
* 声明一个数组 dp ，dp\[i] 表示使用数组 nums 中的数构成新数组，使其和为 i 的新数组的个数；
* 转移方程：dp\[i] = sum(dp\[i-num] for num in nums if i-num>=0),也就是说，为了找到使得和为 i 的所有组合，我们可以在和为 i - j 的组合后面加上一个 j，于是构成和为 i 的组合就有 dp\[i-j]组，此时 j 的取值范围是 num 数组中所有小于 i 的数。
* 我们需要将 dp\[0] 初始化为 1，表示当 i 和 j 相等的时候可以有一种组合方式。
* 结果，dp 数组的最后一个数。

```py
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            dp[i] = sum(dp[i - j] for j in nums if i - j >= 0)

        return dp[-1]
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-07-20-377-Combination-Sum-IV.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-377-combination-sum-iv/) ，作者信息和本声明.
