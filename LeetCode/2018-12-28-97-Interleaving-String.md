# LeetCode 97. Interleaving String

## Description

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

```python
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
```

Example 2:

```python
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
```

## 描述

给定s1，s2，s3，确定s3是否由s1和s2的交织形成，若是返回True，若不是则返回False.

### 思路

* 交织形成的意思是：不断的从s1和s2中交替的取出一些字符\(数量随机)构成一个新的字符，若当s1和s2都取完了且此时的新字符串与s3相等，说明s3可以由s1和s2交织形成，否则不可以交织形成.
* 此题目使用[动态规划](https://zh.wikipedia.org/wiki/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92).
* 动态规划适用于求解 **判断是否能够满足条件**\(返回布尔值)类型的题 和 **求解满足条件解的个数**\(返回个数，不要求返回每种解的具体情况)类型的题.
* 我们维护一个二维矩阵matrix\[m]\[n]，m = len(s1),n = len(s2).
* 每一个位置的值取决于:
* 以下说明索引从1开始:
1. 当前位置的上一个位置为True:说明 s2\[1:col] + \s1\[1:row-1] 可以构成s3\[1:row+col-1]的字符，于是我们取s1\[row],如果当前字符与s3\[row+col-1]相等，于是s2\[1:col]+\s1\[1:row-1] 可以构成s3\[1:row+col]的字符，当前位置设为True.
2. 当前位置的左一个位置为True:说明s1\[1:row] + s2\[1:col-1] 可以构成s3\[1:row+col-1]的字符，于是我们取s2\[col],如果当前字符与s3\[row+col-1]相等，于是s1\[1:row] + s2\[1:col] 可以构成s3\[1:row+col]的字符，当前位置设为True.
3. 如果上两个条件不能满足，说明当前位置是不可构成s3\[1:row+col]的字符的，于是当前位置设为False.
4. 最后返回matrix\[m]\[n]的值.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-28 09:26:14
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-28 10:23:43

from pprint import pprint

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # 动态规划，使用二维矩阵.
        # 获取矩阵的行数和列数.
        row, col = len(s1), len(s2)
        # 如果字符串1的长度加上字符串2的长度不等于字符串3的长度
        # 则字符串3一定不可以由字符串s1和字符串s2交替构成.
        if row + col != len(s3):
            return False
        # 生成二维矩阵
        matrix = [[False for _ in range(col+1)] for _ in range(row+1)]
        # 0 0 表示从s1中取0个字符，从s2中取0个字符用来构成S3中的空字符，可以构成，则设为True.
        matrix[0][0] = True
        # 初始化第一行，当s2的当前位置与s3相等并且s2当前位置的前一串能够构成s3的字符串，设为True.
        for i in range(1, col+1):
            matrix[0][i] = True if matrix[0][i - 1] and s2[i-1] == s3[i-1] else False
        # 初始化第一列，当s1的当前位置与s3相等并且s1当前位置的前一串能够构成s3的字符串，设为True.
        for i in range(1, row):
            matrix[i][0] = True if matrix[i -1][0] and s1[i-1] == s3[i-1] else False
        for i in range(1,row+1):
            for j in range(col+1):
                # 循环遍历检查每一个位置
                # 如果当前位置的上一个位置为True，我们就尝试从s1中取出一个字符i与s3中的i+j-1比较，如果相等当前位置设为True.
                # 如果当前位置的左一个位置为True，我们就尝试从s2中取出一个字符i与s3中的i+j-1比较，如果相等当前位置设为True.
                if (matrix[i-1][j] and s1[i-1] == s3[i+j-1]) or (matrix[i][j-1] and s2[j-1] == s3[i+j-1]):
                    matrix[i][j] = True
                # 如果上一个位置为False且左一个位置为False，或者当前位置s1[i-1]与s3[i+j-1]不等且s2[j-1]与s3[i+j-1]不等,
                # 当前位置设为False
                else:
                    matrix[i][j] = False
        return matrix[row][col]

if __name__ == "__main__":
    so = Solution()
    res = so.isInterleave(s1 = "a", s2 = "b", s3 = "a")
    print(res)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-28-97-Interleaving-String.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-97-interleaving-string/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
