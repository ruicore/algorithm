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
