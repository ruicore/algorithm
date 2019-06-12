# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-22 10:34:14
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-22 20:06:26


class Trie:
    # 节点类型
    class TrieNode:
        def __init__(self):
            # 标记是否是单词结尾
            self.end = False
            # 存储每个字母
            self.children = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 声明辅助根节点
        self.root = Trie.TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        # 从根节点开始插入
        node = self.root
        for char in word:
            # 当前字母不在根节点才进行插入
            if char not in node.children:
                node.children[char] = Trie.TrieNode()
            # 下一个节点
            node = node.children[char]
        # 设置结尾标记为True
        node.end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        # 查找单词
        node = self._find(word)
        # 单词存在且是单词结尾返回True，否则返回False
        return node is not None and node.end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        # 只要存在prefix即可返回True
        return not self._find(prefix) is None

    def _find(self, word):
        node = self.root
        for char in word:
            if char not in node.children: return None
            node = node.children[char]
        return node