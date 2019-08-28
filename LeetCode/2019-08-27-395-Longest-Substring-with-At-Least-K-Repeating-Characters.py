# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-27 21:07:09
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-28 08:40:37

from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        for key, v in Counter(s).items():
            if v < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(key))
        return len(s)
