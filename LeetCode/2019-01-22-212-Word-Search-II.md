# LeetCode 212. Word Search II

## Description

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]
Note:
You may assume that all inputs are consist of lowercase letters a-z.

## 描述

给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]

### 思路

* 这道题使用Trie这种数据结构，使用深度右边遍历这种数据结构.
* 为了提前结束回溯，我们将要搜索的字符串构造成一颗Trie树，这样当有某个字符没有出现在给定的board中时，我们就可以结束回溯.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-22 20:38:32
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-23 23:03:28


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ''


class Solution:
    def __init__(self):
        self.root = None
        self.res = []

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # 如果为空则直接返回
        if not board or not words: return []
        # 生成一颗Trie树
        self.createTrie(words)
        # 获取矩阵宽度和高度
        row, col = len(board), len(board[0])
        ischecked = [[False for _ in range(col)] for _ in range(row)]
        # 以每一个位置为出发点进行检查
        for i in range(row):
            for j in range(col):
                self.dfs(i, j, self.root, row, col, board, ischecked)
        return self.res

    def dfs(self, i, j, node, row, col, board, ischecked):
        # 如果是一个完整的单词，添加该单词，并将该单词置为空，避免重复
        if node.word:
            self.res.append(node.word)
            node.word = ''
        # 如果当前位置已经越界，则直接返回
        if i < 0 or i >= row or j < 0 or j >= col or ischecked[i][j]: return
        # 如果当前的字符不在trie中，返回
        if board[i][j] not in node.children: return
        # 能够执行到这里，说明该字符存在与Tire中，将当前的位置标记为已经访问过
        # 更新节点
        ischecked[i][j], newnode = True, node.children[board[i][j]]
        # 向上走一步
        self.dfs(i - 1, j, newnode, row, col, board, ischecked)
        # 想右走一步
        self.dfs(i + 1, j, newnode, row, col, board, ischecked)
        # 向左走一步
        self.dfs(i, j - 1, newnode, row, col, board, ischecked)
        # 向右走一步
        self.dfs(i, j + 1, newnode, row, col, board, ischecked)
        # 重置当前位置为未访问过
        ischecked[i][j] = False

    def createTrie(self, words):
        self.root = TrieNode()
        for word in words:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
        return
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-22-212-Word-Search-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-212-word-search-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
