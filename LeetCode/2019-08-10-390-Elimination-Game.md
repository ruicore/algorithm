# LeetCode 390. Elimination Game

## Description

There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6

## 描述

给定一个从1 到 n 排序的整数列表。
首先，从左到右，从第一个数字开始，每隔一个数字进行删除，直到列表的末尾。
第二步，在剩下的数字中，从右到左，从倒数第一个数字开始，每隔一个数字进行删除，直到列表开头。
我们不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
返回长度为 n 的列表中，最后剩下的数字。

示例：

输入:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

输出:
6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/elimination-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 主要考察递归。
* 以题目中给的例子为例，9；当去掉 1，3，5，7后，剩下的 2，4，6，8，和 1，2，3，4 是差了两倍的关系。
* 也就是说为了求 2，4，6，8 的结果我们只需要在 1，2，3，4 的结果上乘以 2 即可。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-10 08:12:23
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-10 08:31:09


class Solution:
    def lastRemaining(self, n: int) -> int:
        return self.leftright(n)

    def leftright(self, n):
        if n <= 2:
            return n
        if n & 1 == 1:  # 奇数
            # 从左向右遍历，如果是奇数，如 1，2，3，4，5，那么剩下 2，4，也就是 2 *（1，2）
            return 2 * self.rightleft((n - 1) >> 1)
        else:
            # 从左向右遍历，如果是偶数，如 1，2，3，4那么剩下 2，4，也就是 2 *（1，2）
            return 2 * self.rightleft(n >> 1)

    def rightleft(self, n):
        if n <= 2:
            return 1
        if n & 1 == 1:
            # 从右向左遍历，如果是奇数，如 1，2，3，4，5，那么剩下 2，4，也就是 2 *（1，2）
            return 2 * self.leftright((n - 1) >> 1)
        else:
            # 从右向左遍历，如果是偶数，如 1，2，3，4，那么剩下 1，3，此时我们首先对所有数字加 1，也就是 2，4，
            # 那么此时就是 2 *（1，2，），由于增加了 1，我们再将其减去，所以最终是 2*（1，2）-1
            return 2 * self.leftright(n >> 1) - 1
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-08-10-390-Elimination-Game.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-390-elimination-game/) ，作者信息和本声明.
