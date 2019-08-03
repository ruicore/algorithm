# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-03 15:05:01
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-03 15:32:23


from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        start = 1
        for _ in range(1, n + 1):
            yield start
            if start * 10 <= n:
                start *= 10
            else:
                start = start + 1 if start < n else start // 10 + 1
                while not start % 10:
                    start //= 10
        return
