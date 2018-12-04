# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-01 17:16:36
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-03 10:16:07

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:
# https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length <= 2:
            return 0
        water, leftmax, rightmax, left, right = 0, 0, 0, 0, length-1

        while left < right:
            if height[left] > leftmax:
                leftmax = height[left]
            if height[right] > rightmax:
                rightmax = height[right]
            if leftmax <= rightmax:
                water += leftmax-height[left]
                left += 1
            elif rightmax < leftmax:
                water += rightmax-height[right]
                right -= 1
        return water


class Solution2:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 数组的长度，如果数组长度小于等于2，则一定装不了水
        length = len(height)
        if length <= 2:
            return 0
        # 声明两个数组，分别用于存储左边的最大值和右边的最大值
        leftmax, rightmax = [0]*length, [0]*length
        temp, water = 0, 0
        # 找到左边的最大值
        for index in range(length):
            if height[index] >= temp:
                temp = height[index]
            leftmax[index] = temp
        # 找到右边的最大值
        temp = 0
        for index in range(length-1, -1, -1):
            if height[index] >= temp:
                temp = height[index]
            rightmax[index] = temp
        # 遍历求和
        for index in range(length):
            water += min(leftmax[index], rightmax[index])-height[index]
        return water


class Solution3:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 数组的长度，如果数组长度小于等于2，则一定装不了水
        length = len(height)
        if length <= 2:
            return 0
        # 声明五个变量，总水量，左边最高柱的值，右边最高柱的值，左边柱子的索引，右边柱子的索引
        water, leftmax, rightmax, left, right = 0, 0, 0, 0, length-1
        # 只有左边索引小于右边索引才执行
        while left < right:
            # 首先判断是什么情形,如果是左低右高这种情形
            # 这里隐藏了一点是当height[left] <= height[right]时，leftmax一定小于等于 height[right]
            if height[left] <= height[right]:
                if leftmax > height[left]:
                    water += leftmax-height[left]
                else:
                    leftmax = height[left]
                left += 1
            # 这里隐藏了一点是当height[left]  height[right]时，rightmax一定小于等于height[left]
            if height[left] > height[right]:
                if rightmax > height[right]:
                    water += rightmax-height[right]
                else:
                    rightmax = height[right]
                right -= 1
        return water
