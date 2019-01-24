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
