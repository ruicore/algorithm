# LeetCode 278. First Bad Version

## Description

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.

## 描述

你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

示例:

给定 n = 5，并且 version = 4 是第一个错误的版本。

调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true

所以，4 是第一个错误的版本。 

### 思路

* 采用二分法询问，如果在当前位置左边，我们继续询问左边的中点；如果在右边，我们询问右边的中点.
* 结束条件是当前位置元素不是坏的产品，当前位置的下一个位置是坏的产品.

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-05 16:35:35
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-05 16:35:35


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return True


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 二分查找，左边界，右边界
        left, right, middle = 1, n, 0
        while left <= right:
            middle = ((right - left) >> 1) + left
            # isBadVersion 函数由主调函数提供
            # 如果当前位置的右边
            if not isBadVersion(middle):
                # 结束条件
                if isBadVersion(middle + 1):
                    return middle + 1
                left = middle + 1
            # 如果在当前位置的左边
            else:
                right = middle - 1
        # 如果第一个元素就坏了，返回1
        if right == 0: return 1
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-05-278-First-Bad-Version.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-278-first-bad-version/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
