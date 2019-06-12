# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-06 17:49:23
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-06 21:41:22


class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(res, [], s)
        return res

    def dfs(self, res, path, s):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            sub = s[0:i]
            if sub == sub[::-1]:
                self.dfs(res, path+[sub], s[i:])
