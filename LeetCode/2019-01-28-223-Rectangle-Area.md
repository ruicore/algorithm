# LeetCode 223. Rectangle Area

## Description

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

![rectangle_area](https://wp.me/aaizn9-16i)

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.

## 描述

在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。

每个矩形由其左下顶点和右上顶点坐标表示，如图所示。

示例:

输入: -3, 0, 3, 4, 0, -1, 9, 2
输出: 45

### 实现

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-28 20:01:58
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-28 22:42:49


class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        """
        分别获取第一个矩阵的长宽，第二个矩阵的长宽
        获取重叠部分的长和宽，如果长和宽都大于0，说明存在重叠的矩阵，否则不存在
        """
        # 第一个矩形的面积，第二个矩形的面积
        area1, area2 = (C - A) * (D - B), (G - E) * (H - F)
        # 重叠的长，重叠的宽
        _long, _width = min(C, G) - max(A, E), min(D, H) - max(B, F)
        # 如果长宽中有一个小于零，说明并不存在重叠的矩形，设置其面积为0，否则其面积为长*宽
        overlap = _long * _width if _long > 0 and _width > 0 else 0
        return area1 + area2 - overlap
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-28-223-Rectangle-Area.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-223-rectangle-area/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
