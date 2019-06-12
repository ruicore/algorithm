# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-21 15:02:53
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-22 08:49:52


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left, right = 0, 0
        # valid count 表示一共需要的有效的总数
        # now valid count 目前找到的有效的总数
        vc, nvc = 0, 0
        # res 用于存储结果，存储字符串的开始和结尾
        res = [-1, -1]
        # 用于存储t中的字母出现在s中的每一个位置
        indexs = []
        # vd ：valid dict 用于记录目标字符串中每个字符需要出现的次数
        # nvd: now valid dict 目前找的的有效字符的个数
        vd, nvd = {}, {}
        # 找到t中的所有字母在t中的位置
        for i in range(len(s)):
            if s[i] in t:
                indexs.append(i)
        if not indexs:
            return ""
        # 初始化vd，nvd数组
        for item in t:
            vc += 1
            nvd[item] = 0
            vd[item] = vd[item]+1 if item in vd else 1
        # 遍历每一个节点
        for right in range(len(indexs)):
            nvd[s[indexs[right]]] += 1
            # 如果当前字母的个数没有超过最大需要的次数，则当前字母出现有效
            # nvc自增一次
            if nvd[s[indexs[right]]] <= vd[s[indexs[right]]]:
                nvc += 1
            # 如果当前字符欻满足条件，即包含t
            while self.check(left, right, vc, nvc):
                # 将t记录在结果数组中
                self.put(res, indexs, left, right)
                # 将当前字母剔除
                nvd[s[indexs[left]]] -= 1
                # 如果当前字符出现小于需要的次数，则有效字符总数减一
                if nvd[s[indexs[left]]] < vd[s[indexs[left]]]:
                    nvc -= 1
                # left指针向右移动
                left += 1
        return '' if res[0] == -1 else s[res[0]:res[1]+1]

    def check(self, left, right, vc, nvc):
        # 当left大于right返回False
        if left > right:
            return False
        # 当当前有效此处与需要的有效次数相等事后返回Ture
        elif vc == nvc:
            return True
        # 其他情况返回False
        else:
            return False

    def put(self, res, indexs, left, right):
        subtraction = res[1]-res[0]
        # 如果当前res数组为空或者当前有效的字符串小于res数组中的字符串
        # 更新res数组
        if subtraction == 0 or subtraction > indexs[right]-indexs[left]:
            res[0], res[1] = indexs[left], indexs[right]


if __name__ == "__main__":
    so = Solution()
    res = so.minWindow(s="cabwefgewcwaefgcf", t="cae")
    print(res)
