# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-28 18:20:58
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-30 18:09:32

        
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, index, path, res):
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            elif candidates[i] == target:
                res.append([candidates[i]] + path)
                break
            else:
                self.dfs(candidates, target -candidates[i], i, [candidates[i]] + path, res)


if __name__ == "__main__":
    a = [2, 3, 6, 7]
    target = 7
    so = Solution()
    so.combinationSum(a, target)
