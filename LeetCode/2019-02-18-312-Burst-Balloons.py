# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-18 14:52:28
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-18 15:44:09


class Solution:
    def maxCoins(self, nums: 'List[int]') -> 'int':
        # 如果数组为空，我们返回0
        if not nums: return 0
        # 声明一个二维矩阵，matrix[i][j]表示戳num[i]到num[j]的气球可以获得的最大值
        matrix = [[0] * len(nums) for _ in range(len(nums))]
        # left表示起点，right表示中点，count表示right-left的值
        # 辅助变量初始化为0
        left, right, count = 0, 0, 0
        for count in range(0, len(nums)):
            # 每一趟循环，left都从最左边开始
            left = 0
            # right表示所有可能的中点
            for right in range(count, len(nums)):
                # 临时变量用于记录最大值
                _max = 0
                # 从left到right中，我们以每一个位置为最后一个戳气球的位置
                for j in range(left, right + 1):
                    # 当前位置左边可以获得的最大值
                    _left = matrix[left][j - 1] if j - 1 >= left else 0
                    # 当前位置右边可以获得的最大值
                    _right = matrix[j + 1][right] if j + 1 <= right else 0
                    # 当前串的左边界的左边一个值
                    leftnum = nums[left - 1] if left - 1 >= 0 else 1
                    # 当前串的有边界的右边一个值
                    rightnum = nums[right + 1] if right + 1 < len(nums) else 1
                    # 以当前位置为嘴后一个戳气球的位置，可以获得的硬币个数
                    product = _left + nums[j] * leftnum * rightnum + _right
                    _max = max(_max, product)
                # 更新最大值
                matrix[left][right] = _max
                left += 1
        # matrix[0][len(nums) - 1]表示从0到len(nums)可以获得的最多的硬币个数
        return matrix[0][len(nums) - 1]