# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-08-16 11:24:50
# @Last Modified by:   何睿
# @Last Modified time: 2018-08-16 12:32:49

import itertools


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        for i in range(n-1):
            result = ''.join([str(len(list(g)))+key for key,
                              g in itertools.groupby(result)])

        return result


if __name__ == "__main__":
    test = Solution()
    result = test.countAndSay(4)
    print(result)
