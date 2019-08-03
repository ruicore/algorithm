# LeetCode 387. First Unique Character in a String

## Description

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

```py
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
```

## 描述

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

```py
s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
```
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

1. 看到这道题的第一个思路是利用字典，首先统计字符串 s 中每个字符出现的次数，然后顺序遍历 s，返回第一个计数为 1 的字符，但是这样提交后发现时间消耗很大。代码如下：

```py
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = -1
        count = Counter(s)
        for i,c in enumerate(s):
            if count[c]==1:
                res = i
                break

        return res
```
2. 另外一种高效的方法是：由于字母一共只有 26 个，所以最后的结果一定是这 26 个字母中的一个；于是我们依次检查这个 26 个字母在字符串中出现的次数，返回只出现了一次，并且顺序第一的字母的索引。

```py
class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = len(s)
        for char in 'abcdefghijklmnopqrstuvwxyz':
            # 从左右两边找 char 出现的位置，如果 char 在 s 中仅仅出现一次；
            # 那么 left 和 right 一定相等；
            left, right = s.find(char), s.rfind(char)
            if left != -1 and left == right:
                res = min(res, left)

        return -1 if res == len(s) else res
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-08-03-387-First-Unique-Character-in-a-String.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-387-first-unique-character-in-a-string/) ，作者信息和本声明.
