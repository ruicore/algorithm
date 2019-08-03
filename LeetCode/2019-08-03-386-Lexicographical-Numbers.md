# LeetCode 386. Lexicographical Numbers

## Description

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

## 描述

给定一个整数 n, 返回从 1 到 n 的字典顺序。

例如，

给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。

请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lexicographical-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 为了节省空间，使用 Python 的 yield 关键字。
* 我们按照数字的位数遍历。另 start 初始为 1，遍历到当前位置时，在让当前位置自增 1 之前，先遍历当前位的下一位（高位），只要此时这个多位数小于等于 n ，就可以一直往后遍历；如果 start 超过 n，我们把 start 除以 10，然后遍历下一位，也就是加1；当前数末尾的 0 需要去掉；

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-03 15:05:01
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-03 15:32:23


from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        start = 1
        for _ in range(1, n + 1):
            # yield  节省空间
            yield start
            if start * 10 <= n:
                # 每次扩大 10 被
                start *= 10
            else:
                # 如果 start 到 n 之间还有数，先遍历这些数字
                # 否则让 start 的十位加 1
                start = start + 1 if start < n else start // 10 + 1
                # 末尾的 0 需要全部去掉
                while not start % 10:
                    start //= 10
        return
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-08-03-386-Lexicographical-Numbers.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-386-lexicographical-numbers/) ，作者信息和本声明.
