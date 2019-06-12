# LeetCode 59. Spiral Matrix II

## Description

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

## 描述

给定正整数n，以螺旋顺序生成填充有从1到n2的元素的方阵。

### 思路

* 此题目同第[48题Rotate Image](https://leetcode.com/problems/rotate-image)，[第54题Spiral Matrix](https://leetcode.com/problems/spiral-matrix)做法类似.第48题解析在[这里](https://www.ruicore.cn/leetcode-48-rotate-image/)，第54题解析在[这里](https://www.ruicore.cn/leetcode-54-spiral-matrix/).
* 同样，我们维护四个指针，rowtop：指向第一行，rowbot：指向最后一行，coleft:指向第一列，colright:指向最后一列。我们另外维护一个num用来记录当前位置填的值.

```python
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        num = 1
        # 初始化结果数组，每个位置都初始化为0
        res = [[0 for _ in range(n)] for _ in range(n)]
        rowtop, coleft, rowbot, colright = 0, 0, n-1, n-1
        while rowbot > rowtop and coleft < colright:
            # 填第一行
            for i in range(coleft, colright):
                res[rowtop][i] = num
                num += 1
            # 填最后一列
            for i in range(rowtop, rowbot):
                res[i][colright] = num
                num += 1
            # 填最后一列
            for i in range(colright, coleft, -1):
                res[rowbot][i] = num
                num += 1
            # 填第一列
            for i in range(rowbot, rowtop, -1):
                res[i][coleft] = num
                num += 1
            # 进入下一层
            rowtop += 1
            rowbot -= 1
            coleft += 1
            colright -= 1
        # 如果是奇数行，则最后一行需要单独填写
        if n % 2:
            for i in range(coleft, colright+1):
                res[rowtop][i] = num
                num += 1
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-17-59-Spiral-Matrix-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-59-spiral-matrix-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.