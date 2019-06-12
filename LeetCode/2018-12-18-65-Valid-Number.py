# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-18 11:37:46
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-18 13:31:37


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 首先去掉字符串首尾的空格字符
        s = s.strip()
        # num：数字出现的次数，exp：e出现的次数，operator：连续符号出现的次数，dot：点出现的次数，length:s中字符的个数
        num, exp, operator, dot, length = 0, 0, 0, 0, len(s)
        # 如果没有字符或者只有一个字符且不是数字,返回False
        if length == 0 or (length == 1 and not s[0].isnumeric()):
            return False
        # 如果不止一个字符且首字符不是数字
        elif not s[0].isnumeric():
            # 如果是"-"或者"+",operator自增一次
            if s[0] == "-" or s[0] == "+":
                operator += 1
            # 如果是".",dot自增一次
            elif s[0] == '.':
                dot += 1
            # 如果不是数字，且不是".","-","+",直接返回Fasle
            else:
                return False
        else:
            # 统计数字个数，num自增一次
            num += 1
        # 从索引为1的位置开始遍历
        for i in range(1, length):
            # 如果不是数组
            if not s[i].isnumeric():
                # 如果是字母"e"
                if s[i] == 'e':
                    # exp自增一次
                    exp += 1
                    # 如果e出现了不止一次，或者e出现在s中最后一个位置，返回False
                    if exp > 1 or i == length-1:
                        return False
                    # 如果e前面不是数字且前面一个字符不是点号或者e前面一个字符是点号但是点号之前数字一次都没有出现，返回False
                    elif not s[i-1].isnumeric() and (s[i-1] != '.' or num == 0):
                        return False
                # 如果当前位置是运算符"-"或者"+"，operator自增一次
                elif s[i] == '-' or s[i] == '+':
                    operator += 1
                    # 如果operator超过1个(operator表示连续的运算符)，或者运算符在最后一个位置，返回False
                    if operator > 1 or s[i-1] != 'e' or i == length-1:
                        return False
                # 如果当前位置是点号
                elif s[i] == '.':
                    # 点号个数自增一次
                    dot += 1
                    # 如果点号出现大于一次，或者点号之前出现了e(即exp大于0)，返回Fasle
                    if dot > 1 or exp > 0:
                        return False
                    # 如果点号前面不是数字且点号之前也不是运算符（"+","-"）,返回False
                    elif not s[i-1].isnumeric() and (s[i-1] != "-" and s[i-1] != "+"):
                        return False
                    # 如果点号在最后一个位置且点号之前不是数字，返回False
                    elif i == length-1 and not s[i-1].isnumeric():
                        return False
                # 如果不是数字，且不是"+","-",".","e"，返回False
                else:
                    return False
            # 如果是数字，num自增一次：表示数字出现了，operator重置为0，表示连续字符出现为0
            else:
                num += 1
                operator = 0
        # 以上条件都不满足，则表示是一个合法可以表示十进制数的字符串
        return True


if __name__ == "__main__":
    so = Solution()
    res = so.isNumber(".e1")
    print(res)
