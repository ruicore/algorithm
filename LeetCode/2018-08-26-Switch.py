# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-08-26 11:23:46
# @Last Modified by:   何睿
# @Last Modified time: 2018-08-26 11:31:42

import random
from pprint import pprint


def switch():
    # 将所有的偶数放到前面，基数放到后面
    length = 30
    number_list = random.sample(range(-1000, 1000), length)
    print(number_list)
    i = 0
    j = length-1
    while i < j:
        while number_list[i] % 2 == 0:
            i += 1
        while number_list[j] % 2 != 0:
            j -= 1
        temp = number_list[i]
        number_list[i] = number_list[j]
        number_list[j] = temp
        i += 1
        j -= 1
    print(number_list)


if __name__ == "__main__":
    switch()
