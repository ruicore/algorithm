# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-10 11:42:06
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-10 14:52:53


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordset, ans = set(wordDict), {}
        return self.recursion(ans, s, wordset)

    def recursion(self, ans, s, wordset):
        if not s:
            return None
        if s in ans:
            return ans.get(s)
        res = []
        for i in range(1, len(s)+1):
            if s[:i] in wordset:
                # 从当前位置的下面一层的所有组合
                combs = self.recursion(ans, s[i:], wordset)
                # 如果下面的一层有结果
                if combs:
                    # 将当前的字符串与后面的所有字符组合进行组合
                    for item in combs:
                        res.append(s[:i]+" "+item)
                elif i == len(s):
                    res.append(s[:i])
        ans[s] = res
        return res
