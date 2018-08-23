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
        for before in range(index-1, 0, -1):
            if number_list[index] < number_list[before] and number_list[index] >= number_list[before-1]:
                temp = number_list[index]
                DirectInsertionSortMove(number_list, before, index-1)
                number_list[before] = temp
                break
            if before == 1 and number_list[index] < number_list[0]:
                temp = number_list[index]
                DirectInsertionSortMove(number_list, before, index-1)
                number_list[before] = temp
                break
    print("%-*s" % (15, "Sorted List"), number_list)


def DirectInsertionSortMove(numbers, start, end):
    """
    把numbers数组编号[start,end]的数一次往后移动一个
    """
    for index in range(end, start-1, -1):
        numbers[index+1] = numbers[index]
    return None


if __name__ == "__main__":
    DirectInsertionSort()
