# LeetCode 393. UTF-8 Validation

## Description

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

```py
   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
```

Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.

## 描述

UTF-8 中的一个字符可能的长度为 1 到 4 字节，遵循以下的规则：

对于 1 字节的字符，字节的第一位设为0，后面7位为这个符号的unicode码。
对于 n 字节的字符 (n > 1)，第一个字节的前 n 位都设为1，第 n+1 位设为0，后面字节的前两位一律设为10。剩下的没有提及的二进制位，全部为这个符号的unicode码。
这是 UTF-8 编码的工作方式：

```py
   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
```
给定一个表示数据的整数数组，返回它是否为有效的 utf-8 编码。

注意:
输入是整数数组。只有每个整数的最低 8 个有效位用来存储数据。这意味着每个整数只表示 1 字节的数据。

示例 1:

data = [197, 130, 1], 表示 8 位的序列: 11000101 10000010 00000001.

返回 true 。
这是有效的 utf-8 编码，为一个2字节字符，跟着一个1字节字符。
示例 2:

data = [235, 140, 4], 表示 8 位的序列: 11101011 10001100 00000100.

返回 false 。
前 3 位都是 1 ，第 4 位为 0 表示它是一个3字节字符。
下一个字节是开头为 10 的延续字节，这是正确的。
但第二个延续字节不以 10 开头，所以是不符合规则的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/utf-8-validation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 根据条件判断。
* 1. 如果是 0 开头，表示一个单独的码；2. 如果是 110 开头，则表示后面跟着一个 10 开头的八位字节码；3. 如果是 1110 开头，表示后面跟着两个 10 开头的八位字节码；4. 如果是 11110 开头，表示后面跟着 3 个 10 开头的字节码；
* 所以我们需要判断的是 1. 数字以二进制表示的第一个 0 前面 1 的个数；2. 以 10 开头的个数；
* 我们将数字用二进制表示，然后转换成为字符串，用正则进行匹配。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-24 10:55:33
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-24 11:59:50


import re
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        next_ = 0
        pattern = re.compile("0b(.*?)0.*") # 匹配第一个 0 前面 1 的个数
        while next_ != -1 and next_ < len(data):
            next_ = self.__check(next_, data, pattern)

        return False if next_ == -1 else True

    def __check(self, start, data, pattern):

        num = data[start]
        if not num & 0b10000000: # 以 0 开头
            return start + 1
        elif num & 0b11000000 == 0b10000000: # 以 10 开头
            return -1
        else:
            match = pattern.match(str(bin(num))) # 正则匹配
            if not match: # 如果匹配失败，返回 -1 
                return -1
            length = match.span(1)[1] - match.span(1)[0] # 后面应该跟 10 开头的数的个数
            end = start + length  # 当前位置向后移动 length 个位置
            if length > 4 or end > len(data): # 如果个数大于4，如果向后挪动 length 个位置后越界
                return -1 
            if all(map(lambda i: data[i] & 0b11000000 == 0b10000000, range(start + 1, end))): # 范围内的数子都需要以 10 开头
                return start + length
            return -1
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-08-24-393-UTF-8-Validation.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-393-utf-8-validation/) ，作者信息和本声明.
