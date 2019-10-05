# LeetCode 410. Split Array Largest Sum

## Description

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

## 描述

给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-largest-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 这道题可以使用动态规划和二分搜索来做，使用动态规划的 Python 代码会超时，因此下面使用二分搜索。
* 对于题意，当 k 等于 nums 的元素个数时，此时的最小值就是数组的最大值；当 k = 1时，此时的最小值就是整个数组的和。
* 因此，我们要求的结果一定在上面这两个值之间。
* 我们给定一个值 middle，然后我们对数组分组，使得每个组中的元素尽量多，并且其和小于等于 middle，统计总共分的的总组数 group；
* 如果 group 大于 k，说明 middle 这个值给小了，需要给一个更大的值，使得每组中容纳更多的数，使得总组数减小；
* 如果 group 小于 k，说明 middle 这个值给大了，需要给一个更小的值，使得没组中容纳更少的数，使得总组数增多；
* 如果 group 等于 k，说明此时把数组分成 k 组，每组的和都不大于 middle，此时我们尝试把 middle 减少 1，当用 middle 去划分数组有 k 组，middle -1 去划分数组大于 k 组时，middle 就是要求的结果。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-10-04 11:17:10
# @Last Modified by:   何睿
# @Last Modified time: 2019-10-05 16:13:51

from typing import List
from bisect import bisect_right


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        prefix_sum = self.sum_cumulative(nums)
        left, right, count = max(nums), prefix_sum[-1], len(nums)

        while left < right:
            middle = left + ((right - left) >> 1)
            if self.is_greater(prefix_sum, middle, m, count):
                left = middle + 1
            else:
                right = middle

        return right

    def sum_cumulative(self, nums):
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i - 1] + nums[i])

        return prefix_sum

    def is_greater(self, prefix_sum, max_num, m, count):

        pivot, start, group = max_num, 0, 0
        while start < count:
            start = bisect_right(prefix_sum, pivot, start)
            pivot = prefix_sum[start - 1] + max_num
            group += 1
            if group > m:
                return True

        return False

```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-10-04-410-Split-Array-Largest-Sum.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-410-split-array-largest-sum/) ，作者信息和本声明.
