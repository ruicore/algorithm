# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-08-24 09:11:10
# @Last Modified by:   何睿
# @Last Modified time: 2018-08-24 09:11:10

import random


def BubbleSort():
    number = 20
    number_list = random.sample(range(0, 1000), number)
    print("%-*s" % (15, "UnSorted List"), number_list)
    for index_max in range(number-2, -1, -1):
        flag = False
        for index in range(0, index_max+1):
            if number_list[index] > number_list[index+1]:
                temp = number_list[index+1]
                number_list[index+1] = number_list[index]
                number_list[index] = temp
                flag = True
        if not flag:
            break
    print("%-*s" % (15, "Sorted List"), number_list)

if __name__=="__main__":
    BubbleSort()