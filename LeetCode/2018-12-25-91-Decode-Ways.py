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
        # 如果只有一个字符且部位则返回1
        if length == 1 and 1 <= int(s) <= 26:
            return 1
        # 如果只有一个字符且该字符为'0',则返回0
        elif length == 1:
            return 0
        pretwo = 1 if int(s[0]) else 0
        temp = int(s[0:2])
        # 如果第二个数是0，则没有可行的解码方案
        if temp < 10:
            preone = 0
        # 如果前两个字符构成的数字在11到19之间（包括两端），或在21到26之间（包括两端）
        # 则有一种解码方案
        elif 11 <= temp <= 19 or 21 <= temp <= 26:
            preone = 2
        # 如果前两个数构成的数字是10，20或者大于26的数且不是10的倍数
        # 则只有一种解码方案
        elif temp == 10 or temp == 20 or (temp > 26 and int(s[1]) != 0):
            preone = 1
        # 其他情况没有一种解码方案
        else:
            preone = 0
        res = preone
        # 当前位置的解码方案=上一个位置的解码方案数+上两个位置的解码方案数
        for i in range(2, length):
            # 如果当前位置是字符0，说明当前位置与(去掉当前字符，前面所有字符构成的字符串)的
            # 所有解码方案不能组成新的方案，当前方案数置为0
            if s[i] == '0':
                preone = 0
            # 如果当前位置与前一个位置构成的两位数不在10到26之间（包括两端）
            # 则当前位置不能与(去掉当前字符和前一个字符，前面所有字符构成的字符串)的
            # 所有解码方案不能组成新的方案，当前方案数置为0
            if not 10 <= int(s[i-1:i+1]) <= 26:
                pretwo = 0
            # 当前位置的解码方案为前两个位置解码方案之和
            res = preone+pretwo
            pretwo = preone
            preone = res
        return res


if __name__ == "__main__":
    so = Solution()
    res = so.numDecodings("12")
    print(res)
