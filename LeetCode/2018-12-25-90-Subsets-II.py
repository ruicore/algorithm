# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-25 21:24:06
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-25 21:41:42

import copy


class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums = sorted(nums)
        self.recursion(res, [], nums, 0, len(nums))
        return res

    def recursion(self, res, path, nums, start, end):
        if start == end:
            return
        for i in range(start, end):
            if i != start and nums[i] == nums[i-1]:
                continue
            else:
                path.append(nums[i])
                res.append(copy.deepcopy(path))
                self.recursion(res, path, nums, i+1, end)
                path.pop()


if __name__ == "__main__":
    so = Solution()
    res = so.subsetsWithDup([1, 1, 6, 2])
    print(res)
