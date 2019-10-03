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


The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.


After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

### 思路

* 这道题虽然叫 Trapping Rain Water II，但是题目的解法和 Trapping Rain Water 并不一样。
* 这道题用到的基本数据结构是小顶堆。
* 基本思路是：我们想象海平面的海水慢慢侵入方格，依次找到会被海水填满的格子。
* 我们把最外面的四边当成四面墙，想象海水面不断的升高，首先会浸过墙面最低的格子，如果墙面最低格子的四周（出了在墙面的格子）有比它矮的格子，那么这就可以形成一个蓄水池，蓄水池的最高高度就是墙面最低的格子，于是我们计算这个蓄水池可以获得的蓄水量；然后这个蓄水池构成
* [这个视频的动画解释的非常清楚](https://www.youtube.com/watch?v=cJayBq38VYw)。
源代码文件在 这里 。
©本文是原创文章，欢迎转载，转载需保留 文章来源 ，作者信息和本声明.
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 文章来源 ，作者信息和本声明.
