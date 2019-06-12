# LeetCode 338. Counting Bits

## Description

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: \[0,1,1]
Example 2:

Input: 5
Output: \[0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

## 描述

给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: \[0,1,1]
示例 2:

输入: 5
输出: \[0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。

### 思路

* 二进制数 0 到 7 在前面添加一个 1 构成 8 到 15，二进制数 0 到 15 在前面添加一个 1 构成 16 到 31.
* 每 2 ^ i 到 2 ^ (i+1)-1 为一组，前面的数的 1 的个数加一构成当前组对应二进制数 1 的个数。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-07 11:54:35
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-07 12:22:34


class Solution:
    def countBits(self, num: int) -> [int]:
        # 结果数组
        result, count = [0], 1
        while count * 2 <= num:
            # 从 resut 数组中索引对应的二进制数前面加
            # 一个 1 构成范围从 count 到 count*2 -1 的数（包括两端）
            for i in range(count, count * 2):
                result.append(1 + result[i - count])
            count *= 2
        # 处理剩下的数
        for i in range(count, num + 1):
            result.append(1 + result[i - count])
        return result
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-04-07-338-Counting-Bits.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-338-counting-bits/) ，作者信息和本声明.
