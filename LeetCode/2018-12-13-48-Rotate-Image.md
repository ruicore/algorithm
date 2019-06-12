# LeetCode 48. Rotate Image

## Description

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

## 描述

给定一个n x n的二维矩阵，以顺时针方向旋转90度

要求:

您必须就地旋转图像，这意味着您必须直接修改输入的2D矩阵, 不要分配另一个2D矩阵并进行旋转,即空间复杂度O(1)

### 思路

![LeetCode 48. Rotate Image](https://www.ruicore.cn/leetcode-48-rotate-image/ )

* 这道题主要考察发现规律，在不申请额外矩阵空间的条件下，我们需要知道如何转换，如下图，以四维矩阵进行说明
* 如上图，需要观察发现：
* 1-->4-->16-->13-->1
* 2-->8-->15-->9-->2
* 3-->12-->14-->5-->3
* 如上是最外一层的变化，内层同样的道理
* 每一行除去最后一个元素为一个循环，因为在此循环中：
* 第一行的行标和最后一行的列标在循环过程中自身不变
* 最后一行的列标和最后一行的行标在循环过程中自身不变
* 最后一行的行标和第一列的列标在循环过程中自身不变
* 第一列的列标和第一行的行标在循环过程中自身不变
* 我们借助四个变量， rowtop, coleft, rowbot, colright，第一行行标，第一列列标，最后一行行标，最后一列列标
* 于是我们保存第一行的一个元素，将第一列的对应元素给第一行，将最后一行的元素给第一列，将最后一列的元素给最后一行，将第一行的元素给最后一列
* 如下

```python
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 正矩阵的维度
        rank = len(matrix[0])
        # 第一行，最左边的列，最后一行，最右边一列
        rowtop, coleft, rowbot, colright = 0, 0, rank-1, rank-1
        while rank > 1:
            for i in range(rank-1):
                # 第rowtop行的第coleft+i个元素保存
                temp = matrix[rowtop][coleft+i]
                # 将矩阵第一列的元素给矩阵第一行的元素
                matrix[rowtop][coleft+i] = matrix[rowbot-i][coleft]
                # 将矩阵最后一行的元素给矩阵第一列的元素
                matrix[rowbot-i][coleft] = matrix[rowbot][colright-i]
                # 将矩阵最后一列的元素给矩阵最后一行的元素
                matrix[rowbot][colright-i] = matrix[rowtop+i][colright]
                # 将矩阵第一行的元素给矩阵最后一列的元素
                matrix[rowtop+i][colright] = temp
            # 矩阵的行数（行列的个数相等，也可以表示为列数）减少2（上下各减少一行）
            rank -= 2
            # 最高的行数加一，表示行向内进一层，行数减少一行
            rowtop += 1
            # 最左边的列加一，表示向右进一层，列数减少一列
            coleft += 1
            # 最下边的行减一，表示向上进程一层，行数减少一行
            rowbot -= 1
            # 最右边的列减少一列，表示向左进一层，列数减少一列
            colright -= 1
        return
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-13-48-Rotate-Image.py)
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-48-rotate-image/)，欢迎转载，转载需保留文章来源，作者信息和本声明.