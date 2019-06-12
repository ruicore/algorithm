# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-03 14:54:52
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-04 14:56:19


class Solution:

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        res = 1
        left, right = set(), set()
        left.add(beginWord)
        right.add(endWord)
        while left or right:
            newset = set()
            left, right = right, left
            for word in left:
                for i in range(len(word)):
                    for j in range(0, 26):
                        newword = word[0:i]+chr(j+97)+word[i+1:]
                        if newword in wordset:
                            newset.add(newword)
                            wordset.remove(newword)
                        if newword in right:
                            return res+1
            res += 1
            left = newset
        return 0
