# LeetCode 58. Length of Last Word

## Description

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5

## 描述

给定字符串s由大写/小写字母和空格字符''组成，返回字符串中最后一个单词的长度。

如果最后一个单词不存在，则返回0。

注意：单词定义为字符序列仅由非空格字符组成。

### 思路

* 这道题属于easy难度，真正的笔试出现的机率很小
* 在python中，用空格分开每个单词，返回最后一个单词的长度

```python
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        try:
            split_words = s.split()
            return len(split_words[-1])
        except:
            return 0
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-16-58-Length-of-Last-Word.py).
©本文是原创文章，欢迎转载，转载需保留[文章来源](https://www.ruicore.cn/)，作者信息和本声明.