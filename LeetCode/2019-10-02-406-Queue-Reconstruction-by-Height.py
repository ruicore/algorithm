# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-10-02 11:58:14
# @Last Modified by:   何睿
# @Last Modified time: 2019-10-02 16:12:42

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = [None for _ in range(len(people))]
        for pair in sorted(people):
            h, k = pair[0], pair[1]
            if k == 0:
                idx = self.first_not_None(result, -1)
            else:
                idx = self.find_idx(result, h, k)
            result[idx] = pair
        return result

    def find_idx(self, result, h, k):

        cnt, start = 0, -1

        for start, people in enumerate(result):
            if people is None or people[0] >= h:
                cnt += 1
            if cnt == k:
                break

        return self.first_not_None(result, start)

    def first_not_None(self, result, start):
        for i in range(start + 1, len(result)):
            if result[i] is None:
                return i

    def reconstructQueue2(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        result = []
        for p in people:
            result.insert(p[1], p)
