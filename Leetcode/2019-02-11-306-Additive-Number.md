# LeetCode 306. Additive Number

## Description

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

```py
Input: "112358"
Output: true 
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
```
Example 2:

```py
Input: "199100199"
Output: true 
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
```

## 描述

累加数是一个字符串，组成它的数字可以形成累加序列。

一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。

说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

示例 1:

```py
输入: "112358"
输出: true 
解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
```
示例 2:

```py
输入: "199100199"
输出: true 
解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
```
### 思路

* 这道题可以使用深度优先搜索进行回溯.
* 我们使用深度优先搜索，找到所有可能拆分给定字符串的方式，然后我们判断当前的拆分方式是否能构成累加数，如果可以，我们用res记录为True，否则为False.
* __valid函数用于判断当前的组合方式是否能构成累加数，注意：累加数至少需要三个.

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-11 20:50:12
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-11 21:25:41


class Solution:
    def isAdditiveNumber(self, num: 'str') -> 'bool':
        # 根据题意，累计加数至少有三个
        if len(num) < 3: return False
        self.res = False
        # 深度优先搜索，遍历所有可能的解
        self.__dfs(0, num, [])
        return self.res

    def __dfs(self, start, num, coms):
        # 递归结束条件，当num中没有数字时，检查当前组合是否满足条件
        if start == len(num):
            # 如果当前组合合法，我们将self.res置为True
            if self.__valid(coms): self.res = True
            return
        # 记录起始位置
        index = start
        while index < len(num):
            # 如果当前数字的起始数字是"0'退出循环（注意单独一个'0'本身是合法的）
            if num[start] == "0" and index != start: break
            # 如果当前的组合已经有了至少3个数，我们检查前面的所有数是否是累加数
            # 如果不是我们退出循环，表示当前的分支不用再查找，减少时间
            if len(coms) > 2 and not self.__valid(coms): break
            # 递归遍历分支
            self.__dfs(index + 1, num, coms + [num[start:index + 1]])
            index += 1

    def __valid(self, coms):
        # 如果一共都没有三个数，返回False
        if len(coms) < 3: return False
        for i in range(len(coms) - 2):
            # 只要有一个不满足累加数的条件，返回False
            if int(coms[i]) + int(coms[i + 1]) != int(coms[i + 2]):
                return False
        return True
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-11-306-Additive-Number.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-306-additive-number/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
