# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-11-30 16:32:47
# @Last Modified by:   何睿
# @Last Modified time: 2019-11-30 16:44:05

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_count = defaultdict(int)
        res, left, right, count_s = 0, 0, 0, len(s)

        max_repeat_count = 0
        while right < count_s:
            window_count[s[right]] += 1
            max_repeat_count = max(max_repeat_count, window_count[s[right]])

            while right - left + 1 - max_repeat_count > k:
                window_count[s[left]] -= 1
                max_repeat_count = max(max_repeat_count, window_count[s[left]])
                left += 1

            res = max(res, right - left + 1)
            right += 1

        return res

