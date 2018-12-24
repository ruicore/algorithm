# LeetCode 85. Maximal Rectangle

## Description

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

## 描述

* 题意是给定一个二维的零一矩阵,1可以用来围成一些矩阵，题意要求是返回围城矩阵的面积最大值.

![85. Maximal Rectangle](https://wp.me/aaizn9-WH)

* 如上图，此题是第84题的转换题.84题在[这里](https://leetcode.com/problems/largest-rectangle-in-histogram)，解析在[这里](https://www.ruicore.cn/leetcode-84-largest-rectangle-in-histogram/).
* 我们将每一层都转换成为一个条形矩阵，转换的规则是：如果当前位置是1，将当前位置以及当前位置随对应列的上面所有的1相加，直到遇到第一个0为止，如果当前位置是0，则直接置为0.
* 这样已转换就成了和84题一样的题目.
* 二维矩阵的每一行都是一个84题的heights,我们返回其最大值即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-24 19:51:30
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-24 21:26:32


class Solution:
    # 这道题利用了思路转换，将矩阵转换成为了条形图.
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 如果矩阵为空，返回0
        if not matrix:
            return 0
        # 获取矩阵的行数，列数
        row, col = len(matrix), len(matrix[0])
        # 高度矩阵，同84题中的高度矩阵（柱状图）
        heights = [0 for _ in range(col)]
        # 最终返回的记过，初始化为0
        res = 0
        # 遍历每一行
        for i in range(row):
            for j in range(col):
                # 生成高度图
                # 如果当前位置是"1"，则高度加1
                if int(matrix[i][j]) == 1:
                    heights[j] += 1
                # 如果当前位置是0，则高度置为0，不论当前位置对应上面是否有"1"
                # 只要当前位置是0，则该位置的柱状图就是0.
                else:
                    heights[j] = 0
            # 调用子方法，此方法解决的问题为84题所问的问题.
            temp = self.largestRectangleArea(heights)
            # 取较大的结果
            res = res if res > temp else temp
        return res

    def largestRectangleArea(self, heights):
        # 栈，该矩阵的左边界，当前柱状图索引，矩阵右边界，结果
        stack, leftborder, current, rightborder, res = [], 0, 0, 0, 0
        for i in range(len(heights)):
            # 如果矩阵为空或者当前height[i]比栈顶索引对应的高度高则压入栈
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                # 只要height[i]比栈顶元素小且栈不为空则一直循环
                while stack and heights[i] < heights[stack[-1]]:
                    # 取出栈顶元素
                    current = stack.pop()
                    # 如果刚才取出的栈顶元素和此时的栈顶元素相等
                    # 则可以继续取栈顶元素，因为紧挨相同元素所觉决定的矩阵左右边界相等
                    while stack and heights[current] == heights[stack[-1]]:
                        current = stack.pop()
                    # height[current]矩阵的左边界为栈顶元素的索引
                    # 右边界为当前元素，其宽度为i-leftbofer-1
                    leftborder = stack[-1] if stack else -1
                    # 计算当前矩阵的面积
                    temp = (i-leftborder-1)*heights[current]
                    # 返回较大值
                    res = temp if temp > res else res
                # 把当前元素压入栈顶
                stack.append(i)
        # 如果栈不为空，就处理剩余的元素.
        if stack:
            # 此时剩下的所有元素的右边界是栈顶元素+1，并且在循环的过程中保持不变.
            rightborder = stack[-1]+1
            while stack:
                # 取出栈顶元素
                current = stack.pop()
                # 左边界为此时的栈顶元素索引，如果栈顶元素不存在则为-1
                leftborder = stack[-1] if stack else -1
                # 计算当前面积
                temp = (rightborder-leftborder-1)*heights[current]
                # 取较大值
                res = res if res > temp else temp
        return res


if __name__ == "__main__":
    so = Solution()
    res = so.maximalRectangle([
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]
    ])
    print(res)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-24-85-Maximal-Rectangle.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-85-maximal-rectangle/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
