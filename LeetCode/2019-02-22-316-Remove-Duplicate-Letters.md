# LeetCode 316. Remove Duplicate Letters

## Description

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

```py
Input: "bcabc"
Output: "abc"
```

Example 2:

```py
Input: "cbacdcbc"
Output: "acdb"
```

## 描述

给定一个仅包含小写字母的字符串，去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1:

```py
输入: "bcabc"
输出: "abc"
```

示例 2:

```py
输入: "cbacdcbc"
输出: "acdb"
```

### 思路

* 字典序最小：对于两个字符串 S 和 T，如果 S1 < T1，则 字符串 S 的字典序更小。比如第一个例子字符串 “bcabc” 去掉重复后可能的结果有：
* 1.bca 2. bac 3. cab 4.abc 「注意只能从前往后遍历取出字符」。
* 对于 1 和 2，由于 b == b,c > a，所以 2 的字典序比1小，同理 2 的字典序比 3 小，4 的字典序比 2 小，所以最终答案是 4。
* 我们使用 stack 和 字典这两种数据结构。
* 我们用一个字典记录每个字符出现的次数。
* 核心思路是：假设 stack 中记录了给定的 S 中前 i 个字符的结果，那么针对第 i+1 个字符，如果第 i+1 个字符还没有出现在 stack 中，如果：
* 1.第 i+1 个字符比栈顶元素小并且栈顶元素在第 i+1 个元素之后还会出现，那么 第 i+1 个元素应该在 stack 栈顶元素的前面，于是我们弹出 stack 栈顶元素，并用第 i+1 个元素和现在的栈顶元素比较，如果此时第 i+1 个元素仍比栈顶元素小并且此时的栈顶元素在第 i+1 个元素之后仍会出现，我们继续弹出栈顶元素 ...
* 2.第 i+1 个字符比栈顶元素小但是栈顶元素在这之后不会出现了，我们把当前元素追加到栈顶。
* 3.如果当前元素本身就比栈顶元素大，我们把当前元素追加到栈顶。
* 如上，我们需要知道一个元素在之后会不会出现：我们借助字典来实现，字典的键为字符，值为字符在给定的字符串中出现的次数，如果一个字符对应的值大于零，说明这个字符还会出现，如果等于零则不会出现。
* 每次访问一个字符的时候，我们首先让字典中该字符对应的值自减一次，表示已经访问了一次。
* 我们还需要知道一个字符是否已经出现过了在 stack 中，也就是有没有被处理过，我们用 Hastset 来实现，每访问到一个字符，我们都把它加入到 set 中，在第 1 种情况种，如果一个元素从栈顶被弹出了，我们也从 set 中移除这个元素，表示这个元素还没有被处理。
 
```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-22 14:27:31
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-22 15:38:39

import collections


class Solution: 
    def removeDuplicateLetters(self, s: 'str') -> 'str':
        # stack 用于存储已经获取的结果
        # visited 表示当前的字符已经遍历过
        stack, visited = [], set()
        # times 是一个字典，键为字符，值为字符出现过的次数
        times = collections.Counter(s)
        for item in s:
            # 让字典 times 中记录的对应次数减少一次
            times[item] -= 1
            # 如果 item 还没有遍历过，即 item 没有出现在结果中
            # visited 和 stack 里面的字符内容是一样的
            # 只不过我们用stack 是为了从栈顶开始删除
            # 用 visited 可以在 O(1) 时间复杂度内判断一个元素是否被遍历过
            # 并且在 O(1) 内删除一个元素
            if item not in visited:
                # 如果当前元素比栈顶元素小并且栈顶元素在当前元素后面还会出现
                # 那么当前元素应该带栈顶元素的前面
                # 我们弹出栈顶元素，在 visited 中删除栈顶元素的记录
                while stack and item < stack[-1] and times[stack[-1]] != 0:
                    visited.remove(stack.pop())
                # 此时有下列三种情况
                # 1. 栈已经空了 
                # 2. 当前元素大于栈顶元素 
                # 3. 当前元素小于栈顶元素但是栈顶元素在当前元素后面不再出现
                # 我们将当前元素压入栈顶，在 visited 元组中记录当前元素已经被访问过
                stack.append(item)
                visited.add(item)
        # 注意题目要求返回字符串
        return ''.join(stack)
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-22-316-Remove-Duplicate-Letters.py)。
©本文首发于 [何睿的博客](https://www.ruicore.cn/leetcode-316-remove-duplicate-letters/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
