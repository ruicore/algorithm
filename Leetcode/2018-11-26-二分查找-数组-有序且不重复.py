# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-26 21:57:32
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-26 21:59:58


import random

numbers = random.sample(range(0, 200), 100)
numbers.sort()
x = 50


def find(x, numbers):
    low, high = 0, len(numbers)-1
    while low <= high:
        middle = low + ((high-low) >> 1)
        if numbers[middle] == x:
            return middle
        elif numbers[middle] < x:
            low = middle+1
        elif numbers[middle] > x:
            high = middle-1
    return None


def find_recursion(x, numbers, left, right):
    middle = left + ((right-left) >> 1)
    if numbers[middle] == x:
        return middle
    elif left >= right:
        return None
    elif numbers[middle] < x:
        return find_recursion(x, numbers, middle+1, right)
    elif numbers[middle] > x:
        return find_recursion(x, numbers, left, middle-1)


if __name__ == "__main__":
    res = find(x, numbers)
    res_recursion = find_recursion(x, numbers, 0, len(numbers))
    print(res)
    print(res_recursion)
