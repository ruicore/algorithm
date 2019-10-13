# LeetCode 414. Third Maximum Number

## Description

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:

```py
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
```

Example 2:

```py
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
```

Example 3:

```py
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
```

## 描述

给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:

```py
输入: [3, 2, 1]

输出: 1

解释: 第三大的数是 1.
```

示例 2:

```py
输入: [1, 2]

输出: 2

解释: 第三大的数不存在, 所以返回最大的数 2 .
```

示例 3:

```py
输入: [2, 2, 3, 1]

输出: 1

解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/third-maximum-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 使用一个有 3 个元素的 bucket，从大到小排序，初始化为最小值。
* 遍历数组 nums，把数组中的数 num 与 bucket 中的数字 t 比较，如果 num 大于当前位置的数 t ，则 bucket 此位置的数（包括）向后移动，把 num 放到此位置。
* 如果 num 已经出现在了 bucket 中，则跳过此数字。
* 最后 bucket 的最后一个数就是所求。如果最后的一个数依然是 最小值，说明给定的数组中没有第三小的数。返回最大的数。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-10-13 20:27:38
# @Last Modified by:   何睿
# @Last Modified time: 2019-10-13 20:55:02

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        bucket = [float("-inf"), float("-inf"), float("-inf")]
        for num in nums:
            for i in range(3):
                if num > bucket[i]:
                    self._update(i, num, bucket)
                    break
                if num == bucket[i]:
                    break

        return bucket[-1] if bucket[-1] != float("-inf") else bucket[0]

    def _update(self, i, num, bucket):
        if i == 0:
            bucket[1], bucket[2] = bucket[0], bucket[1]
            bucket[0] = num
        elif i == 1:
            bucket[2] = bucket[1]
            bucket[1] = num
        elif i == 2:
            bucket[2] = num
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-10-13-414-Third-Maximum-Number.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-414-third-maximum-number/) ，作者信息和本声明.
