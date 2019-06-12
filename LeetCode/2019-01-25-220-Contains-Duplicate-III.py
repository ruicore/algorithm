# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-25 19:57:09
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-25 21:09:12

import collections


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or k <= 0 or t < 0: return False
        # 创建一个有序字典
        dic = collections.OrderedDict()
        for n in nums:
            # 这里使用了桶的思想
            key = n if not t else n // t
            for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            # False表示先进先出
            if len(dic) == k: dic.popitem(False)
            dic[key] = n
        return False
