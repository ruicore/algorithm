# LeetCode 200. Number of Islands

## Description
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

## 描述

给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3

### 思路

* 这道题可以采用深度优先搜索.
* 我们遇到一个"1"就把计数加一，让后使用深度优先搜索将者一片"1"全部置为"0",如此循环直至将所有的湖泊找到.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-20 18:21:07
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-20 18:32:37


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        res, row, col = 0, len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                # 每次找到一个"1"，就在结果技术中增加一个，然后将这一片连着的1置为"0"
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(
                grid[0]) or grid[row][col] == "0":
            return
        grid[row][col] = "0"
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-20-200-Number-of-Islands.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-200-number-of-islands/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
