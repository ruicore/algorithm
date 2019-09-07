# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-09-07 07:59:40
# @Last Modified by:   何睿
# @Last Modified time: 2019-09-07 09:10:06


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        cnt, stack = 0, []
        for n in num:
            while cnt < k and stack and n < stack[-1]:
                cnt += 1
                stack.pop()
            if n == "0" and not stack:
                continue
            stack.append(n)

        return "".join(stack[0:len(stack) - (k - cnt)]) or "0"
