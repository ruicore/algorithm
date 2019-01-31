# LeetCode 228. Summary Ranges

## Description

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

## 描述

给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。

示例 1:

输入: [0,1,2,4,5,7]
输出: ["0->2","4->5","7"]
解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
示例 2:

输入: [0,2,3,4,6,8,9]
输出: ["0","2->4","6","8->9"]
解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。

### 思路

* 我们从第二个位置开始进行检测，我们用count表示区间的数字个数（不包括左节点），_str 表示区间的起始位置，如果当前位置的数值等于前一个位置的数值，我们将count自增一次.
* 如果不等，我们检查count是否为0，若为0，我们将_str添加到数组中；若count不为0，我们在_str后面添加当前位置前一个位置的元素，并将结果添加到结果数组中，并将_str重置为当前元素.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-29 20:49:54
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-29 21:06:11


class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # 如果没有数字，返回空数组
        if not nums: return []
        # 结果数组，存储每一个区间首位的字符，记录当前区间字符的个数（不包括起点）
        res, _str, count = [], str(nums[0]), 0
        for i in range(1, len(nums)):
            # 如果当前数字与前一个数字连续，count加一
            if nums[i - 1] + 1 == nums[i]:
                count += 1
            else:
                # 如果count为0，说明当前的区间只有一个数字
                if not count:
                    # 我们直接将这个数字放入结果数组中
                    res.append(_str)
                else:
                    # 如果count不为零，说明当前连续的区间不止一个数字，我们以nums[i - 1]为区间的结尾
                    # 并在两个数字之间加上"->"
                    res.append(_str + "->" + str(nums[i - 1]))
                _str, count = str(nums[i]), 0
        # 处理最后剩余的数字，如果_str不为空且count不为0，说明存在一个区间
        # 且需要加上"->"符号
        if _str and count:
            res.append(_str + "->" + str(nums[-1]))
        # 否则如果_str不为零count为0，说明当前只有一个数字
        elif _str:
            res.append(_str)
        # 返回最终结果
        return res
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-29-228-Summary-Ranges.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-228-summary-ranges/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
