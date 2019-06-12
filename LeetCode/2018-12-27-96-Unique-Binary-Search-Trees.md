# LeetCode 96. Unique Binary Search Trees

## Description

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

```python
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

## 描述

* 给定一个自然数n，返回从1到n可能构成的二叉搜索树的个数.
* 此题目使用动态规划.

```python
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0 for _ in range(n+1)]
        nums[0] = 1
        nums[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                # 递归关系式
                nums[i] += nums[i-j-1]*nums[j]
        return nums[n]
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-27-96-Unique-Binary-Search-Trees.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-96-unique-binary-search-trees/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
