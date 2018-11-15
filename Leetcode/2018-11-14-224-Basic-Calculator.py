# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-14 16:59:14
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-14 20:53:36

import re

# Implement a basic calculator to evaluate a simple expression string.

# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

# Example 1:

# Input: "1 + 1"
# Output: 2
# Example 2:

# Input: " 2-1 + 2 "
# Output: 3
# Example 3:

# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.


class Solution(object):
    # 通用方法
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_stack = []
        ope_stack = []
        s = re.findall(r'[0-9]+|[+]+|[-]+|[(]|[)]', s)
        for item in s:
            if item == "(":
                ope_stack.append(item)
            elif item in ["+", "-"]:
                if not ope_stack or ope_stack[-1] == "(":
                    ope_stack.append(item)
                else:
                    self.sub_calculate(ope_stack, num_stack)
                    ope_stack.append(item)
            elif item == ")":
                if ope_stack:
                    while ope_stack[-1] != '(':
                        self.sub_calculate(ope_stack, num_stack)
                    ope_stack.pop()
            else:
                num_stack.append(int(item))
        if ope_stack:
            self.sub_calculate(ope_stack, num_stack)
        return num_stack[0]

    def sub_calculate(self, ope_stack, num_stack):
        ope = ope_stack.pop()
        if ope in ["+", "-"]:
            num_2 = num_stack.pop()
            num_1 = num_stack.pop()
            if ope == "+":
                num_stack.append(num_1+num_2)
            if ope == "-":
                num_stack.append(num_1-num_2)


class QuickSolution(object):
    # 快速方法
    def calculate(self, s):
        num = 0
        sign = 1
        stack = []
        total = 0

        for item in s:
            if item.isdigit():
                num = num * 10 + ord(item)-ord("0")
            elif item == "+":
                total += sign*num
                sign = 1
                num = 0
            elif item == "-":
                total += sign * num
                sign = -1
                num = 0
            elif item == "(":
                stack.append((total, sign))
                sign = 1
                total = 0
                num = 0
            elif item == ")":
                total += sign*num
                pretoatal, presign = stack.pop()
                total = pretoatal+presign*total
                num = 0
        if num:
            total += num*sign
        return total


if __name__ == "__main__":
    so = QuickSolution()
    res = so.calculate("1-(5)")
    print(res)
