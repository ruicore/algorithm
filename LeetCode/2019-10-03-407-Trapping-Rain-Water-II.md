# LeetCode 407. Trapping Rain Water II

## Description


Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Note:

Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.


The above image represents the elevation map \[\[1,4,3,1,3,2],\[3,2,1,3,2,4],\[2,3,3,2,3,1]] before the rain.


After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

### 思路

* 这道题虽然叫 Trapping Rain Water II，但是题目的解法和 Trapping Rain Water 并不一样。
* 这道题用到的基本数据结构是小顶堆。
* 基本思路是：我们想象海平面的海水慢慢侵入方格，依次找到会被海水填满的格子。
* 我们把最外面的四边当成四面墙，想象海水面不断的升高，首先会浸过墙面最低的格子，如果墙面最低格子的四周（出了在墙面的格子）有比它矮的格子，那么这就可以形成一个蓄水池，蓄水池的最高高度就是墙面最低的格子，于是我们计算这个蓄水池可以获得的蓄水量；然后这个蓄水池被添加到墙面中；继续在墙面中找最低的格子；
* [这个视频的动画解释的非常清楚](https://www.youtube.com/watch?v=cJayBq38VYw)。


```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-10-03 08:11:17
# @Last Modified by:   何睿
# @Last Modified time: 2019-10-03 11:57:48

import heapq

from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        queue, visited, max_heigth, water = [], set(), 0, 0
        row, col = len(heightMap), len(heightMap[0])
        count = row * col

        self.fill_border(queue, heightMap)
        visited = {(row, col) for _, row, col in queue}
        while queue:
            # 当所有的格子都在墙面上时，结束
            if len(visited) == count:
                return water
            height, i, j = heapq.heappop(queue)
            max_heigth = max(max_heigth, height)
            # 以最低的格子为起点，判断四周是否可以形成蓄水池，返回蓄水池蓄水的大小
            water += self.visit_neighbors(queue, visited, heightMap, max_heigth, row, col, i, j)
        return water

    def visit_neighbors(self, queue, visited, heightMap, max_heigth, row, col, i, j):

        water = 0
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nrow, ncol = i + x, j + y
            if (nrow, ncol) not in visited and self.is_in_border(row, col, nrow, ncol):
                num = heightMap[nrow][ncol]
                water += max(0, max_heigth - num)
                visited.add((nrow, ncol))
                heapq.heappush(queue, (num, nrow, ncol))

        return water

    def fill_border(self, queue, heightMap):
        row, col = len(heightMap), len(heightMap[0])
        for i in range(row):
            heapq.heappush(queue, (heightMap[i][0], i, 0))
            heapq.heappush(queue, (heightMap[i][-1], i, col - 1))
        for i in range(1, col - 1):
            heapq.heappush(queue, (heightMap[0][i], 0, i))
            heapq.heappush(queue, (heightMap[-1][i], row - 1, i))

    def is_in_border(self, row, col, i, j):
        return 0 <= i < row and 0 <= j < col
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-10-03-407-Trapping-Rain-Water-II.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-407-trapping-rain-water-ii/) ，作者信息和本声明.
