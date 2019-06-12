# LeetCode 60. Permutation Sequence

## Description

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

## 描述

集合[1,2,3，...，n]总共包含n的阶乘个独特的排列。

通过按顺序列出和标记所有排列，我们得到n = 3的以下序列：

"123"
"132"
"213"
"231"
"312"
"321"

给定n和k，返回第k个排列序列。

注意：

给定n将介于1和9之间。
给定k将介于1和n的阶乘之间！闭区间。

### 思路

![LeetCode 60. Permutation Sequence](https://wp.me/aaizn9-Sz)

* 最直观的思路是把所有的排列求出来，然后直接返回第K个(下标为k-1)，但是这样做既浪费时间，又浪费空间
* 我们通过计算的方式来求得排列的每个数字，我们另nums=\['1','2','3'···'k']
* n个数的排列组合，同一个数字开头的排列组合共有（n-1）！个，因此
* 我们有 denominator / numerator = quotient ··· remainder，即: k / (n-1)! = quotient ··· remainder①.
* 我们把相同字母开头的组合称为一组，由上式①得到要求的序列在第quotient组的第remainder个,如上示意图.
* 第quotient组开头的字母就是nums中的nums\[quotient]元素（这里要注意：如果remainder==0，则是nums\[quotient-1]，表示第quotient组的第0个元素，即第quotient-1的最后一个元素）
* 我们把当前的元素放到结果数组中，然后删除当前位置的元素，更新 denominator = remainder，n = n-1
* 结束条件是denominator==0，此时我们确定了是第quotient-1组的最后一组元素，我们倒序把nums字符数组中剩余的元素添加到res中即可.

```python

import math

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1, n+1)]
        res = []
        denominator, numerator = k, k
        while denominator:
            numerator = math.factorial(n-1)
            quotient = denominator//numerator
            remainder = denominator % numerator
            if remainder:
                res.append(nums[quotient])
                del nums[quotient]
            else:
                res.append(nums[quotient-1])
                del nums[quotient-1]
            denominator = remainder
            n -= 1
        return ''.join(res+nums[::-1])
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-17-60-Permutation-Sequence.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-60-permutation-sequence/)，欢迎转载，转载需保留文章来源，作者信息和本声明.