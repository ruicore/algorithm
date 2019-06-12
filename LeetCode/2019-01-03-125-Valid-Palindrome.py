# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-03 11:16:37
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-03 11:34:21


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        left, right = 0, len(s)-1
        while left < right:
            # 如果当前字符是数字或者字母
            if (s[left].isalpha() or s[left].isdigit()) and (s[right].isalpha() or s[right].isdigit()):
                # 如果相等则left向后走一步，right向前走一步
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    # 否则返回False
                    return False
            # 如果左边不是数字或者字符，则认为是满足回文符串的条件
            elif not (s[left].isalpha() or s[left].isdigit()):
                left += 1
            # 如果右边不是数字或者字符，则认为是满足回文字符串的条件
            elif not (s[right].isalpha() or s[right].isdigit()):
                right -= 1
        return True


if __name__ == "__main__":
    so = Solution()
    res = so.isPalindrome("0P")
