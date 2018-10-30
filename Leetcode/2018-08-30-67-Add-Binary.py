# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-08-30 21:15:13
# @Last Modified by:   何睿
# @Last Modified time: 2018-08-30 21:15:35


"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        result = []
        longest = {}
        if len_a < len_b:
            num_min = len_a
            longest.setdefault('a', b)
            left = len_b-len_a
        else:
            num_min = len_b
            longest.setdefault('a', a)
            left = len_a-len_b
        temp = 0
        for index in range(1, num_min+1):
            temp = temp+int(a[-index])+int(b[-index])
            if temp >= 2:
                result.insert(0, temp-2)
                temp = 1
            else:
                result.insert(0, temp)
                temp = 0
        for index in range(left-1, -1, -1):
            temp = temp+int(longest.get('a')[index])
            if temp >= 2:
                result.insert(0, temp-2)
                temp = 1
            else:
                result.insert(0, temp)
                temp = 0
        if temp:
            result.insert(0, temp)
        return ''.join(str(x) for x in result)


if __name__ == "__main__":
    so = Solution()
    re = so.addBinary("1111", "1111")
    print(re)
