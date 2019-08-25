# LeetCode 394. Decode String

## Description

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

```py
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
s = "leetcode",return "leetcode".
```

## 描述

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

```py
s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 使用栈,一个作为数字栈，用于存储数字，一个作为字符栈，用于存储字符；
* 如果遇到了数字，提取数字；
* 如果遇到 ‘[’ ，将数字压入栈，同时也将 ‘[’ 押入栈；
* 如果遇到 ‘]’ ，将栈中的字符从栈中压出，直到遇到了‘[’ ，将被压出的所有字符乘以数字栈中的最后一个字符，并压回栈。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-25 09:19:03
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-25 10:17:59


class Solution:
    def decodeString(self, s: str) -> str:
        num, chr_stack, num_stack = 0, [], []
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                num_stack.append(num)
                chr_stack.append("[")
                num = 0
            elif char == ']':
                tmp = []
                while chr_stack and chr_stack[-1] != '[':
                    tmp.append(chr_stack.pop())
                chr_stack.pop()
                chr_stack.extend(reversed(tmp * num_stack.pop()))
            else:
                chr_stack.append(char)

        return "".join(chr_stack)

```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-08-25-394-Decode-String.py) 。
©本文是原创文章，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-394-decode-string/) ，作者信息和本声明.
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-394-decode-string/) ，作者信息和本声明.
