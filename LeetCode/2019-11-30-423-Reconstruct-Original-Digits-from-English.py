# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-11-30 13:15:30
# @Last Modified by:   何睿
# @Last Modified time: 2019-11-30 13:28:08


from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        res = {}
        count = Counter(s)
        for key, char in zip([0, 2, 4, 6, 8], ['z', 'w', 'u', 'x', 'g']):
            res[key] = count.get(char, 0)
        res[1] = count.get('o', 0) - res[0] - res[2] - res[4]
        res[3] = count.get('h', 0) - res[8]
        res[5] = count.get("f", 0) - res[4]
        res[7] = count.get('s', 0) - res[6]
        res[9] = count.get('i', 0) - res[6] - res[8] - res[5]

        return ''.join(str(num) * res[num] for num in range(0, 10))
