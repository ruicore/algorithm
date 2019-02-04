# LeetCode 264. Ugly Number II

## Description

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.

## 描述

编写一个程序，找出第 n 个丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

### 思路

* 整型范围内(2^32)内一共有1690个丑数.
* 根据丑数的定义，num = 2\^i \* 3\^j \* 5\^k.假设当前的丑数是n，下一个丑数num1一定是n\*2，下二个丑数num2一定是n\*3，n\*5,num1\*2 三个数中较小的一个.
* 丑数乘以2，或3，或5都是丑数，并且当前的丑数一定会被乘以2，乘以3，乘以5来产生新的丑数，只不过相乘所得到的结果并不是连续出现。比如当前丑数是n，下一个丑数num1是n\*2,再下一个丑数是num1*2，接下来才是n\*3。于是我们用i，j，k分别表示当前丑数乘以2，3，5，并取所乘最小的丑数作为下一个丑数，然后刚才被选中的丑数向后移动一个.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-04 13:35:56
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-04 14:25:45


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglynum = [1]
        # i:2的次数，j:3的次数，k：5的次数，count：丑数的个数
        # i表示当前位置的丑数乘以2
        # j表示当前位置的丑数乘以3
        # k表示当前位置的丑数乘以5

        i, j, k, count = 0, 0, 0, 1
        while count < n:
            # 我们以对应的上一个数为基底，分别对应乘上2，3，5，
            # 新的丑数一定是i，j，k位置的丑数对应乘以2，3，5中的最小数
            uglyi, uglyj, uglyk = uglynum[i] * 2, uglynum[j] * 3, uglynum[k] * 5
            # 然后我们选择最小的数
            uglynext = min(uglyi, uglyj, uglyk)
            # 如果uglynext == uglyi，说明当前位置的丑数乘以2得到新的丑数
            # i自增一次表示用下一个数乘以2产生新的丑数
            if uglynext == uglyi: i += 1
            # 如果uglynext == uglyj，说明当前位置的丑数乘以3得到新的丑数
            # j自增一次表示用下一个数乘以3产生新的丑数
            if uglynext == uglyj: j += 1
            # 如果uglynext == uglyk，说明当前位置的丑数乘以5得到新的丑数
            # k自增一次表示用下一个数乘以5产生新的丑数
            if uglynext == uglyk: k += 1
            uglynum.append(uglynext)
            count += 1
        # 返回最后一个数字
        return uglynum[-1]
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-04-264-Ugly-Number-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-264-ugly-number-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
