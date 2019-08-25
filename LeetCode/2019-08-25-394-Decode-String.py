# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-25 09:19:03
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-25 10:17:59


class Solution:
    def decodeString(self, s: str) -> str:
        num, chr_stack, num_stack = 0, [], []
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                num_stack.append(num)
                chr_stack.append("[")
                num = 0
            elif char == ']':
                tmp = []
                while chr_stack and chr_stack[-1] != '[':
                    tmp.append(chr_stack.pop())
                chr_stack.pop()
                chr_stack.extend(reversed(tmp * num_stack.pop()))
            else:
                chr_stack.append(char)

        return "".join(chr_stack)

