# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-08-29 22:31:16
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-21 19:23:52


import re
import random


numlist = random.sample(range(0, 15000), 4001)

# 快速排序
def quicksort(numlist, left, right):
    if left >= right:
        return None
    left, middle, right = partion(numlist, left, right)
    quicksort(numlist, left, middle-1)
    quicksort(numlist, middle+1, right)
    return None


def partion(numlist, left, right):
    i, j = left, left
    pivot = numlist[right]
    while j <= right:
        if numlist[j] < pivot:
            temp = numlist[j]
            numlist[j] = numlist[i]
            numlist[i] = temp
            i += 1
            j += 1
        else:
            j += 1
    numlist[right] = numlist[i]
    numlist[i] = pivot
    return left, i, right

# 归并排序
def mergesort(numlist, left, right):
    if left >= right:
        return None
    middle = (left+right)//2
    mergesort(numlist, left, middle)
    mergesort(numlist, middle+1, right)
    merge(numlist, left, middle, right)


def merge(numlist, left, middle, right):
    len_left = middle-left+1
    len_right = right - middle
    temp = []
    i, j = left, middle+1
    while len_left > 0 and len_right > 0:
        if numlist[i] <= numlist[j]:
            temp.append(numlist[i])
            i += 1
            len_left -= 1
        else:
            temp.append(numlist[j])
            j += 1
            len_right -= 1
    if len_left > 0:
        temp.extend(numlist[i:middle+1])
    if len_right > 0:
        temp.extend(numlist[j:right+1])
    j = 0
    for i in range(left, right+1):
        numlist[i] = temp[j]
        j += 1
    return None


print(numlist)
# quicksort(numlist, 0, 29)
mergesort(numlist,0,4000)
print(numlist)
