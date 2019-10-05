# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-10-05 20:01:30
# @Last Modified by:   何睿
# @Last Modified time: 2019-10-05 20:02:43


from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ['FizzBuzz' if not i % 15 else 'Buzz' if not i % 5 else 'Fizz' if not i % 3 else str(i) for i in range(1, n + 1)]
