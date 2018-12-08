# LeetCode 44. Wildcard Matching

## Description

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

python
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the **entire** input string (not partial).

**Note:**

* s could be empty and contains only lowercase letters a-z.
* p could be empty and contains only lowercase letters a-z, and characters like ? or *.

**Example 1:**

Input: s = "aa" p = "a" Output: false
Explanation: "a" does not match the entire string "aa".

**Example 2:**

Input: s = "aa" p = "*" Output: true
Explanation: '*' matches any sequence.

**Example 3:**

Input: s = "cb" p = "?a" Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

**Example 4:**

Input: s = "adceb" p = "\*a\*b" Output: true
Explanation: The first '\*' matches the empty sequence, while the second '\*' matches the substring "dce".

**Example 5:**

Input: s = "acdcb" p = "a\*c?b" Output: false

## 描述

给定输入字符串s和模式串(p)，实现通配符模式匹配支持'?' 和'\*'.

### 思路

* 根据题意?应当和任意一个字符匹配，即?需要**匹配且仅匹配**一个字符，\*可以匹配任意种类字符，任意长度字符，也可以不匹配.
* 这里的难点在于不清楚\*应该匹配多少个字符，匹配过多或者过少都可能倒是后面的匹配失效.
* 我们使用四个变量indexs,indexp,matcheds,star,其中indexs用来记录s的索引，indexp用来记录模式串p的索引.
* 如果字符串s[indexs]和模式串p[indexp]相等,或者模式串p[indexp]为?时，我们让indexs和indexp自增一位.
* 如果字符串s[indexs]和模式串p[indexp]不等，且模式串p[indexp]是\*时，我们让star记录下此时\*的位置，matcheds记录下此时s[indexs]的位置.
* 表示p中索引star的\*可能需要与字符串s中索引为matched的字符匹配，然后我们置indexp为star+1,indexs保持不变.
* 如果遇到了s中既不和p中字符相等，且p中的字符不为?和\*,我们检查p前面是否有\*.
* 如果存在\*，则我们让matched自增一个，表示原来的假设成立，即\*需要和matched自增前表示的字符匹配，matched自增表示\*可能需要与当前的字符匹配.
* 如果没有\*，说没匹配不成功，直接返回False
* 遍历完之后，检查p字符串，如果还有剩余：检查剩余的是否全是*，若全是\*返回True，否则返回False

```python
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 首先获取字符串s和模式串p的长度
        lens, lenp = len(s), len(p)
        indexp, indexs, indexstar, matcheds = 0, 0, -1, 0
        # 循环条件，还没有遍历到s尾部时才继续执行
        while indexs < lens:
            # 当p还没有到达尾部，且s和p对应位置字符相等或p位置字符为?号时
            if indexp < lenp and (s[indexs] == p[indexp] or p[indexp] == '?'):
                # 同时自增，表示相等
                indexs += 1
                indexp += 1
            # 当p还没有到达尾部且s和p对应位置不相等，且p为*号
            elif indexp < lenp and p[indexp] == "*":
                # 记下此时*号的位置
                indexstar = indexp
                # 记下此时*号对应匹配的s中字符的位置，此时还不确定*号是否需要和此字符匹配
                matcheds = indexs
                # 继续匹配
                indexp += 1
            # 当s和p对应位置不等，且p位置不为*，检查前面是否有*号
            elif indexstar != -1:
                # 如果有，则说明前面的*号需要匹配一个字符，matcheds自增一个，indexp指向后面一个，indexs重新开始于matcheds
                matcheds += 1
                indexp = indexstar+1
                indexs = matcheds
            # 如果以上条件都不满足（即不满足s和p对应位置相等，且不满不p前面位置有8号）
            else:
                # 查找失败，返回False
                return False
        # 如果在s遍历完成之后，p还有剩余，则检查p剩余的内容
        while indexp < lenp:
            # 只要p中剩余的内容有一个不是*，返回False
            if p[indexp] != '*':
                return False
            indexp += 1
        return True
```

©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-44-wildcard-matching/)，欢迎转载，转载需保留文章来源，作者信息和本声明.