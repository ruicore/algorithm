# LeetCode 395. Longest Substring with At Least K Repeating Characters

## Description

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

```py
Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
```

Example 2:

```py
Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
```

## 描述

找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。

示例 1:

```py
输入:
s = "aaabb", k = 3

输出:
3

最长子串为 "aaa" ，其中 'a' 重复了 3 次。
```

示例 2:

```py
输入:
s = "ababbc", k = 2

输出:
5

最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```
### 思路

* 统计每个字符出现的次数，用次数少于 k 的字符对原字符串进行拆分。递归地对字符串进行同样的操作。
* 在字符串中出现次数少于 k 的字符，一定不能在最长字符串里面，所以用此字符串对原字符串进行切割。如果所有的字符串出现的此处都大于 k，则返回字符串的长度。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-27 21:07:09
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-28 08:40:37

from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        for key, v in Counter(s).items():
            if v < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(key))
        return len(s)
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-08-27-395-Longest-Substring-with-At-Least-K-Repeating-Characters.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/395-longest-substring-with-at-least-k-repeating-characters/) ，作者信息和本声明.
