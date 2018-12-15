# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-15 17:13:28
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-15 17:19:47


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxindex = 0
        for i in range(len(nums)):
            if i+nums[i] > maxindex and maxindex >= i:
                maxindex = i+nums[i]
            if maxindex >= len(nums)-1:
                return True
        return False

if __name__ == "__main__":
    so = Solution()
    res = so.canJump([3,2,1,0,4])
    print(res)