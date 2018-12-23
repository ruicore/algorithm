# LeetCode 80. Remove Duplicates from Sorted Array II

## Description

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

## 描述

给定排序的数组nums，就地删除重复项，使重复项最多出现两次并返回新的长度.

不要为另一个数组分配额外的空间，必须通过使用O（1）复杂度的额外空间来修改输入数组，从而实现此目的.

例1：给定nums = [1,1,1,2,2,3]，函数应返回length = 5，其中nums的前五个元素分别为1,1,2,2和3.

数组中超出了你返回范围的值无关紧要.

例2：给定nums = [0,0,1,1,1,1,2,3,3]，函数应返回length = 7，nums的前七个元素分别修改为0,0,1,1,2,3和3。

数组中超出了你返回范围的值无关紧要.

对为什么返回值是一个整数但输出的答案是一个数组感到迷惑？

请注意，输入数组通过引用传入，这意味着调用者也将知道对输入数组的修改。

下面这个例子可以帮助你理解：

// nums通过引用传入。 （即没有复制）
int len = removeDuplicates（nums）;

//调用者可以知道函数中对nums的任何修改。
//使用函数返回的长度，打印出前len个元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

### 思路

* 这道题我们采用就地移动的方式来是空间复杂度达到O(1).
* 我们两个变量index，count:index表示已经到达最终位置的元素的后面一个值，count表示当前元素出现的次数.
* index和count都初始化为1.
* 如果当前元素等于前面一个元素,count自增一次,如果不等count重置为1.
* 如果count小于等于2，我们把当前元素放到nums\[index],index自增一次.
* 直到遍历到nums尾部,我们返回index.

```python

# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-22 17:55:43
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-23 10:35:05


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 如果是空则返回0
        if not nums:
            return 0
        index, count = 1, 1
        for i in range(1, len(nums)):
            # 如果两个字符相等
            if nums[i-1] == nums[i]:
                # count计数自增一次
                count += 1
            # 如果不等，count重置为1
            else:
                count = 1
            # 如果count小于等于2，则把nums[i]放到有效位置的后一个位置
            if count <= 2:
                nums[index] = nums[i]
                index += 1
        # 删除无用元素[也可不用删除，LeetCode不会检查后面的元素]
        del nums[index:]
        return index


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    so = Solution()
    res = so.removeDuplicates(nums)
    print(res, nums)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-22-80-Remove-Duplicates-from-Sorted-Array-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-80-remove-duplicates-from-sorted-array-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
