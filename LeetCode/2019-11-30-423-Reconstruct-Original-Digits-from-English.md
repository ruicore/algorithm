# LeetCode 423. Reconstruct Original Digits from English

## Description

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:

Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.

Example 1:
```py
Input: "owoztneoer"

Output: "012"
```

Example 2:
```py
Input: "fviefuro"

Output: "45"
```
## 描述

给定一个非空字符串，其中包含字母顺序打乱的英文单词表示的数字0-9。按升序输出原始的数字。

注意:

输入只包含小写英文字母。
输入保证合法并可以转换为原始的数字，这意味着像 "abc" 或 "zerone" 的输入是不允许的。
输入字符串的长度小于 50,000。
示例 1:

```py
输入: "owoztneoer"

输出: "012" (zeroonetwo)
```

示例 2:
```py
输入: "fviefuro"

输出: "45" (fourfiv
```
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reconstruct-original-digits-from-english
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 这道题考数学，考观察，没有考察到什么算法。
* 'z' 只出现在 zero 中，因此 z 唯一确定 0 的个数；
* 同理，w，u，x，g 分别只出现在 two，four，six，eight 中，因此唯一确定 2，4，6，8.
* o 出现在 zero，two，four，one 中，由于 0，2，4 已经被确定，因此 1 可以被确定；
* h 出现在 three ，eight 中，8 已经被确定，因此 3 可以被确定；
* s 出现在 six，seven 中，由于 6 已经被确定，因此 7 可以被确定；
* i 出现在 five，six，eight，nine 中，由于 5，6，8 已经被确定，因此 9 可以被确定。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-11-30 13:15:30
# @Last Modified by:   何睿
# @Last Modified time: 2019-11-30 13:28:08

from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        res = {}
        count = Counter(s)
        for key, char in zip([0, 2, 4, 6, 8], ['z', 'w', 'u', 'x', 'g']):
            res[key] = count.get(char, 0)
        res[1] = count.get('o', 0) - res[0] - res[2] - res[4]
        res[3] = count.get('h', 0) - res[8]
        res[5] = count.get("f", 0) - res[4]
        res[7] = count.get('s', 0) - res[6]
        res[9] = count.get('i', 0) - res[5] - res[6] - res[8] 

        return ''.join(str(num) * res[num] for num in range(0, 10))
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-11-30-423-Reconstruct-Original-Digits-from-English.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-423-reconstruct-original-digits-from-english/) ，作者信息和本声明.
