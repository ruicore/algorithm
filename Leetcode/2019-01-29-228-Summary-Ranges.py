# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-29 20:49:54
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-29 21:06:11


class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # 如果没有数字，返回空数组
        if not nums: return []
        # 结果数组，存储每一个区间首位的字符，记录当前区间字符的个数（不包括起点）
        res, _str, count = [], str(nums[0]), 0
        for i in range(1, len(nums)):
            # 如果当前数字与前一个数字连续，count加一
            if nums[i - 1] + 1 == nums[i]:
                count += 1
            else:
                # 如果count为0，说明当前的区间只有一个数字
                if not count:
                    # 我们直接将这个数字放入结果数组中
                    res.append(_str)
                else:
                    # 如果count不为零，说明当前连续的区间不止一个数字，我们以nums[i - 1]为区间的结尾
                    # 并在两个数字之间加上"->"
                    res.append(_str + "->" + str(nums[i - 1]))
                _str, count = str(nums[i]), 0
        # 处理最后剩余的数字，如果_str不为空且count不为0，说明存在一个区间
        # 且需要加上"->"符号
        if _str and count:
            res.append(_str + "->" + str(nums[-1]))
        # 否则如果_str不为零count为0，说明当前只有一个数字
        elif _str:
            res.append(_str)
        # 返回最终结果
        return res
    