# LeetCode 416. Partition Equal Subset Sum

## Description

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

## 描述

给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 这道题属于背包问题。
* 给定一个数组，把数组中的数分成两组，使得这两组数组的和相等，等价于：在整个数组中，每个数只可以使用一次，找这样一些数，使得这些数的和为整个数组和的一半。即备选集合为数组，包的大小为数组和的一半。
* 首先一定不能构成两个和相等的情况可以直接排除，对于一个数组 num，我们记 num 的两个子数组的和为 x，有 x + x = sum(num)，所以要求 num 的和一定是偶数，那么如果整个 num 的和是奇数，我们直接返回 False；子数组的和为 x，那么数组 num 的最大值一定小于等于 x，如果最大值大于 x（即 num 和的一半），我们直接返回 False；
* 我们对数组从小到大排序，动态规划，状态：dp\[i]\[j] 表示是否可以使用 num 的前 i（索引，包括 i） 个数，使其和为 j，
* 转移方程，对于 dp\[i]\[j],我们已经知道了 dp[i-1] 的所有情况，如果 dp\[i-1]\[j] 为 true，那么我们可以不使用第 i 个数就达到和为 j，如果dp\[i-1]\[j] 为 False，那么我们检查 dp\[i-1]\[j-num\[i]] 是否为 true，表示我们使用第 i 个数 num\[i],如果 前 i - 1 个数可以构成 j-nums[i] 的话，我们就可以使用前 i 个数使其和为 j。
* 转移方程为：dp\[i]\[j] = dp\[i - 1]\[j] if dp\[i - 1][j] else dp[i - 1][j - nums[i]]
* [可以参考这个视频](https://www.youtube.com/watch?v=s6FhG--P7z0)。

```py 
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-10-26 09:30:29
# @Last Modified by:   何睿
# @Last Modified time: 2019-10-26 10:18:19

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums & 1 or max(nums) > (sum_nums >> 1):
            return

        half_sum = sum_nums >> 1
        nums.sort(reverse=True)
        dp = [[False] * (half_sum + 1) for _ in range(2)]
        dp[0][0] = True
        dp[0][nums[0]] = True

        for i in range(1, len(nums)):
            idx = i % 2
            for j in range(nums[i]):
                dp[idx][j] = dp[idx - 1][j]
            for j in range(nums[i], half_sum + 1):
                dp[idx][j] = dp[idx - 1][j] if dp[idx - 1][j] else dp[idx - 1][j - nums[i]]
            if dp[idx][-1]:
                return True

        return dp[-1][-1]
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-10-26-416-Partition-Equal-Subset-Sum.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-416-partition-equal-subset-sum/) ，作者信息和本声明.
