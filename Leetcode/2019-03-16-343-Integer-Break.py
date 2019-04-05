# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-03-16 20:48:51
# @Last Modified by:   何睿
# @Last Modified time: 2019-03-16 20:48:51
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-12 06:50:01
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-12 18:58:52


class Solution:
    def integerBreak(self, n: int) -> int:
        tmp = [1, 2, 4, 6, 9]
        for i in range(5, n - 1):
            tmp.append(3 * tmp[i - 3])
        return tmp[n - 2]

    def integerBreak2(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        tmp = [4, 6, 9]
        for i in range(n - 6):
            tmp[i % 3] *= 3
        return tmp[(n - 1) % 3]
