# LeetCode 398. Random Pick Index

## Description

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

```py
int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
```

## 描述

给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

注意：
数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

示例:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
solution.pick(3);

// pick(1) 应该返回 0。因为只有nums[0]等于1。
solution.pick(1);

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/random-pick-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 这道题和第 382 题 [Linked List Random Node](https://leetcode.com/problems/linked-list-random-node) 解法类似。
* 遍历给定的数组，统计当前满足条件的数的个数 n，用 random 函数随机生成一个 1 到 n 的数，如果选到了 n ，就把当前的数和最终结果替换。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-30 19:55:46
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-30 20:17:06

import heapq
import random

from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.arrays = nums

    def pick(self, target: int) -> int:
        hep = []
        for i, v in enumerate(self.arrays):
            if v == target:
                # heap 维护最小堆，random.random() 会被用来比较
                # 没个数被弹出的概率都是一样的
                heapq.heappush(hep, (random.random(), i))
        _, index = heapq.heappop(hep)
        return index

    def pick2(self, target: int) -> int:

        n, res = 0, 0
        for x in filter(lambda x: x[1] == target, enumerate(self.arrays)):
            n += 1
            if random.randint(1, n) == n: # 解法思路同蓄水题解法思路
                res = x[0]

        return res
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-08-30-398-Random-Pick-Index.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-398-random-pick-index/) ，作者信息和本声明.
