# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-25 22:56:32
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-26 10:50:02


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 1 and 1 <= int(s) <= 26:
            return 1
        elif length == 1:
            return 0
        pretwo = 1 if int(s[0]) else 0
        temp = int(s[0:2])
        if temp < 10:
            preone = 0
        elif 11 <= temp <= 19 or 21 <= temp <= 26:
            preone = 2
        elif temp == 10 or temp == 20 or (temp > 26 and int(s[1]) != 0):
            preone = 1
        else:
            preone = 0
        res = preone
        for i in range(2, length):
            if not 0 < int(s[i]) <= 26:
                preone = 0
            if not 0 < int(s[i-1:i+1]) <= 26 or s[i-1] == '0':
                pretwo = 0
            res = preone+pretwo
            pretwo = preone
            preone = res
        return res


if __name__ == "__main__":
    so = Solution()
    res = so.numDecodings("12")
    print(res)
