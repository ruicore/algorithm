# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-12 11:05:40
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-12 12:12:24


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 如果只有一个值，直接返回
        if len(nums) == 1:
            return [nums]
        # 声明最终需要返回的答案
        res = []
        # 遍历数组中的元素
        for i, num in enumerate(nums):
            if i != 0 and num in nums[0:i]:
                continue
            # 去掉已经遍历的元素
            subnum = nums[:i]+nums[i+1:]
            # 把刚刚去掉的元素和剩下的元素所有可能的结果相加
            for subres in self.permuteUnique(subnum):
                res.append([num]+subres)
        return res

if __name__ == "__main__":
    so = Solution()
    print(so.permuteUnique([3,3,0,3]))