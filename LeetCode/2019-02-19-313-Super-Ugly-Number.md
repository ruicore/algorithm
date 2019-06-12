# LeetCode 313. Super Ugly Number

## Description

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

```py
Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
```

Note:

* 1 is a super ugly number for any given primes.
* The given numbers in primes are in ascending order.
* 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
* The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

## 描述

编写一段程序来查找第 n 个超级丑数。

超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

示例:

```py
输入: n = 12, primes = [2,7,13,19]
输出: 32 
解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
```

说明:

* 1 是任何给定 primes 的超级丑数。
* 给定 primes 中的数字以升序排列。
* 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000 。
* 第 n 个超级丑数确保在 32 位有符整数范围内。

### 思路

* 这道题和第 264 题 [Ugly Number II](https://leetcode.com/problems/ugly-number-ii) 做法类似。
* 我们使用动态规划。
* 状态：我们用 index 用于记录 primes 中每个质数上一次产生丑数的有效位置，并用一个数组 uglynum 记录产生的丑数。比如 index\[2] = 7， 表示质数 primes\[2] 上一次产生的质数在 uglynum 中的索引为 7 ，即产生的丑数为 uglynum\[7]。 
* 初始值：index 所有值初始化 0，ugly 第一个值初始化为1。
* 状态转移方程：获取下一个丑数：我们用 index 中记录的上一次质数产生的丑数在 uglynum 中的位置获得对应的丑数 uglynum\[index\[i]]，并用对应的质数 primes\[i] 与 uglynum\[index\[i]] 相乘作为下一次可能的丑数，所有的丑数用一个临时数组 _next 存储。我们取所有数中的最小值作为下个丑数。更新 index 数组：如果 uglynext == _next\[i]，我们让 index\[i] 自增一次。
* 结果：丑数数组的最后一个值。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-19 15:35:20
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-19 16:11:26


class Solution:
    def nthSuperUglyNumber(self, n: 'int', primes: 'List[int]') -> 'int':
        """
        :type n: int
        :rtype: int
        """
        # 处理特殊情况，如果n为1或者primes为空，返回1
        if n < 2 or not primes: return 1
        # 声明一个数组，用于存储获取的丑数
        uglynum = [1]
        # 辅助变量，primes的个数，当前生成的丑数的个数
        num, count = len(primes), 1
        # index数组用于存储primes中每个数上一次产生有效数的下一个位置
        index = [0 for _ in range(num)]
        while count < n:
            # 动态规划，用primes中的每个数从上一次产生有效位置的地方产生下一个数
            _next = [primes[i] * uglynum[index[i]] for i in range(num)]
            # 下一个丑数是产生的丑数中最小的数
            uglynext = min(_next)
            # 更新索引值
            for i in range(num):
                if uglynext == _next[i]: index[i] += 1
            uglynum.append(uglynext)
            count += 1
        # 返回最后一个丑数
        return uglynum[-1]
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-19-313-Super-Ugly-Number.py)。
©本文首发于 [何睿的博客](https://www.ruicore.cn/leetcode-313-super-ugly-number/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
