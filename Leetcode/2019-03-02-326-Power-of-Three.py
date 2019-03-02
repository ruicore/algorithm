# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-03-02 15:38:41
# @Last Modified by:   何睿
# @Last Modified time: 2019-03-02 15:39:03

import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return 3**round(math.log(n, 3)) == n if n > 0 else False
