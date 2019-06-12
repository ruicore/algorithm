# LeetCode 227. Basic Calculator II

## Description

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.

## 描述

实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

### 思路

* 我们使用两个栈来实现表达式求值.
* 其中一个用来存储数字，另一个来存储符号.
* 我们从给定的字符串中不断的取出数字和符号，若是数字，我们将其压入数字栈，如果是符号，我们和当前栈顶的符号进行比较，如果当前符号的优先级小于等于栈顶元素的符号，我们弹出符号栈顶元素，并用此符号对数字栈栈顶的两个元素进行运算，并将运算的结果重新压入数字栈，直到当前符号大于符号栈栈顶元素或者符号栈为空.

```python
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
                    # 如果当前操作符优先级小于等于符号栈栈顶操作符，我们持续进行运算
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
        # op2的优先级>=op1的优先级返回True
        # 否则返回False
        if (op1 == "+" or op1 == "-") and (op2 == '+' or op2 == "-"):
            return True
        if (op1 == "*" or op1 == "/") and (op2 == '*' or op2 == '/'):
            return True
        if (op1 == "*" or op1 == "/") and (op2 == '+' or op2 == "-"):
            return True
        return False
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-28-227-Basic-Calculator-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-27-basic-calculator-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
