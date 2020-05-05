# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2020-05-05 15:29:17
# @Last Modified by:   何睿
# @Last Modified time: 2020-05-05 20:08:00

from typing import List
from copy import deepcopy
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if not s or not p:
            return []

        p_dict = defaultdict(int)
        tmp_dict = defaultdict(int)
        for char in p:
            p_dict[char] += 1

        for char in s[:len(p)]:
            tmp_dict[char] += 1

        res = []

        for i in range(0, len(s) - len(p)):
            if tmp_dict == p_dict:
                res.append(i)

            tmp_dict[s[i]] -= 1
            if tmp_dict[s[i]] == 0:
                tmp_dict.pop(s[i])
            tmp_dict[s[i + len(p)]] += 1

        if tmp_dict == p_dict:
            res.append(len(s) - len(p))
        return res

    def findAnagrams2(self, s: str, p: str) -> List[int]:

        if not s or not p:
            return []

        p_dict = defaultdict(int)
        for char in p:
            p_dict[char] += 1

        left, right, cnt = 0, 0, len(p)
        res = []

        while right < len(s):
            p_dict[s[right]] -= 1

            if p_dict[s[right]] >= 0:
                cnt -= 1
            if cnt == 0:
                res.append(left)
            if right - left + 1 == len(p):
                if p_dict[s[left]] >= 0:
                    cnt += 1
                p_dict[s[left]] += 1
                left += 1

            right += 1

        return res



