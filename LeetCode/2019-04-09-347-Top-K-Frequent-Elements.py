# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-09 12:37:36
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-09 15:57:00

from collections import Counter


class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        # 桶
        bucket = dict()
        # 构建字典，键位数字，值为该数字出现过的次数
        table = Counter(nums)
        result, count = [], 0
        # 以元素出现的次数位键，该次数下的所有元素构成的 List 为值
        for num, times in table.items():
            if times not in bucket: bucket[times] = []
            bucket[times].append(num)
        # 出现的最大次数
        maxtime = max(table.values())

        for time in range(maxtime, 0, -1):
            # 如果该次数下有元素
            if time in bucket:
                # 提取当前次数下的所有元素到结果中
                result.extend(bucket[time])
                count += len(bucket[time])
            if count == k: break
        return result