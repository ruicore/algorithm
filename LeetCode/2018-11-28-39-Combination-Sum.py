# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-28 18:20:58
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-18 07:11:56


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, index, path, res):

        if target == 0:
            res.append(list(path))

        for i in range(index, len(candidates)):
            if candidates[i] > target:
                return

            path.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, path, res)
            path.pop()
