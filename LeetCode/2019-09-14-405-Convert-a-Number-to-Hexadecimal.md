# LeetCode 405. Convert a Number to Hexadecimal

## Description

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

```py
Input:
26

Output:
"1a"
```

Example 2:

```py
Input:
-1

Output:
"ffffffff"
```

## 描述

给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

注意:

十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
示例 1：

```py
输入:
26

输出:
"1a"
```

示例 2：

```py
输入:
-1

输出:
"ffffffff"
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 将负数转换为补码：我们知道对于一个负数 -a（a>0）,其补码为 a 的二进制表示按位取反，然后加一；为什要这么做？因为要使得负数的二进制表示与这个负数绝对值的二进制表示加和为 0；比如 0b1，将最高位置为 1，按位取反后（假设只有 8 位）为 0b11111110，此时把这辆个数加起来为 0b1111111，此时这个数再加上 1，就可以变成 0，于是负数的补码是，此数绝对值的二进制的反码 + 1;
* 为了求的一个数 num （num < 0）的补码，我们记要求的补码为 x，则有 x + （-num） = 0，于是 x = 0 - num，在 32 位表示中，0 为 0xffffffff + 1，
* 将负数转换成为补码后，对 16 取模，记下余数；如此循环，直到商为 0；

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-09-14 10:47:02
# @Last Modified by:   何睿
# @Last Modified time: 2019-09-14 11:07:11


class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num = 0xffffffff + 1 + num

        transfer = "0123456789abcdef"
        res = []
        while num:
            res.append(transfer[num % 16])
            num >>= 4

        return ''.join(reversed(res)) or '0'

```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-09-14-405-Convert-a-Number-to-Hexadecimal.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-405-convert-a-number-to-hexadecimal/) ，作者信息和本声明.
