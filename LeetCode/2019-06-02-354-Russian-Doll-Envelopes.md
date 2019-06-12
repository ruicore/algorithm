# LeetCode 354. Russian Doll Envelopes

## Description

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: \[\[5,4],\[6,4],\[6,7],\[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 (\[2,3] => \[5,4] => \[6,7]).

## 描述

给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

说明:
不允许旋转信封。

示例:

输入: envelopes = \[\[5,4],\[6,4],\[6,7],\[2,3]]
输出: 3 
解释: 最多信封的个数为 3, 组合为: \[2,3] => \[5,4] => \[6,7]。

### 思路

* 题意即为前一个信封的宽度小于后一个信封的宽度，并且前一个信封的高度小于后一个信封。
* 对信封排序，宽度小的信封排在前面，宽度一样，高度大的信封排在前面（为什么把高度大的排在前面下面解释）。
* 当信封的宽度是递增的时候，我们只用考虑信封的高度。只要信封的高度小于后面一个信封的高度，我们就可以把这个信封塞进后买你一个信封。
* 此时，我们单独考虑信封的高度，就相当于在高度构成的数组中，确定最长递增序列的长度（LIS），这个长度就是要找的答案。
* 由于如（3，4），（3，7）这种信封，前一个不能被塞进后一个，所以我们希望在寻找高度最长递增序列的时候出现（7，4）（前一个信封不能塞进后一个信封）而不是（4，7）（前一个信封可以塞进后一个信封）。所以信封宽度一样的时候，高度大的排前面。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-02 13:04:40
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-02 15:26:38

import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        if not envelopes: return 0

        # 以信封的宽度和高度排序，宽度小的在前，宽度一样，高度大的在前
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        tails = list()

        # 所有的高度构成一个数组，寻找此数组中的连续最长递增序列
        for _, num in envelopes:
            index = bisect.bisect_left(tails, num)
            if index == len(tails):
                tails.append(num)
            else:
                tails[index] = num
        return len(tails)
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-06-02-354-Russian-Doll-Envelopes.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-354-russian-doll-envelopes/) ，作者信息和本声明.