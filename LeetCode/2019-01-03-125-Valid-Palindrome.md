# LeetCode 125. Valid Palindrome

## Description

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

## 描述

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

## 思路

* 回文字符串是指字符串呈中心对成，即第一个字符与最后一个字符相等，第二个字符与倒数第二个字符相等.
* 我们用两个指针，一共从前往后遍历，一个从后往前遍历即可，需要注意的是我们只比较字母和数字，其他情况直接跳过.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-03 11:16:37
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-03 11:34:21


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        left, right = 0, len(s)-1
        while left < right:
            # 如果当前字符是数字或者字母
            if (s[left].isalpha() or s[left].isdigit()) and (s[right].isalpha() or s[right].isdigit()):
                # 如果相等则left向后走一步，right向前走一步
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    # 否则返回False
                    return False
            # 如果左边不是数字或者字符，则认为是满足回文符串的条件
            elif not (s[left].isalpha() or s[left].isdigit()):
                left += 1
            # 如果右边不是数字或者字符，则认为是满足回文字符串的条件
            elif not (s[right].isalpha() or s[right].isdigit()):
                right -= 1
        return True


if __name__ == "__main__":
    so = Solution()
    res = so.isPalindrome("0P")
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-03-125-Valid-Palindrome.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-125-valid-palindrome/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
