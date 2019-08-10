# LeetCode 391. Perfect Rectangle

## Description

Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).

Example 1:

```py
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.
```
Example 2:

```py
rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.
```

Example 3:

```py
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.
 
```

Example 4:

```py
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
```

## 描述

我们有 N 个与坐标轴对齐的矩形, 其中 N > 0, 判断它们是否能精确地覆盖一个矩形区域。

每个矩形用左下角的点和右上角的点的坐标来表示。例如， 一个单位正方形可以表示为 [1,1,2,2]。 ( 左下角的点的坐标为 (1, 1) 以及右上角的点的坐标为 (2, 2) )。

```py
示例 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

返回 true。5个矩形一起可以精确地覆盖一个矩形区域。
```

示例 2:

```py
rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

返回 false。两个矩形之间有间隔，无法覆盖成一个矩形。
```
 
示例 3:

```py
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

返回 false。图形顶端留有间隔，无法覆盖成一个矩形。
```
 
示例 4:

```py
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

返回 false。因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 发现特点，举行变的顶点只能出现奇数次，并且总个数一定为 4 个。
* 统计出现过的奇数次的点的个数，找到其中最大的点和最小的点，计算面积；计算所有矩阵的面积的和；判断这两个面积是否相等。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-10 12:09:46
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-10 12:09:46

from typing import List
from collections import defaultdict


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        point_table = defaultdict(int)

        area = 0
        for line in rectangles:
            leftx, lefty, rightx, righty = line
            point_table[(leftx, lefty)] += 1
            point_table[(rightx, righty)] += 1
            point_table[(leftx, righty)] += 1
            point_table[(rightx, lefty)] += 1
            area += (rightx - leftx) * (righty - lefty)

        vertex = [x for x in point_table if point_table[x] & 1]
        if len(vertex) != 4: # 如果不是 4 个，直接返回 False
            return False

        min_, max_ = min(vertex), max(vertex)
        (minx, miny), (maxx, maxy) = min_, max_

        return (maxx - minx) * (maxy - miny) == area
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-08-10-391-Perfect-Rectangle.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-391-perfect-rectangle/) ，作者信息和本声明.
