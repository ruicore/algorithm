# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-07-30 07:58:59
# @Last Modified by:   何睿
# @Last Modified time: 2019-07-30 08:03:10

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))
