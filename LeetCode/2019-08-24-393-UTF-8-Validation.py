# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-24 10:55:33
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-24 11:59:50


import re
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        next_ = 0
        pattern = re.compile("0b(.*?)0.*")
        while next_ != -1 and next_ < len(data):
            next_ = self.__check(next_, data, pattern)

        return False if next_ == -1 else True

    def __check(self, start, data, pattern):

        num = data[start]
        if not num & 0b10000000:
            return start + 1
        elif num & 0b11000000 == 0b10000000:
            return -1
        else:
            match = pattern.match(str(bin(num)))
            if not match:
                return -1
            length = match.span(1)[1] - match.span(1)[0]
            end = start + length
            if length > 4 or end > len(data):
                return -1
            if all(map(lambda i: data[i] & 0b11000000 == 0b10000000, range(start + 1, end))):
                return start + length
            return -1
