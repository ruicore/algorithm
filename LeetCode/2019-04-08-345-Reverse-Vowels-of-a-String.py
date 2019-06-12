# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-08 22:07:12
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-08 22:07:12


class Solution:
    def reverseVowels(self, s: str) -> str:
        # 所有的元音字母
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        index = [i for i in range(len(s)) if s[i] in vowels]
        half, count = len(index) // 2, len(index) - 1
        s = list(s)
        # 交换所有的原因字母
        for i in range(half):
            s[index[i]], s[index[count - i]] = s[index[count - i]], s[index[i]]
        return ''.join(s)