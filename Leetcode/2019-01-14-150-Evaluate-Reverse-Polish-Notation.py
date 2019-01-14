# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-14 17:15:18
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-14 17:50:02


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack1, stack2 = [], []
        for i in range(len(tokens) - 1, -1, -1):
            stack1.append(tokens[i])
        operateset = set(["+", "-", "*", "/"])
        while stack1:
            top = stack1.pop()
            if top in operateset:
                num1, num2 = stack2.pop(), stack2.pop()
                stack2.append(self.operate(top, num1, num2))
            else:
                stack2.append(int(top))
        return stack2[-1]

    def operate(self, op, num1, num2):
        if op == "+":
            return num2 + num1
        if op == "-":
            return num2 - num1
        if op == "*":
            return num2 * num1
        if op == "/":
            return int(num2 / num1) if num1 != 0 else 0
