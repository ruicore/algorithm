# LeetCode 54. Spiral Matrix

## Description

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

## 描述

给定m×n个元素的矩阵（m行，n列），以螺旋顺序\[顺时针]返回矩阵的所有元素

## 思路

![54. Spiral Matrix](https://wp.me/aaizn9-RQ)

* 如上图,此题目同第48题Rotate Image做法非常类似，原题目在[这里](https://leetcode.com/problems/rotate-image/)，解析在[这里](https://www.ruicore.cn/leetcode-48-rotate-image/).
* 同样如上图，我们维护四个变量：rowtop, coleft, rowbot, colright，分别表示第一行行索引，第一列列索引，最后一行行索引，最后一列列索引
* 然后我们按照先从左至右取第一行的每个元素，然后从上至下取最后列的每一个元素，然后从右至左取最后一列的每一个元素，最后从下往上取第一列的每一个元素
* 每一圈就是一个while循环，也就是一层，我们一层一层的取，直到最后一层
* 需要注意的是如果矩阵只剩下一列或者只剩下一行我们需要单独拿出来取值，因为如果此时仍然放在while循环中，会导致这一行的元素别被重复取

```python
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 如果矩阵为空，直接返回空
        if not matrix:
            return []
        # 结果数组，用来保存最终答案
        res = []
        # row表示行数，col表示列数
        row, col = len(matrix), len(matrix[0])
        # 第一行行索引，第一列列索引，最后一行行索引，最后一列列索引
        rowtop, coleft, rowbot, colright = 0, 0, row-1, col - 1
        # 循环条件，当矩阵剩余不止一行且不止一列时，才进行循环
        while rowbot > rowtop and coleft < colright:
            # 取第一行
            for i in range(coleft, colright):
                res.append(matrix[rowtop][i])
            # 取最后一列
            for i in range(rowtop, rowbot):
                res.append(matrix[i][colright])
            # 取最后一行
            for i in range(colright, coleft, -1):
                res.append(matrix[rowbot][i])
            # 取第一列
            for i in range(rowbot, rowtop, -1):
                res.append(matrix[i][coleft])
            # 第一行字减一次，进入下一行
            rowtop += 1
            # 最后一行自减一次，进入上一行
            rowbot -= 1
            # 第一列自减一次，进入第二列
            coleft += 1
            # 最后一列自减一次，进入前一列
            colright -= 1
        # 如果最后还剩一行
        if rowtop == rowbot:
            for i in range(coleft, colright+1):
                res.append(matrix[rowtop][i])
        # 如果最后还剩一列
        elif coleft == colright:
            for i in range(rowtop, rowbot+1):
                res.append(matrix[i][coleft])
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-15-54-Spiral-Matrix.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-54-spiral-matrix/)，欢迎转载，转载需保留文章来源，作者信息和本声明.