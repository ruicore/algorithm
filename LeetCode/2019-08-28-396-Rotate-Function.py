# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-28 21:06:46
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-28 21:41:13


from typing import List


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        sum_, count = sum(A), len(A)
        product = sum(map(lambda x: x[0] * x[1], enumerate(A)))
        res = product

        for i in A[:-1]:
            product = product - sum_ + count * i
            res = max(res, product)

        return res
