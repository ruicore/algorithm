# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-09-03 22:35:31
# @Last Modified by:   何睿
# @Last Modified time: 2019-09-04 08:59:55

from typing import List
from itertools import combinations


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        minutes = {i: 2**i for i in range(6)}
        hours = {i: 2**(i - 6) for i in range(6, 10)}
        times = map(lambda x: self.__transfer(x, minutes, hours), combinations(list(range(10)), num))
        
        return filter(lambda x: x is not None, times)

    def __transfer(self, com, minutes, hours):
        minute = sum(map(lambda x: minutes.get(x, 0), com))
        hour = sum(map(lambda x: hours.get(x, 0), com))
        return "{}:{:02d}".format(hour, minute) if hour <= 11 and minute <= 59 else None
