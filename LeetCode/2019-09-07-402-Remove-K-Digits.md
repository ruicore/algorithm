# LeetCode 402. Remove K Digits

## Description

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:

```py
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
```

Example 2:

```py
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
```

Example 3:

```py
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
```

## 描述

给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:

num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。

示例 1 :

```py
输入: num = "1432219", k = 3
输出: "1219"
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
```

示例 2 :

```py
输入: num = "10200", k = 1
输出: "200"
解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
```

示例 3 :

```py
输入: num = "10", k = 2
输出: "0"
解释: 从原数字移除所有的数字，剩余为空就是0。
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-k-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 使用栈，需要指明的是，在字符形式下，依然有 "1" < "2" ... < "9".
* 我们依次把数字（字符格式）压入栈中；每次压入的时候都和栈顶的数做比较，如果栈顶的数比较大，就把栈顶的数 pop 出来（循环检查），直到要压入栈的数小于等于栈顶的数；统计从栈中 pop 出数的个数 cnt，如果cnt 超过了给定的 k；则不再比较，直接压入栈中；
* 如果当前要压入的数为 "0"，并且栈为空，那么跳过次数，不压入栈中；

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-09-07 07:59:40
# @Last Modified by:   何睿
# @Last Modified time: 2019-09-07 09:10:06


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        cnt, stack = 0, []
        for n in num:
            while cnt < k and stack and n < stack[-1]:
                cnt += 1
                stack.pop()
            if n == "0" and not stack:
                continue
            stack.append(n)

        return "".join(stack[0:len(stack) - (k - cnt)]) or "0"
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-09-07-402-Remove-K-Digits.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-402-remove-k-digits/) ，作者信息和本声明.
