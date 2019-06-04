# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-27 10:57:45
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-27 11:28:11

import random
import time

numbers = random.choices(range(0, 10), k=15)
numbers.sort()


def find_first(numbers, x):
    left, right = 0, len(numbers)-1
    while left <= right:
        middle = left+((right-left) >> 1)
        if numbers[middle] == x:
            if middle == 0:
                return 0
            elif numbers[middle-1] != x:
                return middle
            elif numbers[middle-1] == x:
                right = middle-1
        elif numbers[middle] > x:
            right = middle-1
        elif numbers[middle] < x:
            left = middle+1
    return None


def find_last(numbers, x):
    left, right = 0, len(numbers)-1
    while left <= right:
        middle = left+((right-left) >> 1)
        if numbers[middle] == x:
            if middle == len(numbers)-1:
                return middle
            elif numbers[middle+1] != x:
                return middle
            elif numbers[middle+1] == x:
                left = middle+1
        elif numbers[middle] > x:
            right = middle-1
        elif numbers[middle] < x:
            left = middle+1
    return None


def find_first_greater(numbers, x):
    left, right = 0, len(numbers)-1
    while left <= right:
        middle = left+((right-left) >> 1)
        if numbers[middle] >= x:
            if middle == 0:
                return 0
            elif numbers[middle-1] < x:
                return middle
            elif numbers[middle-1] >= x:
                right = middle-1
        elif numbers[middle] < x:
            left = middle+1
    return None


def find_last_less(numbers, x):
    left, right = 0, len(numbers)-1
    while left <= right:
        middle = left+((right-left) >> 1)
        if numbers[middle] <= x:
            if middle == len(numbers)-1:
                return middle
            elif numbers[middle+1] > x:
                return middle
            elif numbers[middle+1] <= x:
                left = middle+1
        elif numbers[middle] > x:
            right = middle-1
    return None


if __name__ == "__main__":
    x = 5
    print(numbers)
    print("Find First", x, find_first(numbers, x))
    print("Find Last", x, find_last(numbers, x))
    print("Find First Greater", x, find_first_greater(numbers, x))
    print("Find Last Less ", x, find_last_less(numbers, x))

