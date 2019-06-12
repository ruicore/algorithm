# LeetCode 62. Unique Paths

## Description

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

![robot_maze](https://wp.me/aaizn9-SK)

Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:

1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28

## 描述

机器人位于m x n网格的左上角（在上图中标记为“开始”）。

机器人只能在任何时间点向下或向右移动。 机器人正试图到达网格的右下角（在下图中标记为“完成”）。

有多少可能的独特路径？

### 思路

* 这个题目即是要求从m x n 的棋盘的左上角走到右下角，问一共有多少种走法
* 基本思路是动态规划，递归.
* 我们观察得到右下角的格子只有两种走法,即从上往下走，或者从左往右走；而左边的格子也只有两种走法，从上到下，或者从左到右.
* 即A\[m]\[n] = A\[m]\[n-1]+A\[m-1]\[n].
* 注意：在使用递归的过程种会出现同一个位置多次遍历的情况，为此我们使用一个二维数组保存已经遍历的位置，加快递归.

```python
class Solution:
    def __init__(self):
        self.res = []

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        self.res = [[0 for _ in range(n)] for _ in range(m)]
        return self.recursion(m, n)

    def recursion(self, m, n):
        # 递归结束条件，当到达最左边的时候或者到达最上层的时候，结束递归
        if m == 1 or n == 1:
            return 1
        # 递归检查，检查当前位置是否已经遍历过，如果是则直接返回
        if self.res[m-1][n-1] > 0:
            return self.res[m-1][n-1]
        # 获得走到此位置左边的走法
        left = self.recursion(m, n-1)
        # 获得此位置右边的走法
        top = self.recursion(m-1, n)
        # 记录当前位置的走法
        self.res[m-1][n-1] = left+top
        # 返回
        return self.res[m-1][n-1]
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-17-62-Unique-Paths.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-62-unique-paths/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
