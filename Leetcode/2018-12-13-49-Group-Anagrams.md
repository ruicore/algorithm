# LeetCode 49. Group Anagrams

## Description

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

## 描述

给定一组字符串，将由相同字母组成的字符串组合在一起。

注意：所有给定的输入都是小写，输出的顺序不重要

## 思路

* 这道题思路很清晰，也比较简单
* 对字符串排序，以排好序的字符串为键，构建hash表，值为包含字符串的list
* 用python实现很容易，因为由内置函数，如果改用C语言，会增加难度

```python
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        strdict = {}
        for item in strs:
            # 对字符串进行排序，sorted返回一个list，需要重新组装成为一个字符串
            key = ''.join(sorted(item))
            # 如果排好序的字符串已经存在，则将该字符串原来的形式插入对应的list
            if key in strdict.keys():
                strdict[key].append(item)
            else:
                # 如果不存在，就先创建一个list，然后在插入
                strdict[key] = []
                strdict[key].append(item)
        # 取出所有的结果，放到一个list中
        for key in strdict:
            res.append(strdict[key])
        # 返回所有的结果
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-13-49-Group-Anagrams.py)
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-49-group-anagrams/)，欢迎转载，转载需保留文章来源，作者信息和本声明.