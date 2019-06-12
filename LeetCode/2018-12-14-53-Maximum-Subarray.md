# LeetCode 53. Maximum Subarray

## Description

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## 描述

给定整数数组nums，找到具有最大总和的子数组（数组要求连续）并且返回数组的和，给定的数组包含至少一个数字。

### 思路

* 我们用res来表示最终的和，用temp来表示临时的和
* 初始时res = nums\[0]，temp = 0
* 遇到一个值，我们就把它加到temp上面，如果temp大于res，把temp赋值给res
* 如果temp小于res但是大于0，继续加和
* 如果temp小于零，我把temp置为零，因为此时temp已经小于零了，如果保留temp当前的值再往里面加值，整个的和一定会变得更小\[因为temp当前是负数]，
* 也就是说当temp是负数时，temp的贡献一定是负，无论后面加什么值，一定会使得当前的子数组和更小

```python
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 初始化为nums[0]
        res = nums[0]
        temp = 0
        for item in nums:
            # 往temp加和
            temp += item
            # 如果比res大，更新res
            if temp > res:
                res = temp
            # 如果小于0，则重置为0
            if temp < 0:
                temp = 0
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-14-53-Maximum-Subarray.py)
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-53-maximum-subarray/)，欢迎转载，转载需保留文章来源，作者信息和本声明.