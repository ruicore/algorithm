# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-02 13:04:40
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-02 15:26:38

import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        if not envelopes: return 0

        # 以信封的宽度和高度排序，宽度小的在前，宽度一样，高度大的在前
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        tails = list()

        # 所有的高度构成一个数组，寻找此数组中的连续最长递增序列
        for _, num in envelopes:
            index = bisect.bisect_left(tails, num)
            if index == len(tails):
                tails.append(num)
            else:
                tails[index] = num
        return len(tails)
