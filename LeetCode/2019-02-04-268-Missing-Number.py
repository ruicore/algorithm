# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-04 15:30:54
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-04 16:05:54


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 位运算  0^0^1^2^2^3^3^4^4 = 1
        # 即偶数次亦或结果为0，奇数次为本身
        # 给定的数范围从0到n共n个（丢失了一个），我们然i从0自增到n-1，另res初始化为n。
        # 对所有的数进行异或运算，重复出现的数字两两配对，抑或的结果为0
        # 落单的数字亦或会被保留
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res
