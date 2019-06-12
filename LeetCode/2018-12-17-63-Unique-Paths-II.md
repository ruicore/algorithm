# LeetCode 63. Unique Paths II

## Description

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

![robot_maze](https://wp.me/aaizn9-SK)
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:

1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

## 描述

机器人位于m x n网格的左上角（在下图中标记为“开始”）。

机器人只能在任何时间点向下或向右移动。 机器人正试图到达网格的右下角（在下图中标记为“完成”）。

现在考虑是否在网格中添加了一些障碍。 有多少条独特的路径？

### 思路

* 此题目同第[62题](https://leetcode.com/problems/unique-paths)思路基本一致，只是多了障碍,62题解析在[这里](https://www.ruicore.cn/leetcode-62-unique-paths/).
* 基本思路是：当前位置路径条数 = 当前位置左边路径条数 + 当前位置上边路径条数.
* 实现思路可以用递归，也可以用循环.
* 递归：递归需要注意的是需要保存已经遍历过节点位置的路径条数，以此来减少递归次数，否则LeetCode会报超时.

```python
class Solution:
    # 递归版本实现，当前位置的路径条数 = 当前位置左边的路径条数 + 当前位置上边的路径条数
    def __init__(self):
        # 结果矩阵，用于存储已经遍历过的位置，减少递归重复
        self.res = []

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 如果矩阵为空，则直接返回0
        if not obstacleGrid:
            return 0
        # 获取矩阵的行数最大索引，获取矩阵列数最大索引
        row, col = len(obstacleGrid)-1, len(obstacleGrid[0])-1
        # 初始化结果矩阵，每一个位置都初始化为-1，表示当前位置还没有遍历到
        self.res = [[-1 for _ in range(col+1)] for _ in range(row+1)]
        # 进行递归调用
        return self.recur(row, col, obstacleGrid)

    def recur(self, row, col, o):
        # 存储递归结果的递归，要注意递归的结束条件
        # 条件一：如果到达左上角，则返回
        if row == 0 and col == 0:
            # 如果左上角没有障碍返回1，表示有一条路，否则返回0，表示不可到达，即没有路
            return 1 if o[0][0] == 0 else 0
        # 条件二：如果已经到达矩阵之外，返回0，表示没有路，不可到达
        elif row < 0 or col < 0:
            return 0
        # 条件三：如果当前位置已经遍历过，则直接返回当前位置的路径
        elif self.res[row][col] != -1:
            return self.res[row][col]
        # 条件四：如果当前位置不可到达，直接返回0，并标记当前位置已经遍历过
        elif o[row][col] == 1:
            self.res[row][col] = 0
            return 0
        else:
            # 求得当前位置左边的路径条数
            left = self.recur(row, col-1, o)
            # 求得当前路径上边的路径条数
            top = self.recur(row-1, col, o)
            # 记录当前位置的路径条数
            self.res[row][col] = left+top
        # 返回当前位置的路径条数
        return self.res[row][col]


class Solution2:
    # 循环版本实现，当前位置的路径条数 = 当前位置左边的路径条数 + 当前位置上边的路径条数
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 如果矩阵为空，直接返回0
        if not obstacleGrid:
            return 0
        # 获得矩阵行数最大索引，获得矩阵列数最大索引
        row, col = len(obstacleGrid)-1, len(obstacleGrid[0])-1
        # 结果矩阵，用于存储到达每一个位置的路径条数，每一个位置都初始化为0
        res = [[0 for _ in range(col+1)] for _ in range(row+1)]
        # 初始化左上角
        res[0][0] = 1 if not obstacleGrid[0][0] else 0
        # 初始化第一行，当前位置如果没有障碍且上一个位置能够到达：初始化为1，否则初始化为0
        for i in range(1, col+1):
            res[0][i] = 1 if not obstacleGrid[0][i] and res[0][i-1] else 0
        # 初始化第一列，当前位置如果没有障碍且上一个位置能够到达：初始化为1，否则初始化为0
        for i in range(1, row+1):
            res[i][0] = 1 if not obstacleGrid[i][0] and res[i-1][0] else 0
        # 遍历每一个位置
        for i in range(1, row+1):
            for j in range(1, col+1):
                # 当前位置没有障碍：当前位置路径条数= 当前位置左边路径条数+当前位置上一个路径条数
                # 当前位置有障碍：条数为0
                res[i][j] = res[i-1][j] + \
                    res[i][j-1] if not obstacleGrid[i][j] else 0
        return res[row][col]


if __name__ == "__main__":
    so = Solution2()
    res = so.uniquePathsWithObstacles([[0, 1, 0], [1, 0, 0], [0, 0, 0], [0, 0, 0]])
    print(res)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-17-63-Unique-Paths-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-63-unique-paths-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.