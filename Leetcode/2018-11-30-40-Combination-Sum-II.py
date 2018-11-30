# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-30 18:26:44
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-30 22:57:55

import copy


# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# Each number in candidates may only be used once in the combination.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        start = 0
        sum_ = 0
        subindex = 0
        length = len(candidates)
        candidates.sort()
        candidatestack = []
        indexstack = []
        while start < length:
            while start != 0 and start < length and candidates[start] == candidates[start-1]:
                start += 1
            if start == length:
                break
            sum_ = 0
            subindex = start
            while True:
                while sum_ < target and subindex < length:
                    candidatestack.append(candidates[subindex])
                    indexstack.append(subindex)
                    sum_ += candidates[subindex]
                    subindex += 1
                if sum_ == target:
                    res.append(copy.deepcopy(candidatestack))
                if candidatestack:
                    sum_ -= candidatestack.pop()
                    indexstack.pop()
                if candidatestack:
                    sum_ -= candidatestack.pop()
                    subindex = indexstack.pop()+1
                while subindex < length and candidates[subindex-1] == candidates[subindex]:
                    subindex += 1
                while subindex == length and candidatestack:
                    sum_ -= candidatestack.pop()
                    subindex = indexstack.pop()+1
                    while subindex < length and candidates[subindex-1] == candidates[subindex]:
                        subindex += 1
                if not candidatestack:
                    break
            start += 1
        return res


if __name__ == "__main__":
    so = Solution()
    res = so.combinationSum2([1], 2)
    print(res)
