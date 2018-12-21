# LeetCode 73. Set Matrix Zeroes

## Description

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

## 描述

给定一个m * n 的矩阵，如果当前元是0，则把此元素所在的行，列全部置为0.
额外要求：是否可以做到空间复杂度O(1)?

### 思路一

* 我们首先对所有的正数加1，这样原来的矩阵中就没有1了，于是1可以用来作为标记.
* 我们先按行遍历，遇到第一个0，就把0前面的所有元素置为0，把0后面的元素：若是0，置为标记符1，如不是0，置为0.
* 我们按列检查，只要当前列有1，则把此列的所有元素值为0.
* 最后我们把所有的正数自减一次.
* 此方法没有使用额外的空间.

```python
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 获取行数或者列数
        row, col = len(matrix), len(matrix[0])
        # 把所有的整数自增一次，这样我们就创造了一个特殊值1
        for i in range(row):
            for j in range(col):
                if matrix[i][j] > 0:
                    matrix[i][j] += 1
        # 按行遍历，遇到每一行的第一个0，则把0前面的元素全部置为0
        # 把0后面的元素：若是0，置为1，如不是0，置为0
        # 把本身（即第一个0）置为0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                    for t in range(0, j):
                        matrix[i][t] = 0
                    for t in range(j+1, col):
                        if matrix[i][t] == 0:
                            matrix[i][t] = 1
                        else:
                            matrix[i][t] = 0
                    break
        # 检查列，只要此列有1，则把此列置为0
        for i in range(col):
            for j in range(row):
                if matrix[j][i] == 1:
                    for t in range(0, row):
                        matrix[t][i] = 0
                    break
        # 把所有的正数自减一次
        for i in range(row):
            for j in range(col):
                if matrix[i][j] > 0:
                    matrix[i][j] -= 1
```

### 思路二

* 我们用原矩阵的第一列来存储当前元素所对应的行是否需要置为0.
* 我们用原矩阵的第一行来存储当前元素所对应的列是否需要置为0.
* 我们用firstrow=False，firstcol=False来存储第一行，第一列是否需要置为0.
* 我们遍历第一行，遇到了0就把firstrow置为Ture.
* 我们遍历第一列，遇到了0就把firstcol置为Ture.
* 我们从matrix\[1]\[1]开始遍历行列，如果matrix\[i]\[j]==0，则置matrix\[i]\[0]=0,matrix\[0]\[j]=0.
* 我们从matrix\[0]\[1]检查第一行，如果matrix\[0]\[col]==0,则置第col（索引）列元素为0.
* 我们从matrix\[1]\[0]检查第一行，如果matrix\[row]\[0]==0,则置第coi（索引）列元素为0.
* 如果firstrow==Ture,我们置第一行元素为0.
* 如果firstcol==Ture,我们置第一列元素为0.
* 此方法使用了额外的两个空间.

```python
class Solution2:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 用于标记第一行，第一列是否需要改变
        firstrow, firstcol = False, False
        # 获取行数和列数
        row, col = len(matrix), len(matrix[0])
        # 检查矩阵第一列是否需要改变
        # 只要矩阵第一列有0，则第一列需要置为0
        for i in range(row):
            if matrix[i][0] == 0:
                # 找到0即可break退出循环
                firstcol = True
                break
        # 检查矩阵第一行是否需要改变
        # 只要矩阵第一行有0，则第一行需要置为0
        for i in range(col):
            if matrix[0][i] == 0:
                # 找到0即可break推出循环
                firstrow = True
                break
        # 从（1，1）开始检查，若matrix[i][j]==0
        # 则置matrix[i][0]=0,matrix[0][j]=0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # 把第一行为0所对应的列全部置为0
        for i in range(1, col):
            if matrix[0][i] == 0:
                for j in range(1, row):
                    matrix[j][i] = 0
        # 把第一列所对应的行全部置为0
        for i in range(1, row):
            if matrix[i][0] == 0:
                for j in range(1, col):
                    matrix[i][j] = 0
        # 检查是否许需要把第一列置为0
        if firstcol:
            for i in range(row):
                matrix[i][0] = 0
        # 检查是否需要把第一行置为0
        if firstrow:
            for i in range(col):
                matrix[0][i] = 0
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-20-73-Set-Matrix-Zeroes.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-73-set-matrix-zeroes/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
