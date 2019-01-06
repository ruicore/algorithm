# LeetCode 130. Surrounded Regions

## Description

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

```python
X X X X
X O O X
X X O X
X O X X
```

After running your function, the board should be:

```python
X X X X
X X X X
X X X X
X O X X
```

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

## 描述

给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

```python
X X X X
X O O X
X X O X
X O X X
```

运行你的函数后，矩阵变为：

```python
X X X X
X X X X
X X X X
X O X X
```

解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

### 思路

* 此题目使用了[深度优先搜索](https://zh.wikipedia.org/zh-hans/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2).
* 我们检查矩阵的第一行，最后一行，第一列，最后一列有没有"O",如果有，我们从此位置进行深度优先遍历，将从此位置开始所有连续的"O"都置为一个标记元素,如"1".
* 然后我们在进行遍历，将所有的"1"都置为"O"，其他元素都置为"X".

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-05 22:10:17
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-06 14:25:42

from pprint import pprint


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 如果矩阵为空，则直接返回
        if not board:
            return
        # 获取矩阵行数和列数
        row, col = len(board), len(board[0])
        # 遍历第一行和最后一行
        for i in range(0, row):
            # 如果当前的元素为"O",则进行深度优先遍历，将所有的"O"都置为"1"
            # （或者其他标记元素，只要不是"X"或"O"即可）
            # 检查第一行的所有元素
            if board[i][0] == "O":
                self.dfs(board, i, 0, row, col)
            # 检查最后一行的所有元素
            if board[i][col-1] == 'O':
                self.dfs(board, i, col-1, row, col)
        # 同上，遍历第一列和最后一列的所有元素
        for i in range(1, col-1):
            if board[0][i] == 'O':
                self.dfs(board, 0, i, row, col)
            if board[row-1][i] == 'O':
                self.dfs(board, row-1, i, row, col)
        # 遍历所有元素，将刚才标记的元素置为"O",其他元素都置为"X"
        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == "1":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

    def dfs(self, board, row, col, rows, cols):
        # 递归结束条件，如果已经越界则结束递归
        if row >= rows or col >= cols or row < 0 or col < 0:
            return
        # 如果当前元素是"O",则置为标记元素"1"
        if board[row][col] == "O":
            board[row][col] = '1'
            # 进行深度优先遍历，一共有上下左右四个出口
            self.dfs(board, row+1, col, rows, cols)
            self.dfs(board, row-1, col, rows, cols)
            self.dfs(board, row, col+1, rows, cols)
            self.dfs(board, row, col-1, rows, cols)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-05-130-Surrounded-Regions.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-130-surrounded-regions/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
