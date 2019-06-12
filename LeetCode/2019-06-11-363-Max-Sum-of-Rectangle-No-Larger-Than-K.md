# LeetCode 363. Max Sum of Rectangle No Larger Than K

## Description

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

Input: matrix = \[\[1,0,1],\[0,-2,3]], k = 2
Output: 2 
Explanation: Because the sum of rectangle \[\[0, 1], \[-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
Note:

The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?

## 描述

给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。

示例:

输入: matrix = \[\[1,0,1],\[0,-2,3]], k = 2
输出: 2 
解释: 矩形区域 \[\[0, 1], \[-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。

### 思路

* 将二维的矩阵转换成为一维的数组，求数组的子数组中和小于等于 k 的最大数组。
* 假设给定的矩阵一共有 4 列，编号为 1，2，3，4；那么可以构成的数组有：1，1+2，1+2+3，1+2+3+4，2，2+3，2+3+4，3，3+4，4。
* 对这些列求和，构成一个新的一维数组。
* [kadane](https://en.wikipedia.org/wiki/Maximum_subarray_problem) 算法可以用来寻找数组的子数组中，和最大的那一数组。在这里**无法**用于求解小于 k 的最大数组和。
* 求解数组中小于等于 k 的最大和：用 sum（0，i）表述数组 array 从 0 到 i的和，如果存在一个sum（0，j），j<\i,使得 sum（0，i）-sum（0，j）<=k；那么区间(j,i]就是一个有效的子区间；同时为了使得sum（0，i）-sum（0，j）这个值尽可能大，应当使得sum（0，j）尽可能小。
* 基本思路是，我们从左往右遍历数组 array，并求得数组从起始位置 0 到当前位置的 i 和 sum（0，i），并找到从 0 到 i的位置中，和大于等于 sum（0，i）- k的最小值；这样我们就确定了这样一个区间：此区间以 i 做为结尾，并且和小于等于 k ，且为最大。
* 如何确定一个数组中大于等于 t 的最小值？我们使用 bisect 库，对于数组 a（我们在构建的时候应当使得 a 有序）；用 bisect.bisect_left 找到将 t 插入到数组 a 中应当插入的位置 index，a\[index] 就是大于等于 t 的最小值。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-11 20:41:49
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-12 08:14:42

import sys
import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:

        if not matrix: return 0
        area, row, col = -sys.maxsize, len(matrix), len(matrix[0])

        # 将矩阵转换成为一维的数组
        for left in range(col):
            tmp = [0 for _ in range(row)]
            for right in range(left, col):
                # 将后面的列加入到前面已经形成的列中
                for i in range(row):
                    tmp[i] += matrix[i][right]
                # 找到此数组中和小于等于 k 的最大数组和
                res = self.__get_kadane(tmp, k)
                # 如果存在，对结果进行更新
                if res != None: area = max(res, area)

        return area

    def __get_kadane(self, array: List[int], k: int) -> int:

        if not array: return 0

        sum_list, tmp, res = [0], 0, -sys.maxsize

        for item in array:
            tmp += item
            max_min = tmp - k
            if max_min == 0:
                return k
            else:
                # 找到插入的位置
                index = bisect.bisect_left(sum_list, max_min)
                # 插入的位置在数组的最后一个，说明不存在一个值比 max_min 大
                # 否则大于等于 max_min 的最小值就是 sum_list[index]
                if index != len(sum_list):
                    res = max(res, tmp - sum_list[index])
            # 最后将当前的和插入到 sum_list 数组中
            bisect.insort_left(sum_list, tmp)

        return res if res <= k else None
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-06-11-363-Max-Sum-of-Rectangle-No-Larger-Than-K.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-363-max-sum-of-rectangle-no-larger-than-k/) ，作者信息和本声明.
