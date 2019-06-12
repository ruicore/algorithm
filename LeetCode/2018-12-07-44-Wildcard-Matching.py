# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-07 11:09:12
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-08 11:20:23

# 44. Wildcard Matching
# Description
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Note:

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:

# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:

# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:

# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lens, lenp = len(s), len(p)
        if lens == 0 and lenp == 0:
            return True
        rownum, colnum = lenp+1, lens+1
        boolmatrix = [False]*(rownum*colnum)
        # 初始化
        boolmatrix[0] = True
        for row in range(1, lenp+1):
            if boolmatrix[(row-1)*colnum] and p[row-1] == '*':
                boolmatrix[row*colnum] = True
            else:
                break
        for col in range(1, lens+1):
            for row in range(1, lenp+1):
                if (p[row-1] == s[col-1] or p[row-1] == '?') and (boolmatrix[(row-1)*colnum+col-1]):
                    boolmatrix[row*colnum+col] = True
                if (p[row-1] == '*') and (boolmatrix[(row-1)*colnum+col] or boolmatrix[row*colnum+col-1]):
                    boolmatrix[row*colnum+col] = True
        return boolmatrix[rownum*colnum-1]


class Solution2:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lens, lenp = len(s), len(p)
        indexp, indexs, indexstar, matcheds = 0, 0, -1, 0
        if lens == 0 and lenp == 0:
            return True
        # 循环条件，还没有遍历到s尾部时才继续执行
        while indexs < lens:
            # 当p还没有到达尾部，且s和p对应位置相等或p位置为?号时
            if indexp < lenp and (s[indexs] == p[indexp] or p[indexp] == '?'):
                indexs += 1
                indexp += 1
            # 当p还没有到达尾部且s和p对应位置不相等，且p为*号
            elif indexp < lenp and p[indexp] == "*":
                # 记下此时*号的位置
                indexstar = indexp
                # 记下此时*号对应匹配的s中字符的位置，此时还不确定*号是否需要和此字符匹配
                matcheds = indexs
                # 继续匹配
                indexp += 1
            # 当s和p对应位置不等，且p位置不为*，检查前面是否有*号
            elif indexstar != -1:
                # 如果有，则说明前面的*号需要匹配一个字符，matcheds自增一个，indexp指向后面一个，indexs重新开始于matcheds
                matcheds += 1
                indexp = indexstar+1
                indexs = matcheds
            # 如果以上条件都不满足（即不满足s和p对应位置相等，且不满不p前面位置有8号）
            else:
                # 查找失败，返回False
                return False
        # 如果在s遍历完成之后，p还有剩余，则检查p剩余的内容
        while indexp < lenp:
            # 只要p中剩余的内容有一个不是*，返回False
            if p[indexp] != '*':
                return False
            indexp += 1
        return True


if __name__ == "__main__":
    so = Solution2()
    res = so.isMatch(s="aaaa", p="***a")
    print(res)
