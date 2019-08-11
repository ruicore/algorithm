# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-30 18:26:44
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-30 22:57:55

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.__dfs(0, [], res, target, candidates)
        return res

    def __dfs(self, start, path, res, target, candidates):

        if target == 0:
            res.append(list(path))
            return

        for i in range(start, len(candidates)):

            if i > start and candidates[i] == candidates[i - 1]:
                continue
            num = candidates[i]
            if num > target:
                return
            path.append(num)
            self.__dfs(i + 1, path, res, target - num, candidates)
            path.pop()
