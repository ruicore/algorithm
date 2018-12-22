# LeetCode 77. Combinations

## Description

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

## 思路

* 此题目求组合数.
* 使用递归求解.

```python
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res, nums = [], [i+1 for i in range(n)]
        self.recursion(res, [], nums, 0, n, k)
        return res

    def recursion(self, res, path, nums, start, end, depth):
        if depth == 1:
            for i in range(start, end):
                res.append(path+[nums[i]])
        for i in range(start, end):
            self.recursion(res, path+[nums[i]], nums, i+1, end, depth-1)


if __name__ == "__main__":
    so = Solution()
    res = so.combine(4, 2)
    print(res)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-22-77-Combinations.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-77-combinations/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
