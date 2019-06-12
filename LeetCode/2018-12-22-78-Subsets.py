# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-22 11:41:12
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-22 12:08:29

import copy


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        length = len(nums)
        self.recursion(res, nums, [], 0, length)
        return res

    def recursion(self, res, nums, path, start, end):
        if start == end:
            return
        for i in range(start, end):
            path.append(nums[i])
            res.append(copy.deepcopy(path))
            self.recursion(res, nums, path, i+1, end,)
            path.pop()


if __name__ == "__main__":
    so = Solution()
    res = so.subsets([1, 2, 3])
    print(res)
