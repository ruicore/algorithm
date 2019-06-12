# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-25 15:11:08
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-25 16:25:11


class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 如果有一个字符串为空，或者两个字符串的长度不相等，则返回False
        if not s1 or not s2 or len(s1) != len(s2):
            return False
        # 如果字符串长度为1，并且字符相等则返回True
        elif len(s1) == 1 and s1 == s2:
            return True
        # 如果两个字符含有的字符不同，返回False
        elif sorted(s1) != sorted(s2):
            return False
        length = len(s1)
        for i in range(1, length):
            left, right = s1[0:i], s1[i:length]
            # 每一个位置都被分开
            # 如果 左==左 and 右 == 右 或者 左==右 and 右== 左则返回Ture
            if (self.isScramble(left, s2[0:i]) and self.isScramble(right, s2[i:len(s2)])) or \
                    (self.isScramble(left, s2[len(s2) - i:len(s2)]) and self.isScramble(right, s2[0:len(s2)-i])):
                return True
        # 否则返回False
        return False


if __name__ == "__main__":
    so = Solution()
    res = so.isScramble("abcdefghijklmnopq", 'efghijklmnopqcadb')
    print(res)
