# LeetCode 279. Perfect Squares

## Description

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

## 描述

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

### 思路


#### 1.动态规划
* 状态：我们用dynamic数组表示每个数字需要由多少个平方数组成，即dynamic\[i]=j表示数字i需要j个完全平方数.
* 每一个数都由前面的某个数加上一个完全平方数构成，dynamic[i + sq] = dynamic\[i] + 1:sq表示一个完全平方数，所以数字i+sq可以由数字i加上完全平方数sq构成，数字i需要dynamic\[i]个完全平方数，所以dynamic[i + sq]需要dynamic\[i]加1个完全平方数.我们用循环将数字i到n都和n以内的完全平方数字组合，得到dynamic\[i]的解.

#### 2.[四平方和定理](https://zh.wikipedia.org/zh/%E5%9B%9B%E5%B9%B3%E6%96%B9%E5%92%8C%E5%AE%9A%E7%90%86)

* 四平方和定理的内容是：每个正整数均可表示为4个整数的平方和，所以对于任意一个整数，其用平方和表示最多需要4个数.
* 并且数字4a(a>=0)和a需要的平方数个数相同，并且num % 8 = 7，则num需要四个平方数构成.
* 我们另i=0，1，2...sqrt(n)，j=sqrt(n-i\*\*2),如果i\*\*2+j\*\*2==n: 1. 如果i，j不为0说明需要两个数，如果i，j为0需要一个数.
* 如果循环完毕没有找到合适的i，j说明需要3个数.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-06 09:19:35
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-06 17:33:50


class Solution:
    def numSquares(self, n: 'int') -> 'int':
        # 动态规划数组，dynamic[i]表示数字i可以最少可以有i个平方数相加
        dynamic = [x for x in range(n + 1)]
        # 生成候选完全平方数，n仅可能由这些数构成
        squares = [i * i for i in range(1, int(n**0.5) + 1)]
        # 完全平方数只需要1个数相加，即自己本身
        for item in squares:
            dynamic[item] = 1
        # 动态转移方程
        for i in range(1, n + 1):
            # 将每一个位置的值和完全平方数组合
            for sq in squares:
                if i + sq <= n:
                    # 产生dynamic[i + sq]的方式有多种，我么取最小的一种.
                    dynamic[i + sq] = min(dynamic[i] + 1, dynamic[i + sq])
        return dynamic[-1]

    def numSquares2(self, n: 'int') -> 'int':
        # 参考四平方和定理：https://zh.wikipedia.org/wiki/四平方和定理
        # 即每个正整数均可表示为4个整数的平方和
        # 数字4a和a需要的平方数相同
        while n % 4 == 0:
            n //= 4
        # 如果n对8取模结果为7，n一定由4个平方数组成
        if n % 8 == 7: return 4
        # 处理两个和1个平方和的情况
        i = 0
        sq = i**2
        while sq <= n:
            j = int((n - sq)**0.5)
            # n由两个平方数组成
            if sq + j * j == n:
                if i != 0 and j != 0: return 2
                else: return 1
            i += 1
            sq = i * i

        #如果执行到这里，说明n不由1，2，4个平凡数字组成，返回3
        return 3
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-06-279-Perfect-Squares.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-279-perfect-squares/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
