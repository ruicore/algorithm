# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-08-23 14:13:36
# @Last Modified by:   何睿
# @Last Modified time: 2018-08-23 14:13:36

import random


def DirectInsertionSort():

    # 直接插入排序,递增排序：
    number_list = random.sample(range(0, 500), 20)
    print("%-*s" % (15, "UnSorted List"), number_list)
    length = len(number_list)
    for index in range(1, length):
        before = index-1
        compare = number_list[index]
        while before >= 0 and compare <= number_list[before]:
            number_list[before+1] = number_list[before]
            number_list[before] = compare
            before -= 1
    print("%-*s" % (15, "Sorted List"), number_list)


if __name__ == "__main__":
    DirectInsertionSort()
