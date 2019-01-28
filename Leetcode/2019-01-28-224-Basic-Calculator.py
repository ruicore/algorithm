# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-28 20:18:35
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-28 22:52:23


class Solution(object):
    def calculate(self, s):
        num = 0
        sign = 1
        stack = []
        total = 0

        for item in s:
            # 获取一个完整的整数
            if item.isdigit():
                num = num * 10 + ord(item) - ord("0")
            # 如果是加号，把目前获取的结果加到最终结果中
            # 下一个数字前面的符号是加号
            elif item == "+":
                total += sign * num
                sign = 1
                num = 0
            # 如果是减号，把目前获取的结果加到最终结果中
            # 下一个数字前面的符号是减号
            elif item == "-":
                total += sign * num
                sign = -1
                num = 0
            # 如果是左括号，将左括号前面所得的结果和sign(表示括号内的值所带的符号)压入栈内
            elif item == "(":
                stack.append((total, sign))
                sign = 1
                # 将total重置为0，接下来将计算括号内的值
                total = 0
                num = 0
            # 如果是右括号，计算括号内的值
            elif item == ")":
                # 括号内的值
                total += sign * num
                # 括号前面已经计算的值
                pretoatal, presign = stack.pop()
                total = pretoatal + presign * total
                num = 0
        # 将最后剩下的值加到最终结果之中
        if num:
            total += num * sign
        return total
