# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-09-09 15:39:48
# @Last Modified by:   何睿
# @Last Modified time: 2018-09-09 15:39:48

import sys
import math

lines = [list(map(int, line.strip().split()))
         for line in sys.stdin.readlines()]
test = lines[1]
n = lines[0][0]
die = 0
day = 0

i = n-2
j = n-1
temp = []
while i > -1:
    if test[i] > test[j] and test[j] != 0:
        die += 1
        test[j] = 0
    i -= 1
    j -= 1
for item in test:
    if item != 0:
        temp.append(item)
if die != 0:
    day += 1
while die != 0:
    die = 0
    i = len(temp)-2
    j = len(temp)-1
    while i > -1:
        if temp[i] > temp[j] and temp[j] != 0:
            die += 1
            temp[j] = 0
        i -= 1
        j -= 1
    if die != 0:
        day += 1
    temp_1 = temp
    temp = []
    for item in temp_1:
        if item != 0:
            temp.append(item)
    del temp_1
print(day)
