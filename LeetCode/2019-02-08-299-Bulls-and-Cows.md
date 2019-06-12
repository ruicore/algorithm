# LeetCode 299. Bulls and Cows

## Description

You are playing the following [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows) game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

```py
Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
```

Example 2:

```py
Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
```

Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

## 描述

你正在和你的朋友玩 猜数字（Bulls and Cows）游戏：你写下一个数字让你的朋友猜。每次他猜测后，你给他一个提示，告诉他有多少位数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位数字猜对了但是位置不对（称为“Cows”, 奶牛）。你的朋友将会根据提示继续猜，直到猜出秘密数字。

请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。

请注意秘密数字和朋友的猜测数都可能含有重复数字。

示例 1:

```py
输入: secret = "1807", guess = "7810"

输出: "1A3B"

解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。
```

示例 2:

```py
输入: secret = "1123", guess = "0111"

输出: "1A1B"

解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。
```

说明: 你可以假设秘密数字和朋友的猜测数都只包含数字，并且它们的长度永远相等。

### 思路

* 我们遍历secret和guess字符串中的字符，如果字符相等，我们让A自增一次（A初始化为0），如果不等，我们利用哈希表count统计secret中字符出现的次数，并把guess中的字符添加到unused数组中.
* 遍历完一趟数组之后，我们已经获得了A的个数，接下来我们遍历unused数组，如果unuesed数组中的元素出现在了count表中，并且次数大于0，我们另B加一，并且另count当前元素对应的值减一，表示当前元素已经用了一次.
* 最后我们按要求返回字符串即可.

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-08 18:00:07
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-08 18:22:24


class Solution:
    def getHint(self, secret: 'str', guess: 'str') -> 'str':
        A, B = 0, 0
        # 字典，用于统计secret出现的字符个数
        # unused用于统计guess中还没有和secret匹配的字符（指对应位置字符不等）
        count, unused = {}, []
        for x, y in zip(secret, guess):
            # 如果对应位置的字符相等，A自增一次
            if x == y:
                A += 1
            else:
                # 否则我们统计secret中当前字符出现的次数
                count[x] = count.get(x, 0) + 1
                # 并将guess中的当前字符添加到unused中
                unused.append(y)
        # 我们遍历unsed中的字符
        for item in unused:
            # 如果当前字符出现在了count字典中
            if item in count and count[item] > 0:
                # B自增一次
                B += 1
                # 字典中对应字符次数减少一次，表示当前字符已经被匹配了一次
                count[item] -= 1
        return str(A) + "A" + str(B) + "B"
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-08-299-Bulls-and-Cows.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-299-bulls-and-cows/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
