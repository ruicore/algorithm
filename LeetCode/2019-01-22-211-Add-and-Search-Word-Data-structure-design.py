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
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
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
