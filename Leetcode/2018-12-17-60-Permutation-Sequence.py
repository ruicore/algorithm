# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-17 10:15:58
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-17 11:00:08

import math


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1, n+1)]
        res = []
        denominator, numerator = k, k
        while denominator:
            numerator = math.factorial(n-1)
            quotient = denominator//numerator
            remainder = denominator % numerator
            if remainder:
                res.append(nums[quotient])
                del nums[quotient]
            else:
                res.append(nums[quotient-1])
                del nums[quotient-1]
            denominator = remainder
            n -= 1
        return ''.join(res+nums[::-1])


if __name__ == "__main__":
    so = Solution()
    res = so.getPermutation(4, 5)
    print(res)
