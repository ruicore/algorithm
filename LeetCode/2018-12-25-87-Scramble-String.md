# LeetCode 87. Scramble String

## Description

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

```python
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
```

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

```python
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
```

We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

```python
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
```

We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false

## 描述

* 题意是给定两个字符串，判断他们是否满足某种关系.

### 思路

* 根据题意，我们观察二叉树的叶子节点，有如下关系：
* (左子树 == 左子树 and 右子树 == 右子树) or (左子树 == 右子树 and 右子树 == 左子树).
* 我们以上图第一图和第二图为例:
* 第一图左串gr == 第二图左串 rg,第一图右串eat == 第二图右串eat.
* 其中gr == rg：第一图gr的左串g == 第二图rg右串g，第一图gr的右串r == 第二图rg左串r，
* 其中eat == eat:第一图左串e = 第二图左串 e；第一图右串at == 第二图右串at：第一图左串 a = 第二图左串a，第一图右串= 第二图右串

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-25 15:11:08
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-25 16:25:11


class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 如果有一个字符串为空，或者两个字符串的长度不相等，则返回False
        if not s1 or not s2 or len(s1) != len(s2):
            return False
        # 如果字符串长度为1，并且字符相等则返回True
        elif len(s1) == 1 and s1 == s2:
            return True
        # 如果两个字符含有的字符不同，返回False
        elif sorted(s1) != sorted(s2):
            return False
        length = len(s1)
        for i in range(1, length):
            left, right = s1[0:i], s1[i:length]
            # 每一个位置都被分开
            # 如果 左==左 and 右 == 右 或者 左==右 and 右== 左则返回Ture
            if (self.isScramble(left, s2[0:i]) and self.isScramble(right, s2[i:len(s2)])) or \
                    (self.isScramble(left, s2[len(s2) - i:len(s2)]) and self.isScramble(right, s2[0:len(s2)-i])):
                return True
        # 否则返回False
        return False


if __name__ == "__main__":
    so = Solution()
    res = so.isScramble("abcdefghijklmnopq", 'efghijklmnopqcadb')
    print(res)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-25-87-Scramble-String.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-87-scramble-string/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
