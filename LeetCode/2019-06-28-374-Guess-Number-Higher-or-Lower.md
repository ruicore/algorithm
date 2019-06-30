# LeetCode 374. Guess Number Higher or Lower

## Description

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6

## 描述

我们正在玩一个猜数字游戏。 游戏规则如下：
我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
每次你猜错了，我会告诉你这个数字是大了还是小了。
你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

-1 : 我的数字比较小
 1 : 我的数字比较大
 0 : 恭喜！你猜对了！
示例 :

输入: n = 10, pick = 6
输出: 6

### 思路

* 使用二分法，left 表示左边界，right 表示右边界。
* num 为中间值，如果 num 大于要猜的值，将 right 置为 num - 1；如果 num 小于要猜的值，将 left 置为 num + 1。
 
```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-28 16:24:44
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-28 16:29:54

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        
        num = left + ((right - left) >> 1)
        res = guess(num)
        if res == 0: return num

        while res:
            if res == 1:
                left = num + 1
            if res == -1:
                right = num - 1
            num = left + ((right - left) >> 1)
            res = guess(num)

        return num
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-06-28-374-Guess-Number-Higher-or-Lower.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-374-guess-number-higher-or-lower/) ，作者信息和本声明.
