# LeetCode 424. Longest Repeating Character Replacement

## Description

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:
```py
Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
```

Example 2:

```py
Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```
## 描述

给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意:
字符串长度 和 k 不会超过 104。

示例 1:
```py
输入:
s = "ABAB", k = 2

输出:
4

解释:
用两个'A'替换为两个'B',反之亦然。
```
示例 2:

```py
输入:
s = "AABABBA", k = 1

输出:
4

解释:
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。
```
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-repeating-character-replacement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 这道题是使用 **滑动窗口** 的一道比较典型的题目。
* 维护一个滑动窗口，并维护一个字典，统计这个窗口内每个字符出现的次数。
* 记窗口的左右边界为 left，right。记窗口里出现最多次的字符为 Same，记 Same 出现的次数为 max_repeat_count。
* 主要思路是，向窗口内不断添加字符，并将与 Same （出现最多次）不同的字符，变成 Same，只要当前需要变换的次数小于等于 k，当前就是一个有效的窗口。
* 移动右边界的条件：窗口内与 Same 不同的字符小于等于 k 时，说明还有变换操作可以用，此时可以继续移动 right；
* 移动左边界的条件：窗口内与 Same 不同的字符大于 k 时，说明为了使得窗口内的字符都等于 Same，k 次操作已经不够用了，此时应当移动 left

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-11-30 16:32:47
# @Last Modified by:   何睿
# @Last Modified time: 2019-11-30 16:44:05

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_count = defaultdict(int) # 统计窗口内每个字符出现过的次数
        res, left, right, count_s = 0, 0, 0, len(s)

        max_repeat_count = 0 # 窗口内出现最多次字符的次数
        while right < count_s:
            window_count[s[right]] += 1 # 次数加一
            # 由于窗口只有 s[right] 增加了一次，那么 出现最多次字符的次数 只需要和这个字符的字符比较就可以了
            max_repeat_count = max(max_repeat_count, window_count[s[right]]) # 更新出现最多次字符的次数

            while right - left + 1 - max_repeat_count > k: # left 向边移动
                window_count[s[left]] -= 1 
                max_repeat_count = max(max_repeat_count, window_count[s[left]])
                left += 1

            res = max(res, right - left + 1) # 窗口内的单词个数
            right += 1

        return res

```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-11-30-424-Longest-Repeating-Character-Replacement.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-424-longest-repeating-character-replacement/) ，作者信息和本声明.
