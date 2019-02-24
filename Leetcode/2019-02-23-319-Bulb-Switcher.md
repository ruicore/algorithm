# LeetCode 319. Bulb Switcher

## Description

There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

```py
Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
```

## 描述

初始时有 n 个灯泡关闭。 第 1 轮，你打开所有的灯泡。 第 2 轮，每两个灯泡你关闭一次。 第 3 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启则关闭）。第 i 轮，每 i 个灯泡切换一次开关。 对于第 n 轮，你只切换最后一个灯泡的开关。 找出 n 轮后有多少个亮着的灯泡。

示例:

```py
输入: 3
输出: 1 
解释: 
初始时, 灯泡状态 [关闭, 关闭, 关闭].
第一轮后, 灯泡状态 [开启, 开启, 开启].
第二轮后, 灯泡状态 [开启, 关闭, 开启].
第三轮后, 灯泡状态 [开启, 关闭, 关闭]. 

你应该返回 1，因为只有一个灯泡还亮着。
```

### 思路

* 数学题，对给定的数字开平方向下取整即是答案。
* 暴力求解（会超时），但是通过暴力解法可以发现规律。我们声明一个长度为 n 的数组，数组初始值为 0 。然后我们按照题目要求对其进行改变状态的操作，0 表示关，1 表示开。我们通过这个会发现如果给定的 n 为前三个数（1~3）会有 1 盏灯亮着，如果给定的 n 为接下来的 5 个数 （4~8），会有 2 盏灯亮着，接下来的 7 个数（9~15）会有3 盏灯两者，我们称给定的所有可能的 n 中，最后剩下相同的灯亮着的情况的 n 为一组，于是可以发现每组 n 的个数是一个首项为 3 公差为 2 的等差数列。
* 于是有了第一个解法：我们不断的从 n 中减去，3，5，7 ... （n 小于零就停止），能减少多少次就有多少盏灯亮着。
* 我们可以发现 1~3：1；4~8：2；9~15：3，16~25：4，不难发现我们对 n 开放取整就可以得到答案，关于严格的数学证明请参考 [这里](https://leetcode.com/problems/bulb-switcher/discuss/77112/Share-my-o(1)-solution-with-explanation) 。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-23 18:46:36
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-23 19:46:07


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**0.5)

    def bulbSwitch2(self, n: int) -> int:
        count, i = 0, 3
        # 首项为3，公差为 2 的等差数列
        # n 为这些数字的和
        while n > 0:
            # 每次从 n 中去掉一项
            n -= i
            i += 2
            # 记录去掉的次数
            count += 1
        # 次数就是剩下的晾着的灯泡个数
        return count

    def bulbSwitch3(self, n: int) -> int:
        # 最直观的思路，用一个数组表示灯泡的开关情况，0 表示关，1 表示开
        # !!! 此方法会超时
        bulbs = [0 for i in range(n)]
        for i in range(n):
            j = i
            # 每轮调整 i 整数倍的位置
            while j < n:
                bulbs[j] ^= 1
                j += i + 1
        # 统计最后剩下的 1 的个数
        return bulbs.count(1)
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-23-319-Bulb-Switcher.py) 。
©本文首发于 [何睿的博客](https://www.ruicore.cn/leetcode-319-bulb-switcher/) ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-319-bulb-switcher/) ，作者信息和本声明.
