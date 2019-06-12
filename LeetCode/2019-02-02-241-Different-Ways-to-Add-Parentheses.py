# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-02 15:19:33
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-02 16:51:16


class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        sovled = {}
        _input = input
        return list(self.__recursion(sovled, _input))

    def __recursion(self, sovled, _input):
        if _input in sovled: return sovled[_input]
        patial, num = [], 0
        for i in range(len(_input)):
            # 从字符串中取出数字
            if _input[i].isdigit():
                num = num * 10 + int(_input[i])
            # 如果当前位置是符号
            elif _input[i] == '+' or _input[i] == "-" or _input[i] == '*':
                # 以当前位置为分隔
                # 递归求解当前位置左边字符串的解
                left = self.__recursion(sovled, _input[0:i])
                # 递归求解当前位置右边字符串的解
                right = self.__recursion(sovled, _input[i + 1:])
                # 将当前位置左边的解和右边的解用当前的符号进行组合
                for x in left:
                    for y in right:
                        patial.append(self.__cal(_input[i], x, y))
                num = 0
        if not patial: patial.append(num)
        sovled[_input] = patial
        # 返回当前的解
        return patial

    def __cal(self, operator, num1, num2):
        # 题目给定只有三个运算符    
        if operator == "+": return num1 + num2
        if operator == "-": return num1 - num2
        if operator == "*": return num1 * num2