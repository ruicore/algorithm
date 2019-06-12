# LeetCode 70. Climbing Stairs

## Description

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2 Output: 2

Explanation: There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3 Output: 3
Explanation: There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

## 描述

你正在爬楼梯。 它需要n步才能达到顶峰。

每次你可以爬1或2步。 您可以通过多少不同的方式登顶？

注意：给定n将是一个正整数。

### 思路

* 题意是一个有n层的楼梯，每一次可以往上走1步或者2步，问走到楼顶一共有多少种方法.
* 对于楼梯的每一个位置，到达当前位置的上一步只有两种可能，即：来自前面一层楼梯或者前面两层楼梯.

$$ Steps[i] = Steps[i-1] + Steps[i-2] $$

* 我们初始化```Steps[1] = 1```,```Steps[2] = 1```,当前层totoal = preone + pretwo,更新preone = total,pretwo = preone 即可.

```python
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 如果只有一层，返回1
        if n == 1:
            return 1
        # 如果有两层，返回2
        if n == 2:
            return 2
        total, preone, pretwo = 0, 2, 1
        # 循环遍历，到达当前的层数的路径数 = 前一层的路径数+前两层的路径数
        for _ in range(3, n+1):
            total = preone + pretwo
            pretwo, preone = preone, total

        return total
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-19-70-Climbing-Stairs.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-70-climbing-stairs/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
