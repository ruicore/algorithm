# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-22 10:15:22
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-22 11:26:53


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res, nums = [], [i+1 for i in range(n)]
        self.recursion(res, [], nums, 0, n, k)
        return res

    def recursion(self, res, path, nums, start, end, depth):
        if depth == 1:
            for i in range(start, end):
                res.append(path+[nums[i]])
        for i in range(start, end):
            self.recursion(res, path+[nums[i]], nums, i+1, end, depth-1)


if __name__ == "__main__":
    so = Solution()
    res = so.combine(4, 2)
    print(res)
