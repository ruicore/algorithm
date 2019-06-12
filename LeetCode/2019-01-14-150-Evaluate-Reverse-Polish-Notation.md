# LeetCode 150. Evaluate Reverse Polish Notation

## Description

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

```python
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

Example 2:

```python
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

Example 3:

```python
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

## 描述

根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

### 思路

* 使用两个栈来实现逆[波兰表达式](https://zh.wikipedia.org/zh-hans/%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E7%A4%BA%E6%B3%95).
* 先将表达式中的所有元素压入到栈1，接下来我们pop出栈，如果是数字则压入栈2，如果是符号我们从栈2中弹出两个数组，用刚才的符号对其进行操作，再将操作的结果压入栈2.最后的结果是栈2中剩下的一个元素.

```python
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
            # 这里可以不用做判断，题目保证了除数不会是0
            return int(num2 / num1) if num1 != 0 else 0
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-14-150-Evaluate-Reverse-Polish-Notation.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-150-evaluate-reverse-polish-notation/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
