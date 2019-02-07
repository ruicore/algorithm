# LeetCode 282. Expression Add Operators

## Description
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []

## 描述

给定一个仅包含数字 0-9 的字符串和一个目标值，在数字之间添加二元运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。

示例 1:

输入: num = "123", target = 6
输出: ["1+2+3", "1*2*3"] 
示例 2:

输入: num = "232", target = 8
输出: ["2*3+2", "2+3*2"]
示例 3:

输入: num = "105", target = 5
输出: ["1*0+5","10-5"]
示例 4:

输入: num = "00", target = 0
输出: ["0+0", "0-0", "0*0"]
示例 5:

输入: num = "3456237490", target = 9191
输出: []

### 思路

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-07 09:14:58
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-07 13:31:18


class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':
        res = []
        expression = [0] * (2 * len(num) - 1)
        self.__dfs(num, target, 0, expression, 0, 0, 0, res)
        return res

    def __dfs(self, num, target, start, exp, vaild, prev, curr, res):
        if start == len(num):
            if curr == target:
                res.append("".join(exp[0:vaild]))
                return
        n = 0
        s = start
        l = vaild
        if s: vaild += 1
        while start < len(num):
            n = n * 10 + (ord(num[start]) - ord('0'))
            if num[s] == "0" and start - s > 0: break
            exp[vaild] = num[start]
            vaild += 1
            start += 1
            if s == 0:
                self.__dfs(num, target, start, exp, vaild, n, n, res)
                continue
            exp[l] = "+"
            self.__dfs(num, target, start, exp, vaild, n, curr + n, res)
            exp[l] = "-"
            self.__dfs(num, target, start, exp, vaild, -n, curr - n, res)
            exp[l] = "*"
            self.__dfs(num, target, start, exp, vaild, prev * n,curr - prev + prev * n, res)


if __name__ == "__main__":
    so = Solution()
    res = so.addOperators("179898705", 6565)
    print(res)
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-07-282-Expression-Add-Operators.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-282-expression-add-operators/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
