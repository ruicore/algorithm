# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-25 20:55:39
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-25 21:02:34

class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        i = 0
        res = []
        for i in  range(2**n):
            # 
            res.append(i^(i>>1))
        return res

if __name__ == "__main__":
    so = Solution()
    res = so.grayCode(2)
    print(res)