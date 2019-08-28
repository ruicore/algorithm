# LeetCode 396. Rotate Function

## Description

Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.

Example:

```py
A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
```

## 描述

给定一个长度为 n 的整数数组 A 。

假设 Bk 是数组 A 顺时针旋转 k 个位置后的数组，我们定义 A 的“旋转函数” F 为：

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]。

计算F(0), F(1), ..., F(n-1)中的最大值。

注意:
可以认为 n 的值小于 105。

示例:

```py
A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-function
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 移动原数组和移动索引效果相同（第一次原数组乘[0,1..n-1\]，第二次原数组乘[n-1,0,1...]）
* 观察发现：第 i+1 次的结果可以由第 i 次结果得到。如下图：
![LeetCode-396.-Rotate-Function-solve](https://ruicore.cn/wp-content/uploads/2019/08/LeetCode-396.-Rotate-Function-solve.jpeg)

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-28 21:06:46
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-28 21:41:13


from typing import List


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        sum_, count = sum(A), len(A)
        product = sum(map(lambda x: x[0] * x[1], enumerate(A)))
        res = product

        for i in A[:-1]:
            # 上一次的乘机减去所有数的和，加上当前位置的数乘以总数的个数
            product = product - sum_ + count * i 
            res = max(res, product)

        return res
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-08-28-396-Rotate-Function.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/?p=4974) ，作者信息和本声明.
