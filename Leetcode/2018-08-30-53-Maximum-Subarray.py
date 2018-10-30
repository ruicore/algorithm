# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-08-30 19:43:04
# @Last Modified by:   何睿
# @Last Modified time: 2018-08-30 19:43:24


"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        temp_max_sum = nums[0]
        try:
            for item in nums[1:]:
                if item >= temp_max_sum+item:
                    temp_max_sum = item
                else:
                    temp_max_sum += item
                if temp_max_sum >= max_sum:
                    max_sum = temp_max_sum
        except:
            return nums[0]
        return max_sum


if __name__ == "__main__":
    so = Solution()
    re = so.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(re)
