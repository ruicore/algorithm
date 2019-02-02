# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-02 08:52:08
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-02 09:01:08


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 声明结果数组，第一个位置（索引0）一定要初始化为1
        res = [1 for _ in range(len(nums))]
        # 辅助变量
        _product = nums[-1]
        # 正向遍历，获取当前位置左边的所有数字乘积的值
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        # 反向遍历，_product表示当前位置右边的数所有乘积的值
        for i in range(len(nums) - 2, -1, -1):
            # 当前位置的值等与当前位置左右两边所有数的乘积
            res[i] = _product * res[i]
            _product *= nums[i]
        # 返回结果
        return res
