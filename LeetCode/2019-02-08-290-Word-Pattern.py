# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-08 11:19:39
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-09 09:43:27


class Solution:
    def wordPattern(self, pattern: 'str', str: 'str') -> 'bool':
        #  字典，记录对应关系
        match = {}
        # 将给定的单词用空格区分
        word = str.split(" ")
        # 如果长度不相等，直接返回False
        if len(pattern) != len(word): return False
        for i in range(len(pattern)):
            # 如果模式串pattern[i]不在字典中（键）
            if pattern[i] not in match:
                # 如果此时的单词在字典的值中，说明已经有模式串的字符与当前单词匹配，返回False
                if word[i] in match.values():
                    return False
                # 如果单词没有出现在字典的值中，添加当前模式串与单词的对应关系
                match[pattern[i]] = word[i]
            else:
                # 如果当前模式串的键已经在字典中，检查字典的值和当前单词是否相等，不等返回False
                if match[pattern[i]] != word[i]:
                    return False
        return True
