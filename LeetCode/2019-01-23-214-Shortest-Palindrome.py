# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-23 19:08:33
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-25 22:38:27


# 有关KMP的算法详解请关注：
# https://www.youtube.com/watch?v=V5-7GzOfADQ&t=70s
# https://www.youtube.com/watch?v=GTJr8OvyEVQ

class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # KMP next 数组
        _next = [0] * (2 * len(s) + 1)
        # 重新拼接字符串
        news = s + "$" + "".join(list(reversed(s)))
        j = 0
        # 构造_next数组
        for i in range(1, len(news)):
            if news[i] == news[j]:
                _next[i] = j + 1
                j += 1
            else:
                while j != 0 and news[i] != news[j]:
                    j = _next[j - 1]
                if news[i] == news[j]:
                    _next[i] = j + 1
                    j += 1
        return news[len(s) + 1:len(s) + len(s) - _next[-1] + 1] + s
