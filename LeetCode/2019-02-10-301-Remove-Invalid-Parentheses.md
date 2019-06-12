# LeetCode 301. Remove Invalid Parentheses

## Description

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

```py
Input: "()())()"
Output: ["()()()", "(())()"]
```
Example 2:

```py
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
```

Example 3:

```py
Input: ")("
Output: [""]
```

## 描述

删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

```py
输入: "()())()"
输出: ["()()()", "(())()"]
```

示例 2:

```py
输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
```

示例 3:

```py
输入: ")("
输出: [""]
```

### 思路

* 深度优先搜索.
* 对于一个合法括号，在任意一个不是最后的位置，当前位置（包括）前面的左括号个数一定是大于等于右括号个数，此为我们判断一个字符串是否是合法字符串的条件.
* 我们首先获取需要去掉多少个左括号和去掉多少个右括号，然后我我们使用深度优先搜索，递归的先去左括号，再去右括号.

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-10 15:47:49
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-10 17:57:38


class Solution:
    def removeInvalidParentheses(self, s: 'str') -> 'List[str]':
        # 如果为空，返回空字符串
        if not s: return [""]
        # 统计非法的左右括号的个数
        left, right = 0, 0
        for _s in s:
            # 如果是左括号，left自增一次
            if _s == "(": left += 1
            # 如果没有非法的左括号，并且当前是右括号，right自增一次
            if left == 0 and _s == ")":
                right += 1
            # 否则如果当前是右括号，我们让当前的右括号和一个左括号匹配
            # left自减一次
            elif _s == ")":
                left -= 1
        res = []
        self.__dfs(s, 0, left, right, res)
        return res

    def __dfs(self, s, start, left, right, res):
        # 递归结束条件
        if not left and not right and self.__valid(s):
            res.append(s)
            return
        for i in range(start, len(s)):
            # 避免重复
            if i != start and s[i] == s[i - 1]: continue
            if s[i] == "(" or s[i] == ")":
                # 删除字符
                current = s[0:i] + s[i + 1:]
                # 先删除右括号
                if right > 0: self.__dfs(current, i, left, right - 1, res)
                # 再删除左括号
                elif left > 0: self.__dfs(current, i, left - 1, right, res)

        return

    def __valid(self, s):
        # 统计有效的括号个数
        # 只要不到最后一个位置，左括号个数一定大于右括号的个数
        # 最后一个位置左右括号的个数相等
        count = 0
        for _s in s:
            # 遇到左括号，count加一
            if _s == "(": count += 1
            # 遇到右括号，count减一
            if _s == ")": count -= 1
            # 如果count小于0，说明当前位置一定没有足够的左括号
            # 和右括号进行匹配，返回False
            if count < 0: return False
        return count == 0
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-10-301-Remove-Invalid-Parentheses.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-301-remove-invalid-parentheses/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
