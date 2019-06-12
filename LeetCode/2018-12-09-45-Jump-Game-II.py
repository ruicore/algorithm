# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-09 11:04:53
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-09 16:38:33


# 45. Jump Game II

# Description

# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# Example:

# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Note:

# You can assume that you can always reach the last index.

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 记录步数
        count = 0
        # 下标
        index, length = 0, len(nums)
        # 只有第一个到倒数第二个之间才需要走，最后一个已经到达目的地，不需要在往下走
        while index < length-1:
            # 如果当前位置能直接走到最后一个位置，说明再走一次就可以到达尾部，返回count+1
            if index + nums[index] >= length-1:
                return count + 1
            # 寻找从index+1位置开始，到index + nums[index]，依次寻找能跳到最远位置的值
            # 能跳到最远位置的值，初始化为index
            maxindex = index
            # 最远的位置，初始化为index当前的位置加上当前位置能够跳的最远值
            temp = nums[index]+index
            # 依次遍历寻找
            for subindex in range(index+1, index+nums[index]+1):
                # 注意，这里不能取等号，因为如果能够从index位置一次跳到末尾，就不再需要中间多停留一次
                if nums[subindex]+subindex > temp:
                    temp = nums[subindex]+subindex
                    maxindex = subindex
            # 找到最大值，index跳到对应位置
            # 如果index没有变动
            if index == maxindex:
                index = nums[index]+index
            else:
                # 如果index变动
                index = maxindex
            # 步数记录自增一次
            count += 1
        return count


if __name__ == "__main__":
    so = Solution()
    res = so.jump([4, 1, 1, 3, 1, 1, 1])
    print(res)
