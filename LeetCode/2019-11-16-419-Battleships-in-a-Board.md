# LeetCode 419. Battleships in a Board

## Description

Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:

```py
X..X
...X
...X
```

In the above board there are 2 battleships.
Invalid Example:

```py
...X
XXXX
...X
```
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

## 描述

给定一个二维的甲板， 请计算其中有多少艘战舰。 战舰用 'X'表示，空位用 '.'表示。 你需要遵守以下规则：

给你一个有效的甲板，仅由战舰或者空位组成。
战舰只能水平或者垂直放置。换句话说,战舰只能由 1xN (1 行, N 列)组成，或者 Nx1 (N 行, 1 列)组成，其中N可以是任意大小。
两艘战舰之间至少有一个水平或垂直的空位分隔 - 即没有相邻的战舰。
示例 :

```py
X..X
...X
...X
```
在上面的甲板中有2艘战舰。

无效样例 :
```py
...X
XXXX
...X
```
你不会收到这样的无效甲板 - 因为战舰之间至少会有一个空位将它们分开。

进阶:

你可以用一次扫描算法，只使用O(1)额外空间，并且不修改甲板的值来解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/battleships-in-a-board
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 横向连在一起的 "X" 构成一个战舰，竖向连在一起的 "X" 构成一个战舰。并且横向和竖向之间的战舰没有交叉。
* 对于每个战舰，统计它的第一个 "X" 。
* 如果一个 "X" 的左边或者上边有 "X"，那么它不是这个战舰的首个 "X"，忽略。只统计某一个位置是 "X"，并且其左边和上边不是 "X" 的位置数。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-11-16 21:22:05
# @Last Modified by:   何睿
# @Last Modified time: 2019-11-16 21:36:25

from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        count, row, col = 0, len(board), len(board[0])

        for i in range(row):
            for j in range(col):
                if board[i][j] == ".":
                    continue
                if i > 0 and board[i - 1][j] == "X":
                    continue
                if j > 0 and board[i][j - 1] == "X":
                    continue
                count += 1

                # 下面这种写法是正向思考，等价于上面的写法，思考是下面的思路，简化代码为上面的写法
                # if i > 0 and j > 0:
                #     if board[i][j] == "X" and board[i][j - 1] == "." and board[i - 1][j] == ".":
                #         count += 1
                # elif i == 0 and j == 0:
                #     if board[i][j] == "X":
                #         count += 1
                # elif i == 0:
                #     if board[i][j] == "X" and board[i][j - 1] == ".":
                #         count += 1
                # elif j == 0:
                #     if board[i][j] == "X" and board[i - 1][j] == ".":
                #         count += 1

        return count
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-11-16-419-Battleships-in-a-Board.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-419-battleships-in-a-board/) ，作者信息和本声明.
