# LeetCode 211. Add and Search Word Data structure design

## Description

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

## 描述

设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

### 思路

* 本题目使用Trie这种数据结构和深度优先遍历.
* 使用Trie将所有要查询的所有数据结构存储起来.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-22 12:31:27
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-22 17:04:59


class WordDictionary:
    class TreeNode:
        def __init__(self):
            self.end = False
            self.children = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TreeNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.TreeNode()
            node = node.children[char]
        node.end = True

    def search(self, word):
        """
        Returns if the word is in the data structure. 
        A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.end:
                self.res = True
            return
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-22-211-Add-and-Search-Word-Data-structure-design.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-211-add-and-search-word-data-structure-design/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
