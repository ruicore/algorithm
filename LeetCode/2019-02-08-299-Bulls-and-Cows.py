# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-08 18:00:07
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-08 18:22:24


class Solution:
    def getHint(self, secret: 'str', guess: 'str') -> 'str':
        A, B = 0, 0
        # 字典，用于统计secret出现的字符个数
        # unused用于统计guess中还没有和secret匹配的字符（指对应位置字符不等）
        match, unused = {}, []
        for x, y in zip(secret, guess):
            # 如果对应位置的字符相等，A自增一次
            if x == y:
                A += 1
            else:
                # 否则我们统计secret中当前字符出现的次数
                match[x] = match.get(x, 0) + 1
                # 并将guess中的当前字符添加到unused中
                unused.append(y)
        # 我们遍历unsed中的字符
        for item in unused:
            # 如果当前字符出现在了match字典中
            if item in match and match[item] > 0:
                # B自增一次
                B += 1
                # 字典中对应字符次数减少一次，表示当前字符已经被匹配了一次
                match[item] -= 1
        return str(A) + "A" + str(B) + "B"
