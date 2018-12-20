# LeetCode 72. Edit Distance

## Description

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros" Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution" Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

## 描述

给定两个单词word1和word2，找到将word1转换为word2所需的最小操作数。

您对单词允许以下3个操作：

插入一个字符
删除一个字符
替换一个字符

### 思路

* 题意是给定两个单词，问将单词1变成单词二最少需要几次操作.允许的操作是:替换一个字符，增加一个字符，删除一个字符.类似数据库的增删改.
* 此题目考察[动态规划](https://zh.wikipedia.org/zh-hans/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92).

![LeetCode 72. Edit Distance](https://wp.me/aaizn9-Vl)

* 我们维护一个二维数组Matrixp\[row]\[col],如上图.接下来以字符串C1\[3]和C2\[2]为例说明(以下数组下标从1开始).
* 我们有三种方法把C1\[1:3]变成C2\[1:2]

1.如果我们已经知道C1\[1:3]变成C2\[1:1]的步数Step1,我们删除C1的最后一个元素.
2.如果我们已经知道C1\[1:2]变成C2\[1:2]的步数Step2,我们为C1增加一个元素.
3.如果我们已经知道C1\[1:2]变成C2\[1:1]的步数Step3,我们改变C1\[3]为C2\[2]\(如果元素已经相等，则不需要改变).

* 把C1\[3]变成C2\[2]为step1，step2，step3中的最小值,我们有递推关系式.

$$Matrix[i][j] = Min (Matrix[i-1][j]+1, Matrix[i-1][j-1]+1 (C1[i]!=C2[j]), Matrix[i][j-1]+1)$$
$$or: Matrix[i][j] = Min (Matrix[i-1][j]+1, Matrix[i-1][j-1]   (C1[i]==C2[j]), Matrix[i][j-1]+1)$$

* 同理我们把C1\[1:3]变成C2\[1:1]也有如上的三步.

```python
import sys
from pprint import pprint


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 获取字符串word1和字符串word2的长度
        numword1, numword2 = len(word1), len(word2)
        # 如果字符串word1长度为0，则字符串1变成字符串2需要numword2步
        if numword1 == 0:
            return numword2
        # 如果字符串2长度为0，则字符串1变成字符串0需要numword1步
        if numword2 == 0:
            return numword1
        # 声明结果数组
        res = []
        # 初始化二维矩阵，每一个位置都初始化为Int类型的最大值
        for _ in range(numword1+1):
            res.append([sys.maxsize for _ in range(numword2+1)])
        # 初始化矩阵第一行，表示一个空字符变成当前长度的字符需要几步
        for row in range(numword1+1):
            res[row][0] = row
        # 初始化矩阵第一列，表示一个空字符变成当前字符需要几步
        for col in range(numword2+1):
            res[0][col] = col
        # 遍历二维数组的每一个位置
        for row in range(1, numword1+1):
            for col in range(1, numword2+1):
                # 如果两个字符串当前字符相等
                if word1[row-1] == word2[col-1]:
                    res[row][col] = min(res[row][col-1]+1,
                                        res[row-1][col-1], res[row-1][col]+1)
                # 如果两个字符当前字符不相等
                else:
                    res[row][col] = min(res[row][col-1]+1,
                                        res[row-1][col-1]+1, res[row-1][col]+1)
        # 返回最后一个位置的值
        return res[numword1][numword2]


if __name__ == "__main__":
    so = Solution()
    res = so.minDistance("intention", "execution")
    pprint(res)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-20-72-Edit-Distance.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-72-edit-distance/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
