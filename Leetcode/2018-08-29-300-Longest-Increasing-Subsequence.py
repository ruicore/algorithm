# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-08-29 13:41:23
# @Last Modified by:   何睿
# @Last Modified time: 2018-08-29 13:41:23

import random

"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 1:
            return 0
        if length == 1:
            return 1
        else:
            nums_count = [0]*length
            nums_count[0] = 1
            for index in range(1, length):
                max_num = 1
                for sub_index in range(0, index):
                    if nums[sub_index] < nums[index]:
                        if max_num < nums_count[sub_index] + 1:
                            max_num = nums_count[sub_index] + 1
                nums_count[index] = max_num
            return max(nums_count)


if __name__ == "__main__":
    solution = Solution()
    nums = random.sample(range(0, 100), 10)
    print(solution.lengthOfLIS(nums))
