# LeetCode 241. Different Ways to Add Parentheses

## Description

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2\*3-4\*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2\*(3-(4\*5))) = -34 
((2\*3)-(4\*5)) = -14 
((2\*(3-4))\*5) = -10 
(2\*((3-4)\*5)) = -10 
(((2\*3)-4)\*5) = 10

## 描述

给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

示例 1:

输入: "2-1-1"
输出: [0, 2]
解释: 
((2-1)-1) = 0 
(2-(1-1)) = 2
示例 2:

输入: "2\*3-4\*5"
输出: [-34, -14, -10, -10, 10]
解释: 
(2\*(3-(4\*5))) = -34 
((2\*3)-(4\*5)) = -14 
((2\*(3-4))\*5) = -10 
(2\*((3-4)\*5)) = -10 
(((2\*3)-4)\*5) = 10

### 思路

* 这道题使用递归求解.
* 以每一个操作符为分割点，我们将给定的字符串分割成两个字串，假设我们递归求解得到了左边的所有组合结果left，右边的所有组合right，我们以当前符号为分隔符，把left和right中的所有数用当前运算符做运算，得到最终结果.
* 递归终止条件，输入的字符串只包含一个数字.

```python
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
        # 有记录的递归，如果当前求解的字符串已经求解过了，我们直接返回结果.
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
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-02-241-Different-Ways-to-Add-Parentheses.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-241-different-ways-to-add-parentheses/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
