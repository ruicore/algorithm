# LeetCode 312. Burst Balloons

## Description

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

* You may imagine nums\[-1] = nums\[n] = 1. They are not real therefore you can not burst them.
* 0 ≤ n ≤ 500, 0 ≤ nums\[i] ≤ 100

Example:

```py
Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
```

## 描述

有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

说明:

* 你可以假设 nums\[-1] = nums\[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
* 0 ≤ n ≤ 500, 0 ≤ nums\[i] ≤ 100

示例:

```py
输入: [3,1,5,8]
输出: 167 
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
```

### 思路

* 这道题使用动态规划。
* 状态：我们声明一个二维数组 matrix\[len(nums)]\[len(nums)]，matrix\[i]\[j] 表示戳数组 nums\[i] \(包括) 到数组 nums\[j]的气球可以获得的最大值。
* 初始状态：matrix 的每一个值都为0。
* 状态转移方程：从第 left 个位置到第 rigth 个位置，我们以 left 到 right 中的任意一个位置 k 为例，假设最后一个戳 k 气球（其他所有气球已经戳爆了）则我们可以获得的硬币为 num\[left:k]  + nums\[left-1] \* nums\[k] \* nums\[right+1] + nums\[k:right] 
* num\[left:k]：戳破 k 位置左边所有气球的可以获得的硬币。
* nums\[left-1] \* nums\[k] \* nums\[right+1]：戳破当前位置可以获得的气球，由于 num\[left:right] 中只有 k 为位置没有被戳破，所以 k 位置左边的位置为 nums\[left-1]，如果越界则置为1，右边的有效值为 nums\[right+1] ，如果越界则置为1。
* nums\[k:right]：戳破 k 位右边所有气球的可以获得的硬币。
* 结果：matrix\[0]\[len(nums)-1]。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-18 14:52:28
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-18 15:44:09


class Solution:
    def maxCoins(self, nums: 'List[int]') -> 'int':
        # 如果数组为空，我们返回0
        if not nums: return 0
        # 声明一个二维矩阵，matrix[i][j]表示戳num[i]到num[j]的气球可以获得的最大值
        matrix = [[0] * len(nums) for _ in range(len(nums))]
        # left表示起点，right表示中点，count表示right-left的值
        # 辅助变量初始化为0
        left, right, count = 0, 0, 0
        for count in range(0, len(nums)):
            # 每一趟循环，left都从最左边开始
            left = 0
            # right表示所有可能的中点
            for right in range(count, len(nums)):
                # 临时变量用于记录最大值
                _max = 0
                # 从left到right中，我们以每一个位置为最后一个戳气球的位置
                for j in range(left, right + 1):
                    # 当前位置左边可以获得的最大值
                    _left = matrix[left][j - 1] if j - 1 >= left else 0
                    # 当前位置右边可以获得的最大值
                    _right = matrix[j + 1][right] if j + 1 <= right else 0
                    # 当前串的左边界的左边一个值
                    leftnum = nums[left - 1] if left - 1 >= 0 else 1
                    # 当前串的有边界的右边一个值
                    rightnum = nums[right + 1] if right + 1 < len(nums) else 1
                    # 以当前位置为嘴后一个戳气球的位置，可以获得的硬币个数
                    product = _left + nums[j] * leftnum * rightnum + _right
                    _max = max(_max, product)
                # 更新最大值
                matrix[left][right] = _max
                left += 1
        # matrix[0][len(nums) - 1]表示从0到len(nums)可以获得的最多的硬币个数
        return matrix[0][len(nums) - 1]
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-18-312-Burst-Balloons.py)。
©本文首发于 [何睿的博客](https://www.ruicore.cn/leetcode-312-burst-balloons/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
