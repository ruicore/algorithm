# LeetCode 413. Arithmetic Slices

## Description

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

```py
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
```

The following sequence is not arithmetic.

```py
1, 1, 2, 5, 7
```

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

Example:

```py
A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
```

## 描述

如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:

```py
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
```

以下数列不是等差数列。

```py
1, 1, 2, 5, 7
```

数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

如果满足以下条件，则称子数组(P, Q)为等差数组：

元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

函数要返回数组 A 中所有为等差数组的子数组个数。

示例:

```py
A = [1, 2, 3, 4]
```

返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arithmetic-slices
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 使用动态规划,dp[i] 表示以数组 i 号元素结尾构成的序列,这个序列的所有等差子序列的个数。
* 转移方程：如果数字 i 与前面的数字构成等差序列，dp[i] = dp[i-1]+1，否则为 0
* 结果：sum(dp) 
*  _count 函数遍历一个连续的等差序列，生成每个位置能构成的子等差序列的个数。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-10-13 18:47:35
# @Last Modified by:   何睿
# @Last Modified time: 2019-10-13 19:45:52

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:

        if len(A) < 3:
            return 0

        dp = [0 for _ in range(len(A))]
        d = A[1] - A[0]
        start = 2

        next_ = self._count(A, d, dp, start)
        while next_ < len(A):
            d = A[next_] - A[next_ - 1]
            start = next_ + 1
            next_ = self._count(A, d, dp, start)

        return sum(dp)

    def _count(self, A, d, dp, start):

        for i in range(start, len(A)):
            if A[i] - A[i - 1] == d:
                dp[i] = dp[i - 1] + 1
            else:
                return i

        return len(A)
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-10-13-413-Arithmetic-Slices.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-413-arithmetic-slices/) ，作者信息和本声明.
