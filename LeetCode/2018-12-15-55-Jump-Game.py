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
        # 记录最远位置
        maxindex = 0
        for i in range(len(nums)):
            # 如果能偶到达当前位置并且当前位置能够到达的最远位置大于maxindex
            if maxindex >= i and i+nums[i] > maxindex:
                # 更新maxindex
                maxindex = i+nums[i]
            # 一旦maxindex大于等于最大索引，我们返回False
            if maxindex >= len(nums)-1:
                return True
        # 如果到末尾maxinde都小于最大索引，返回False
        return False


if __name__ == "__main__":
    so = Solution()
    res = so.canJump([3, 2, 1, 0, 4])
    print(res)
