# LeetCode 224. Basic Calculator

## Description

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

## 描述

实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

示例 1:

输入: "1 + 1"
输出: 2
示例 2:

输入: " 2-1 + 2 "
输出: 3
示例 3:

输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23

### 实现

* 使用栈对加法进行模拟.

```python
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
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-28-224-Basic-Calculator.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-224-basic-calculator/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
