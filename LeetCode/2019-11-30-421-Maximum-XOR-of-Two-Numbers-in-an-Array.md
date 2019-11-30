# LeetCode 421. Maximum XOR of Two Numbers in an Array

## Description

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

```py
Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
```
## 描述

给定一个非空数组，数组中元素为 a0, a1, a2, … , an-1，其中 0 ≤ ai < 231 。

找到 ai 和aj 最大的异或 (XOR) 运算结果，其中0 ≤ i,  j < n 。

你能在O(n)的时间解决这个问题吗？

示例:

```py
输入: [3, 10, 5, 25, 2, 8]

输出: 28

解释: 最大的结果是 5 ^ 25 = 28.
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
### 思路

* 抑或运算有一个性质，如果 a ^ b = c 那么 a ^ c = b。
* 题目给定数据的输入范围是 32 int 类型，那么其抑或得到的结果也是 32 位。
* 基本思路是，我们考察这个最大值的每一位有没有可能是 1。
* 从最高位置开始考察，如果该位置可以为 1，则置为 1，否则置为 0.
* 设最终结果 res = 0，步骤如下：

1. 我们取每个数（每个数都有 32 位，不足用 0 占位）的前一位，将这些数添加到一个 set 中，置 tmp_res = res,将 tmp_res 向右移动一位，用 tmp_res 依次抑或每一个值，得到结果 tmp，如果 tmp 也在 set 中，说明，存在两个数抑或的结果为 tmp_res，更新 res = tmp_res。
2. 取每个数的前 2 位，添加到 set（初始为空，不是上一次结果的 set ） 中。置 tmp_res = res,将 tmp_res 向右移动一位。用 tmp_res 依次抑或每一个值得到结果 tmp，如果所有的 tmp 都不在 set 中，说明不存在两个数抑或的结果为 tmp_res，res 不更新。
3. 取每个数的前 3 位，添加到 set 中。tmp_res 置为 res，并向右移动一位。依次与 set 中每个值抑或，检查抑或的结果是否也在 set 中，若是，更新 res = tmp_res，否则不更新 res 
4. ...
5. 返回 res

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-11-30 09:35:38
# @Last Modified by:   何睿
# @Last Modified time: 2019-11-30 10:10:40

from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res, mask = 0, 0
        for i in range(31, -1, -1):
            # mask 值的变化是：
            # mask = 0 ｜ 10000000000000000000000000000000 = 10000000000000000000000000000000
            # mask = 10000000000000000000000000000000 | 01000000000000000000000000000000 = 11000000000000000000000000000000
            # mask = 11000000000000000000000000000000 | 00100000000000000000000000000000 = 11100000000000000000000000000000
            mask |= (1 << i) # 用来取每个数的前 1 为，前 2 位 ...
            prefix = set(num & mask for num in nums) # 将前 n 位的结果添加到空 set 中
            tmp = res | (1 << i) # 考察 res 的下一位是否可以为 1
            for s in prefix:
                if tmp ^ s in prefix:
                    res = tmp
                    break

        return res

```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-11-30-421-Maximum-XOR-of-Two-Numbers-in-an-Array.py) 。
©本文是原创文章，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-421-maximum-xor-of-two-numbers-in-an-array/) ，作者信息和本声明.
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-421-maximum-xor-of-two-numbers-in-an-array/) ，作者信息和本声明.
