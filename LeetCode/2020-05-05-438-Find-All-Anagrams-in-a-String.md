# LeetCode 438. Find All Anagrams in a String

## Description

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

```py
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

Example 2:

```py
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

### 思路

* 第一种思路比较简单直接，我们用 p 字符串中的字符构造一个字典，键为字符，值为每个字符在 p 中出现的次数，记这个字典为 p_dict;
* 我们用 s 字符串的前 len(p) 个字符构建一个字典，同样的，键为字符，值为每个字符在 s[0:len(p)] 中出现的次数,记这个字典为 tmp_dict；
* 我们比较这两个字典是否相等，若相等，说明 s[0:len(p)] 满足题意，在结果数组中记下 0 的位置；
* 我们更新 tmp_dict，通过减少 tmp_dict 中 s[i] 元素，增加 s[i+len(p)] 的方式更新 ；
* 继续比较 tmp_dict 和 p_dict 是否相等；

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2020-05-05 15:29:17
# @Last Modified by:   何睿
# @Last Modified time: 2020-05-05 20:08:00

from typing import List
from copy import deepcopy
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if not s or not p:
            return []

        p_dict = defaultdict(int)
        tmp_dict = defaultdict(int)
        for char in p:
            p_dict[char] += 1

        for char in s[:len(p)]:
            tmp_dict[char] += 1

        res = []

        for i in range(0, len(s) - len(p)):
            if tmp_dict == p_dict:
                res.append(i)

            tmp_dict[s[i]] -= 1
            if tmp_dict[s[i]] == 0:
                tmp_dict.pop(s[i])
            tmp_dict[s[i + len(p)]] += 1

        if tmp_dict == p_dict:
            res.append(len(s) - len(p))
        return res

```

* 还有另外一种方式，记录 p 中所有字符的 cnt，遍历 s 中的字符，不断的减小 cnt 的值，当 cnt 的值为 0 时，说明找到了一个满足题意的解；
* 同样的，我们用字符串 p 中的字符构造一个字典，键为字符，值为每个字符在 p 中出现的次数，记这个字典为 p_dict，键为 key，值为 value;这个字典的含义为：要形成字符串 p 的 Anagram，还需要字符 key 各 value 个；
* 如  p = "aavc"，则 p_dict = {"a":2,"v":1,"c":1}，表示需要形成字符串 "aavc" 的 Anagram ，还需要 a 字符 2 个，v 字符 1 个，c 字符 1个；
* 我们用两个指针 left，right，从左向右遍历；
* 记字符 s[right] 为 t，让 p_dict[t] -1，表示「要形成字符 p，对字符 t 的需要减少 1」；此时检查 p_dict[t] 是否大于 0，若大于零，则 cnt -1；
* 检查 cnt 是否等于 0，若为零，表示 s 中 left 到 right 的字符，可以形成 p；
* 当 right - left 包含的字符个数等于 p 时,需要将 left 向右边移动；
* 此时 p_dict[s[left]] 自增 1，如果 p_dict[s[left]] 大于等于零，则 cnt + 1；
* 如果 p_dict[s[left]] 小于 0，说明在字符 p 中没有字符 s[left]

```py
from typing import List
from copy import deepcopy
from collections import defaultdict


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:

        if not s or not p:
            return []

        p_dict = defaultdict(int)
        for char in p:
            p_dict[char] += 1

        left, right, cnt = 0, 0, len(p)
        res = []

        while right < len(s):
            p_dict[s[right]] -= 1

            if p_dict[s[right]] >= 0:
                cnt -= 1
            if cnt == 0:
                res.append(left)
            if right - left + 1 == len(p):
                if p_dict[s[left]] >= 0: # 大于零，说明 p 中有字符 s[left]，否则 p 中没有 s[left]
                    cnt += 1
                p_dict[s[left]] += 1
                left += 1

            right += 1

        return res

```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2020-05-05-438-Find-All-Anagrams-in-a-String.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-438-find-all-anagrams-in-a-string/) ，作者信息和本声明.
