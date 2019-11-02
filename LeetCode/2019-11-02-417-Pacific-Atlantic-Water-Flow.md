# LeetCode 417. Pacific Atlantic Water Flow

## Description

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.

Example:

```py
Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
```

## 描述

给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。

规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。

请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。

提示：

输出坐标的顺序不重要
m 和 n 都小于150

示例：

```py
给定下面的 5x5 矩阵:

  太平洋 ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋
返回:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pacific-atlantic-water-flow
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 使用深度优先搜索（使用广度优先搜索也可以）。
* 声明两个变量，```pacific``` 和 ```atlantic```,```pacific``` 表示从第一列，第一行的点出发遍历点，遍历后所有点的状态，```True``` 为可以到达，```False```为不可到达；```atlantic``` 表示从最后一行，最后一列出发，能够到达的所有的点；取这两部分的交集，即是答案所求。
* 从每一个点出发的时候，使用深度优先搜索。如果当前位置没有越界，还没有被遍历，并且上一个点的高度小于等于当前节点的高度，说明当前节点可以到达。然后当前节点向上、下、左、右四个方向前进。

```py 
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-11-02 10:57:28
# @Last Modified by:   何睿
# @Last Modified time: 2019-11-02 12:02:14

from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return
        row, col = len(matrix), len(matrix[0])
        pacific = [[False] * col for _ in range(row)]
        atlantic = [[False] * col for _ in range(row)]

        for i in range(row):
            self.dfs(matrix, i, 0, -1, row, col, pacific)
            self.dfs(matrix, i, col - 1, -1, row, col, atlantic)

        for i in range(col):
            self.dfs(matrix, 0, i, -1, row, col, pacific)
            self.dfs(matrix, row - 1, i, -1, row, col, atlantic)

        return filter(lambda x: pacific[x[0]][x[1]] and atlantic[x[0]][x[1]], ((i, j) for i in range(row) for j in range(col)))

    def dfs(self, matrix, i, j, height, row, col, reached):
        if not 0 <= i < row or not 0 <= j < col or reached[i][j] or matrix[i][j] < height:
            return
        reached[i][j] = True
        for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            self.dfs(matrix, i + x, j + y, matrix[i][j], row, col, reached)
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-11-02-417-Pacific-Atlantic-Water-Flow.py)。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留[文章来源](https://ruicore.cn/417-pacific-atlantic-water-flow/) ，作者信息和本声明.
