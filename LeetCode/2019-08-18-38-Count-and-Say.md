# LeetCode 38. Count and Say

## Description

The count-and-say sequence is the sequence of integers with the first five terms as following:

```py
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
```

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

```py
Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
```

## 描述

报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

```py
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
```

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

示例 1:

```py
输入: 1
输出: "1"
示例 2:
```

```py
输入: 4
输出: "1211"
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-and-say
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* itertools 的 groupby 模块能够对可迭代对象进行统计。
* 利用 groupby 统计结果，并形成新的字符串；然后再对新的字符串进行统计；一次循环 n - 1 次即可。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-18 09:49:01
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-18 09:51:29

from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        for _ in range(n - 1):
            result = ''.join([str(len(list(g))) + key for key, g in groupby(result)])

        return result
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-08-18-38-Count-and-Say.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-38-count-and-say/) ，作者信息和本声明.
