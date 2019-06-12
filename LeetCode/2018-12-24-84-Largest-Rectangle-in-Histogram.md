# LeetCode 84. Largest Rectangle in Histogram

## Description

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

![histogram](https://wp.me/aaizn9-Wz)

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

![histogram_area](https://wp.me/aaizn9-WA)

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10

## 描述

给定n个非负整数表示直方图的条形高度，其中每个条形的宽度为1，找到直方图中最大矩形的区域。

* 题意：给定一些非负整数，这些整数表示宽度为1，高度为该整数值的直方图，直方图构成了一些矩形，返回面积最大的矩形的面积值.

### 思路一

* 从每一个直方图的条形考虑，它能够围城的矩形宽度是：以该条形为起点，左边的连续高度等于大于此直方的条形数+右边的连续高度大于等于此直方图的条形数+1.
* 我们可以求得每一个矩形的面积，然后返回其最大面积.
* 该方法会**超时**.

### 思路二

* 我们利用栈来确定一个矩阵的左右边界.
* 当heights\[i]大于栈顶元素时，我们把该元素的索引\[i]压入栈顶\(栈内的元素递增，因此每个元素E能构成的矩阵中，E的前一个元素就是其矩阵的左边界.)
* 当遇到小于栈顶元素的时候，说明栈顶元素遇到了右边界：
1. 我们把栈顶元素弹出，零current = stack.pop(),该元素的左边界leftborder = stack\[-1],右边界是当前元素i，于是该元素的能够成的矩阵面积是:
2. temp = (i-leftbofer-1)*heights\[current]，我们把当前值与area\(初始化为0)比较，如果temp大于area则更新area =temp,否则都不做.
3. 紧接着，我们继续把当前元素与栈顶元素比较，如果仍然大于，则继续上述1，2步.
* 最后stack中剩下一些元素，我们令rightborder = stack\[-1]+1,current =stack.pop\(),leftborder = stack[-1]\(当stack为空则leftborder = -1)
* temp = (rightborder-leftbofer-1)*heights\[current]，我们把当前值与area，如果temp大于area则更新area =temp,否则都不做.
* 在处理stack剩余中的元素时，不断更新current =stack.pop\()，leftborder = stack[-1]，rightborder保持不变，计算面积，直到stack变成了空.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-24 12:35:16
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-24 16:33:35


class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 思路的关键是当heights[i]小于heights[i-1],则heights[i-1]已经找到了右边界,而左边界已经知道
        # 则当前情况就可以计算了.
        if not heights:
            return 0
        length = len(heights)
        area, leftborder, rightborder, current, stack = 0, 0, 0, 0, []
        stack.append(0)
        for i in range(1, length):
            # 当栈为空，或者当前元素比栈顶元素大则直接压入栈.
            # 栈中元素是递增的，则针对栈中的元素，其前一个元素就是其左边界.
            # 如果当前值比栈顶元素小，说明栈顶元素已经遇到了右边界.
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
            # 当左右边界已经确定，则该方块就可以计算.
            else:
                # 当heights[i]小于栈顶元素时，持续计算
                while stack and heights[i] < heights[stack[-1]]:
                    current = stack.pop()
                    # 如果栈顶元素是相等的，其左右边界也是相等的，计算最左边的就可以.
                    while stack and heights[current] == heights[stack[-1]]:
                        current = stack.pop()
                    # 取栈顶元素左边的边界.
                    leftborder = stack[-1] if stack else -1
                    # 计算当前的面积.
                    # 面积 = （当前元素右边界-左边界-1）*当前元素高度
                    temp = (i-leftborder-1)*heights[current]
                    area = area if area > temp else temp
                stack.append(i)
        # 处理stack中剩余的元素，处理方式与上面一样.
        # 这里要注意的是，他们的右边界都是一样的.
        rightborder = stack[-1]+1
        while stack:
            current = stack.pop()
            leftborder = stack[-1] if stack else -1
            temp = (rightborder-leftborder-1)*heights[current]
            area = area if area > temp else temp

        return area


if __name__ == "__main__":
    so = Solution()
    res = so.largestRectangleArea([2, 1, 2])
    print(res)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-24-84-Largest-Rectangle-in-Histogram.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-84-largest-rectangle-in-histogram/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
