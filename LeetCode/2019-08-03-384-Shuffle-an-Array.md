# LeetCode 384. Shuffle an Array

## Description

Shuffle a set of numbers without duplicates.

Example:

```py
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
```

## 描述

打乱一个没有重复元素的数组。

示例:

```py
// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shuffle-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 使用 Python 的 random 库可以高效地实现需求。
* 由于 int 类型是不可变类型，所以在维护原数组的时候，使用浅拷贝就可以了。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-03 10:48:30
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-03 10:53:15

import copy
import random

from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.shuffle_ = nums
        self.original = copy.copy(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.shuffle_)
        return self.shuffle_
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-08-03-384-Shuffle-an-Array.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-384-shuffle-an-array/) ，作者信息和本声明.
