# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 14:57:31
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 15:16:35


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return '0'
        # 确定是不是负数
        isnegative = True if numerator * denominator < 0 else False
        # 返回商和余数
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        # 生成点号左边的部分
        s = str(quotient)
        if isnegative: s = "-" + s
        if remainder: s += '.'
        # start用于记录循环开始的位置
        start = len(s)
        nums = {remainder: start}
        while remainder:
            # 对剩下的数字进行计算
            quotient, remainder = divmod(remainder * 10, abs(denominator))
            # 添加到已经生成的结果中
            s += str(quotient)
            # 如果当前的余数已经出现过了
            if remainder in nums:
                s = s[:nums[remainder]] + '(' + s[nums[remainder]:] + ')'
                return s
            start += 1
            nums[remainder] = start
        return s