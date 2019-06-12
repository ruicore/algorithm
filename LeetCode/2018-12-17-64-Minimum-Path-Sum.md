# LeetCode 64. Minimum Path Sum

## Description

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

## 描述

给定m x n网格填充非负数，找到从左上到右下的路径，这最小化了沿其路径的所有数字的总和。

注意：您只能在任何时间点向下或向右移动。

### 思路

* 这道题是给定一个m * n的矩阵，让从左上角走到右下角，每一个位置都有一个权重，让返回一条路径上所有权重和，要求是此和最小.
* 这道题同第[62题](https://leetcode.com/problems/unique-paths)，第[63题](https://leetcode.com/problems/unique-paths-ii)思路非常类似，第62题解析在[这里](https://www.ruicore.cn/leetcode-62-unique-paths/)，第63题在[这里](https://www.ruicore.cn/leetcode-63-unique-paths-ii/).
* 我们假设有矩阵Matrix\[m]\[n],矩阵Matrix\[i]\[j]位置只能由Matrix\[i-1]\[j]和Matrix\[i]\[j-1]到达.
* 因此，到达Matrix\[i]\[j]的最短路径 = Min {Matrix\[i-1]\[j],Matrix\[i]\[j-1]} + Matrix\[i]\[j]
* 即到达矩阵当前位置的最小权重路径 = {到达矩阵当前位置左边的最小权重路径，到达矩阵当前位置上边的最小权重路径}中的最小值 + 矩阵当前位置的权重

```python
class Solution:
    # 递归版本，当前位置最小值 = min{当前位置左边最小值，当前位置上边最小值}+当前位置的值
    def __init__(self):
        # 声明结果矩阵，用于记录已经遍历过的位置
        self.res = []

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 入股gird为空，则直接返回
        if not grid:
            return 0
        # 获取最大行的索引，获取最大列的索引
        row, col = len(grid)-1, len(grid[0])-1
        # 初始化第一行，每一个位置的最短路径 = 左边的最短路径+本身的值
        for i in range(1, col+1):
            grid[0][i] += grid[0][i-1]
        # 初始化第一列，每一个位置的最短路径 = 上边的最短路径+本身的值
        for i in range(1, row+1):
            grid[i][0] += grid[i-1][0]
        # 初始化结果矩阵，-1表示当前位置还没有遍历过
        self.res = [[-1 for _ in range(col+1)] for _ in range(row+1)]
        return self.recur(row, col, grid)

    def recur(self, row, col, grid):
        # 如果到达矩阵左上角的位置，返回此位置的路径值
        if row == 0 and col == 0:
            return grid[0][0]
        # 如果到达第一行但不是最坐上角
        elif row == 0:
            return grid[0][col]
        # 如果到达第一列但不是最左上角
        elif col == 0:
            return grid[row][0]
        # 如果当前位置已经遍历过
        elif self.res[row][col] != -1:
            return self.res[row][col]
        # 求矩阵当前位置做左边的最小值
        left = self.recur(row, col-1, grid)
        # 求矩阵当前位置上边的最小值
        top = self.recur(row-1, col, grid)
        # 记录矩阵当前位置的值
        self.res[row][col] = min(left, top)+grid[row][col]
        # 返回矩阵当前位置的值
        return self.res[row][col]


class Solution2:
    # 循环版本实现，当前位置最小值 = min{当前位置左边最小值，当前位置上边最小值}+当前位置的值
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 如果gird矩阵为空，则直接返回
        if not grid:
            return 0
        # 获得行的最大索引，获得列的最大索引
        row, col = len(grid)-1, len(grid[0])-1
        # 初始化第一行，当前位置最短路径 = 当前位置左边最短路径 + 当前位置的值
        for i in range(1, col+1):
            grid[0][i] += grid[0][i-1]
        # 初始化第一列，当前位置最短路径 = 当前位置上边最短路径 + 当前位置的值
        for i in range(1, row+1):
            grid[i][0] += grid[i-1][0]
        # 遍历每一个位置，当前位置最短路径 = min {当前位置左边最短路径，当前位置上边最短路径} + 当前位置的值
        for i in range(1, row+1):
            for j in range(1, col+1):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1])+grid[i][j]
        return grid[row][col]
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-17-64-Minimum-Path-Sum.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-64-minimum-path-sum/)，欢迎转载，转载需保留文章来源，作者信息和本声明.