# LeetCode 76. Minimum Window Substring

## Description

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

## 描述

给定一个字符串S和一个字符串T，找到S中的最小窗口，它将包含复杂度为O（n）的T中的所有字符。

例： 输入：S ="ADOBECODEBANC"，T ="ABC" 输出："BANC"

注意：

如果S中没有覆盖T中所有字符的窗口，则返回空字符串“”。
如果有这样的窗口，则保证在S中始终只有一个唯一的最小窗口。

### 思路

* 题意是给定两个字符串，分别是S，T. 找到S中这样的字符串C，使得C包含T中的所有字符，返回长度最小的字符串C.
* 要返回最短的字符串，则C的开头和结尾一定是T中的字符，如果C开头不是T中的字符，C一定不是最短，因为去掉仍然满足条件且更短.
* 我们遍历一边数组，记下T中的字符在s中的位置，记录在indexs中.
* 我们用两个指针left,right. 其职位indexs中的值，指向S中在T中出现的字符索引.
* 每次检查s\left:right]是否包含T，若是
* 我们记录下此时的字符串res，然后left向右移动，继续检查当前字符串是否满足条件.
* 若不是，right向右移动，直到末尾.
* 返回res.

#### 注意

* 检查当前字符串C是否包含T，是要保证T中的所有字符在T中出现了足够的次数.
* 我们用两个字典vd, nvd.
* vd记录T中每个字符出现的次数，nvd用于记录当前字符串C中有效字符出现的字符.
* 当nvd中的每个值都大于等于vd中的每个值时，此时C字符串才是有效的字串.
* 我们更新res字符串时，检查当前C的长度是否小于res，若是才更新res.

```python

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left, right = 0, 0
        # valid count 表示一共需要的有效的总数
        # now valid count 目前找到的有效的总数
        vc, nvc = 0, 0
        # res 用于存储结果，存储字符串的开始和结尾
        res = [-1, -1]
        # 用于存储t中的字母出现在s中的每一个位置
        indexs = []
        # vd ：valid dict 用于记录目标字符串中每个字符需要出现的次数
        # nvd: now valid dict 目前找的的有效字符的个数
        vd, nvd = {}, {}
        # 找到t中的所有字母在t中的位置
        for i in range(len(s)):
            if s[i] in t:
                indexs.append(i)
        if not indexs:
            return ""
        # 初始化vd，nvd数组
        for item in t:
            vc += 1
            nvd[item] = 0
            vd[item] = vd[item]+1 if item in vd else 1
        # 遍历每一个节点
        for right in range(len(indexs)):
            nvd[s[indexs[right]]] += 1
            # 如果当前字母的个数没有超过最大需要的次数，则当前字母出现有效
            # nvc自增一次
            if nvd[s[indexs[right]]] <= vd[s[indexs[right]]]:
                nvc += 1
            # 如果当前字符欻满足条件，即包含t
            while self.check(left, right, vc, nvc):
                # 将t记录在结果数组中
                self.put(res, indexs, left, right)
                # 将当前字母剔除
                nvd[s[indexs[left]]] -= 1
                # 如果当前字符出现小于需要的次数，则有效字符总数减一
                if nvd[s[indexs[left]]] < vd[s[indexs[left]]]:
                    nvc -= 1
                # left指针向右移动
                left += 1
        return '' if res[0] == -1 else s[res[0]:res[1]+1]

    def check(self, left, right, vc, nvc):
        # 当left大于right返回False
        if left > right:
            return False
        # 当当前有效此处与需要的有效次数相等事后返回Ture
        elif vc == nvc:
            return True
        # 其他情况返回False
        else:
            return False

    def put(self, res, indexs, left, right):
        subtraction = res[1]-res[0]
        # 如果当前res数组为空或者当前有效的字符串小于res数组中的字符串
        # 更新res数组
        if subtraction == 0 or subtraction > indexs[right]-indexs[left]:
            res[0], res[1] = indexs[left], indexs[right]


if __name__ == "__main__":
    so = Solution()
    res = so.minWindow(s="cabwefgewcwaefgcf", t="cae")
    print(res)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-21-76-Minimum-Window-Substring.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-76-minimum-window-substring/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
