# LeetCode 433. Minimum Genetic Mutation

## Description

A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
 
```py

Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
 

Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
 

Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3
```

## 描述

一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。

假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。

例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。

与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。

现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。

注意:

起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
所有的目标基因序列必须是合法的。
假定起始基因序列与目标基因序列是不一样的。

```py
示例 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

返回值: 1
示例 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

返回值: 2
示例 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

返回值: 3
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-genetic-mutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 使用广度优先遍历，初始字符串为第一层，与初始字符串相差一个字符的字符串为下一层的字符串。
* 遍历寻找字符串，直到找到最重的字符串或者队列为空。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2020-01-30 11:43:15
# @Last Modified by:   何睿
# @Last Modified time: 2020-01-30 12:11:17

import collections
from typing import List


class Solution:
    def _valid_next(self, current: str, next_: str):
        # 判断两个长度相等的字符串，对应位置是否只有 1 个字符不同
        return sum(1 for c, n in zip(current, next_) if c != n) == 1

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = collections.deque()
        queue.append([start, '', 0])

        while queue:
            # 当前字符串，当前字符串的前一个字符串，steps
            current, previous, steps = queue.popleft()
            # 当前字符等于目标字符
            if current == end:
                return steps
            # 找到和 current 字符相差一个字符的字符，并且此字符不能和 current 的上一个字符相等
            for item in bank:
                if item != previous and self._valid_next(current, item):
                    queue.append([item, current, steps + 1])

        return -1
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2020-01-30-433-Minimum-Genetic-Mutation.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-433-minimum-genetic-mutation/) ，作者信息和本声明.
