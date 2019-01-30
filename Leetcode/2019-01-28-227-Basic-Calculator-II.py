# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-28 20:41:10
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-28 21:28:48


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 声明两个栈，用于存储数字和操作符
        stack1, stack2 = [], []
        # num用于从字符串中取出数字
        num = 0
        for item in s:
            # 取数字
            if item.isdigit():
                num = num * 10 + ord(item) - ord("0")
            # 如果为空则继续执行
            elif item == " ":
                continue
            else:
                # 向数字栈中添加数字
                stack1.append(num)
                # 数字重置为0
                num = 0
                # 如果符号栈为空，将当前符号压入栈
                if not stack2:
                    stack2.append(item)
                else:
                    # 如果当前操作符优先级大于等于符号栈栈顶操作符，我们持续进行运算
                    while stack2 and self.compare(stack2[-1], item):
                        # 从数字栈中取出两个数字
                        num1, num2 = stack1.pop(), stack1.pop()
                        # 对这两个数字进行当前符号的运算，并将运算结果压入数字栈
                        stack1.append(self.operate(stack2.pop(), num2, num1))
                    # 将当前符号压入符号栈
                    stack2.append(item)
        # 将最后剩下的数字压入数子栈
        stack1.append(num)
        # 对剩下的数字和符号进行运算
        while stack2 and stack1:
            num1, num2 = stack1.pop(), stack1.pop()
            stack1.append(self.operate(stack2.pop(), num2, num1))
        return stack1.pop()

    def operate(self, operator, num1, num2):
        # 运算函数
        if operator == "+": return num1 + num2
        if operator == "-": return num1 - num2
        if operator == "*": return num1 * num2
        if operator == "/": return num1 // num2

    def compare(self, op1, op2):
        # op2的优先级<=op1的优先级返回True
        # 否则返回False
        if (op1 == "+" or op1 == "-") and (op2 == '+' or op2 == "-"):
            return True
        if (op1 == "*" or op1 == "/") and (op2 == '*' or op2 == '/'):
            return True
        if (op1 == "*" or op1 == "/") and (op2 == '+' or op2 == "-"):
            return True
        return False
