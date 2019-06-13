# LeetCode 365. Water and Jug Problem

## Description

You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.

Example 1: (From the famous "Die Hard" example)

```py
Input: x = 3, y = 5, z = 4
Output: True
```

Example 2:

```py
Input: x = 2, y = 6, z = 5
Output: False
```
## 描述

有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
示例 1: (From the famous "Die Hard" example)

```py
输入: x = 3, y = 5, z = 4
输出: True
```

示例 2:

```py
输入: x = 2, y = 6, z = 5
输出: False
```

### 思路

* 因为每次都只能填满桶或清空桶，那么如果可以通过 x ，y 得到 z，就可以记 z = a * x + b * y，此时 a，b 为整数。
* 根据[裴蜀定理](https://zh.wikipedia.org/wiki/%E8%B2%9D%E7%A5%96%E7%AD%89%E5%BC%8F)，z = a * x + b * y 有整数解时当且仅当 z 是 x 及 y 的最大公约数的倍数。
* 那么我们只需要判断 z 是否是 x，y 的公因式即可。
* 举例说明等式的含义，当 x = 3，y = 5，z = 4，时，有 4 = 5\*2-3\*2。正号表示填满桶，负号表示清空桶。
1. 将容量为 5 的桶填满，全部倒入容量为 3 桶中（由于 3 小于 5，所以将 3 填满，倒出，将剩下的倒入），此时容量为 3 的桶剩余 2.
2. 将容量为 5 的桶填满，将水倒入容量为 3 的桶，由于此时 3 桶中有水量为 2 的水，所以容量为 5 的桶倒出一份即可将 3 填满，此时 5 中剩余 4.
* 再举一例，x = 13,y = 11, z = 1, 有 1 ==6 * 11 - 5 *13；
1. 将 y 的 11 填满，全部倒入 x 的 13 中（此时 x 剩余 11）；
2. 将 y 的 11 填满，全部倒入 x 的 13 中（x 中原本剩余 11；将 y 的 11份水 中的 2 份倒入 x，将 x 全部倒出，再将 y 中的 9 份倒入 13； 此时 x 剩余 9）；
3. 将 y 的 11 填满，全部倒入 x 的 13 中（此时 x 剩余 7）；
4. 将 y 的 11 填满，全部倒入 x 的 13 中（此时 x 剩余 5）；
5. 将 y 的 11 填满，全部倒入 x 的 13 中（此时 x 剩余 3）；
6. 将 y 的 11 填满，全部倒入 x 的 13 中（此时 x 剩余 1）；

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-13 11:03:29
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-13 12:20:44


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0 or (z <= x + y and z % self.__gcd(x, y) == 0):
            return True
        return False

    def __gcd(self, x: int, y: int) -> int:
        return x if y == 0 else self.__gcd(y, x % y)
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-06-13-365-Water-and-Jug-Problem.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-365-water-and-jug-problem/) ，作者信息和本声明.
