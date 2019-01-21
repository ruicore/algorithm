# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-21 11:56:34
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-21 19:36:15


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 字典，键为s中的字符，值为t中的字符
        # 键和值必须一一对应
        res = {}
        for x, y in zip(s, t):
            # 若键存在，则其值一定要和y相等
            if x in res:
                if not res.get(x) == y: return False
            else:
                # 若y已经作为其他键的值，直接返回False，因为这里要求键值一一对应
                if y in res.values(): return False
                else: res[x] = y
        # 上面的条件都满足，返回True
        return True
