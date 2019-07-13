# LeetCode 376. Wiggle Subsequence

## Description

A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, \[1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, \[1,4,7,2,5] and \[1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:

Input: \[1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: \[1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is \[1,17,10,13,10,16,8].
Example 3:

Input: \[1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?

## 描述

如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。

例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。

给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

示例 1:

输入: [1,7,4,9,2,5]
输出: 6 
解释: 整个序列均为摆动序列。
示例 2:

输入: [1,17,5,10,13,15,10,5,16,8]
输出: 7
解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。
示例 3:

输入: [1,2,3,4,5,6,7,8,9]
输出: 2
进阶:
你能否用 O(n) 时间复杂度完成此题?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wiggle-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 使用动态规划求解。动态规划适用于求解「是否」，「有几种」这类型的问题，而如果一个问题要问为什么可以，可以的路径是什么；具体解决问题的各种方案是什么时，动态规划就不适用了。
* 动态规划类的问题求解有几个要素：1.状态，明确状态的含义是什么；2. 转移方程，当前状态转移到下一个状态的条件是什么；3.结果，求解的结果和状态之间的关系是什么。
* 关于这道题目，状态是：使用一个一维数组 dp，dp 的每一个元素都是一个有两个元素的数组，dp\[i]\[0] 表示以给定的数组 nums 中的 nums\[i] 作为最后一个数来形成的最长摆动序列；此时最后一个数与前一个数之间的差值符号（用 1，-1，0 表示，1 表示 nums\[i] - nums\[j] >0；-1 表示 nums\[i] - nums\[j] <0； 0 此时序列只有一个数）；dp\[i]\[1] 表示此时形成的最长摆动序列的长度；
* 转移方程：假设我们已经知道了 dp 的前 i-1 个结果，也就是说以 nums\[i-1] 作为摆动序列的最后一个元素，此时的摆动序列长度，与上一个数的差值符号已经知道；以 nums\[i-1] 作为摆动序列的最后一个元素，此时的摆动序列长度，与上一个数的差值符号已经知道 ... nums\[0] ... 已经知道；为了求解 dp\[i],我们从 nums\[i-1] 开始向前遍历，找到一个数 nums\[j] 使得，(nums\[i] - nums\[j]) 与 dp\[j]\[0] 的乘积小于 0，说明 nums\[i] 可以追加到以 nums\[j] 作为结尾的摆动序列后面，于是我们将 dp\[i]\[1] 置为 dp\[j]\[1] + 1;要注意的是，如果乘积等于 0，但是 nums\[i] - nums\[j] 不为 0，说明以 nums\[j] 作为结尾的只有一个数，此时也应当更新 dp\[i]\[1] 置 dp\[j]\[1] + 1；
* 结果：dp\[-1]\[0]

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-07-13 07:52:43
# @Last Modified by:   何睿
# @Last Modified time: 2019-07-13 08:15:12


from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0

        dp = [[0, 1] for _ in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(i, -1, -1):
                diff = nums[i] - nums[j]
                if diff * dp[j][0] <= 0 and diff != 0 and (dp[j][1] + 1) > dp[i][1]:
                    dp[i][0] = diff // abs(diff)
                    dp[i][1] = dp[j][1] + 1
                    break

        return dp[-1][1]

```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-07-13-376-Wiggle-Subsequence.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-376-wiggle-subsequence/) ，作者信息和本声明.
