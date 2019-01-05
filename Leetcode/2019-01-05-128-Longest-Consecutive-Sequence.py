# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-05 16:22:43
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-05 17:14:04

from pprint import pprint


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 哈希表，结果
        mydict, res, = {}, 0
        # 遍历所有数字
        for item in nums:
            # 重复的数字不算
            if item in mydict:
                continue
            # 获取当前数字左边一个数字构成的最大连续串，若不存在则返回0
            leftborder = mydict.get(item-1, 0)
            # 获取当前数字右边一个数字构成的最大连续串，如不存在则返回0
            rightborder = mydict.get(item+1, 0)
            # 连续串的长度更新为左右最大连续串加一
            length = leftborder+rightborder+1
            mydict[item] = length
            res = max(res, length)
            # 更新左边界
            mydict[item-leftborder] = length
            # 更新右边界
            mydict[item+rightborder] = length
        return res


if __name__ == "__main__":
    so = Solution()
    res = so.longestConsecutive([1, 2, 0, 1])
    print(res)
