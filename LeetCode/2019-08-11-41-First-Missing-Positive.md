# LeetCode 41. First Missing Positive

## Description

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

```py
Input: [1,2,0]
Output: 3
```
Example 2:

```py
Input: [3,4,-1,1]
Output: 2
```
Example 3:

```py
Input: [7,8,9,11,12]
Output: 1
```

Note:

Your algorithm should run in O(n) time and uses constant extra space.

## 描述

给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

```py
输入: [1,2,0]
输出: 3
```

示例 2:
```py
输入: [3,4,-1,1]
输出: 2
```

示例 3:

```py
输入: [7,8,9,11,12]
输出: 1
```
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 基本思想是：将数字 num 放在数组 nums 索引为 num-1 的位置。
* 拿到这道题的首先的思路就是找到数组中的最大值 max，然后声明一个长度为最大值长度的数组 array（初始值置为 False）；遍历给定的数组，将数字在新生成的数组中对应的位置置为 True；最后返回生成的数组 array 中第一个为 False 位置的索引 + 1；
* 借助这个思想，我们不生成新的数组，而是在原数组进行操作；
* 我们遍历数组；遇到小于 1 的数字跳过；将当前位置 i 的数放在 nums\[i]-1 的位置，将 nums\[i]-1 位置的数放到当前位置 i；也就是 i 位置 和 nums[i]-1 位置的值交换；交换后，我们看此时 i 位置的值 nums[i] 与 其本身 nums[i] 应该在的位置是否相等，即是 nums[nums[i] - 1]与 nums[i] 是否相等；如果不等，我们继续交换，直到 nums[i] 的值到达指定的位置，或者超出了范围；
* 最后我们遍历数组，如果所以 i 位置的值 不是 i+1，返回 i+1；如果所有数都满足这个条件，就返回 数组的长度 + 1；
* 注意：python 中 for 循环可以同 else 联用。

```py
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)

        if not nums:
            return 1
        for i in range(length):
            while 0 < nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                n = nums[i] - 1
                nums[i], nums[n] = nums[n], nums[i]

        for i, n in enumerate(nums, 1):
            if i != n:
                return i
        else:
            return n + 1

        return
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-08-11-41-First-Missing-Positive.py) 。
©本文是原创文章，欢迎转载，转载需保留 文章来源 ，作者信息和本声明.
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 文章来源 ，作者信息和本声明.
