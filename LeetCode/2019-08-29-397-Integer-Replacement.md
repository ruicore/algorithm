# LeetCode 397. Integer Replacement

## Description

Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

```py
Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
```

Example 2:

```py
Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
```

## 描述

给定一个正整数 n，你可以做如下操作：

1. 如果 n 是偶数，则用 n / 2替换 n。
2. 如果 n 是奇数，则可以用 n + 1或n - 1替换 n。
n 变为 1 所需的最小替换次数是多少？

示例 1:

```py
输入:
8

输出:
3

解释:
8 -> 4 -> 2 -> 1
```

示例 2:

```py
输入:
7

输出:
4

解释:
7 -> 8 -> 4 -> 2 -> 1
或
7 -> 6 -> 3 -> 2 -> 1
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-replacement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 除以 2 等小于将愿数字二进制向右移动。
* 假设有这样一个数 0b1111，我们可以选择加 1 或减 1；
* 0b1111 +1 --> 0b10000 --> 右移 4 次；共 5 次
* 0b1111 -1 --> 0b1110 --> 0b111 -1 --> 0b110 --> 0b11 -1 --> 0b10 --> 0b1; 共 6 次

* 假设有 0b1101
* 0b1101 -1 --> 0b1100 --> 0b110 --> 0b11 -1 --> 0b10 --> 0b1
* 0b1101 +1 --> 0b1110 --> 0b111 +1 --> 0b1000 --> 0b100 --> 0b10 --> 0b1
* 加一是为了使得此数的二进制表示中 1 的个数减少（但是会产生 1 左移）；减一说明此时「加一减少 1 的个数带来的效果被 1 左移抵消了」。
* 规律：当此数是 2 的倍数是除以2；当此数二进制后两位为 0b11 时，加一；当此数二进制后两位为 0b01 时减一；唯一例外的是当次数刚好是 0b11 时，此时应当减 1

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-29 21:06:55
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-29 21:41:26


class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            count += 1
            if not n % 2:
                n >>= 1
            elif n & 0b11 == 0b11 and n != 0b11:
                n += 1
            else:
                n -= 1

        return count
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-08-29-397-Integer-Replacement.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-397-integer-replacement/) ，作者信息和本声明.
