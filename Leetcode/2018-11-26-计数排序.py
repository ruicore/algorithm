# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-26 15:31:08
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-26 15:38:42

import random


length = 110
numlist = random.choices(range(0, 100), k=length)


def count_sort(numlist):
    max_ = 0
    # assume all number is not negative
    for item in numlist:
        if item > max_:
            max_ = item
    a = [0] * (max_+1)
    for item in numlist:
        a[item] += 1
    for i in range(1, len(a)):
        a[i] = a[i-1]+a[i]
    result = [0]*(len(numlist))
    for item in numlist[::-1]:
        result[a[item]-1] = item
        a[item] -= 1
    return result


print(numlist)
print(count_sort(numlist))
