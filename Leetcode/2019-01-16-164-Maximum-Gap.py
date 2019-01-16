# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 12:08:24
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 14:05:34

import math
import sys


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 获取数字的个数
        count = len(nums)
        # 如果小于两个数字，则根据题意返回0
        if count < 2:
            return 0
        # 确定所有数的范围，寻找最值和最小值
        maxnum, minnum = max(nums), min(nums)
        # 计算数与数之间的平均距离（例如有10个数字，则一共有9个区间，平均的区间差为（最大值-最小值/9）向上取整）
        gap = math.ceil((maxnum - minnum) / (count - 1))
        # 如果gap等于0，说明所有的数值相等，直接返回0
        if gap == 0:
            return 0
        # 计算需要多少个桶，桶个数为数组的返回/平均区间的范围+1
        size = int((maxnum - minnum) / gap) + 1
        # 存储每个桶的最小值，最大值
        bucketmin, bucketmax = [sys.maxsize] * size, [-sys.maxsize] * size
        for i in range(count):
            # 计算当前值应该放到哪个桶内
            index = int((nums[i] - minnum) / gap)
            # 放最小值
            bucketmin[index] = min(bucketmin[index], nums[i])
            # 放最大值
            bucketmax[index] = max(bucketmax[index], nums[i])
        premax, maxgap = bucketmax[0], 0
        # 最大的差值为当前桶的最小值减去前一个桶的最大值
        for i in range(1, size):
            if bucketmin[i] != sys.maxsize:
                maxgap = max(maxgap, bucketmin[i] - premax)
                premax = bucketmax[i]
        return maxgap
