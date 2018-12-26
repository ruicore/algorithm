# LeetCode 93. Restore IP Addresses

## Description

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

```python
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
```

## 描述

* 给定一个用数字表示的字符串，把它们恢复成可能的IP地址.
* 有效的IP地址格式为:

1.一共有4段，每一段之间用点号'.'隔开.
2.每一段的值小于等于255.
3.每一段不能以0开头（除了只有0本身的情况）.

### 思路

* 此题目使用递归的方法.
* 我们每次尝试从给定的字符串s种拿出一个字符，或者两个字符，或者三个字符作为一段，然后从剩下的字符种拿出一个，或两个，或三个作为一段
* 我们用depth表示已经去到了的段数，index表示剩下的字符的开始索引，length表示剩下的字符个数.
* 递归结束条件

1.当depth == 4 and length == 0，说明我们已经取到了三段，并且s中没有剩下的字符，说明当前的解有效，我们添加到最终结果之中.
2.当depth == 4 and lenght  > 0，说明我们已经去到了三段，但是s中还有剩下的字符，说明当前的解无效，函数返回.

* 在循环的过程中，如果s中已经没有剩下的字符，跳出循环.
* 如果当前段取了不止一个字符且第一个字符是'0'，说明当前段不合法，跳出循环.
* 如果当前段取了三个字符且这三个字符构成的数字大于255，说明当前段不合法，跳出循环.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-26 14:00:33
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-26 14:00:33


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length, res = len(s), []
        self.recur(s, res, '', 0, 0, length)
        return res

    def recur(self, s, res, path, index, depth, length):
        # 如果已经取了三段，还有s字符串还有剩余，直接返回
        if depth == 4 and length > 0:
            return
        # 如果已经取了三段，并且s字符串没有剩余，说明当前结果有效，把当前结果添加到最终结果之中
        # 注意要去掉最后一个点号
        if depth == 4 and length == 0:
            res.append(path[:-1])
        # 每次都可以取1个，或者2个，或者3个字符.
        for i in range(1, 4):
            # 如果当前已经没有字符剩余，跳出循环
            if length <= 0:
                break
            # IP地址的每一段不能以0开头
            if s[index] == '0'and i != 1:
                break
            # IP地址的每一段只能小于等于255
            if i == 3 and int(s[index:index+i]) > 255:
                break
            # 选择IP地址的下一段
            self.recur(s, res, path+s[index:index+i] +
                       ".", index+i, depth+1, length-i)


if __name__ == "__main__":
    so = Solution()
    res = so.restoreIpAddresses("111111111111111111111")
    print(res)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-26-93-Restore-IP-Addresses.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-93-restore-ip-addresses/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
