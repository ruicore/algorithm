# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-18 18:11:57
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-18 20:41:12


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 获取字符串a和字符串b的长度
        len_a, len_b = len(a), len(b)
        # 结果数组
        res = []
        # 字典，用于记录哪一个字符更长
        longest = {}
        # 如果字符串a更长
        if len_a < len_b:
            num_min = len_a
            longest.setdefault('a', b)
            left = len_b-len_a
        # 如果字符串b更长
        else:
            num_min = len_b
            longest.setdefault('a', a)
            left = len_a-len_b
        temp = 0
        # 进行加和运算，注意二进制的进位，遍历a数组和b数组相互重叠的部分
        for index in range(1, num_min+1):
            # 从右往左开始做加法运算
            temp = temp+int(a[-index])+int(b[-index])
            # 如果大于2则表示需要进位
            if temp >= 2:
                # 进位，当前位置值设置为temp-2
                res.insert(0, temp-2)
                # 重置temp = 1
                temp = 1
            else:
                # 在结果数组的首位插入，然后将temp重置为0
                res.insert(0, temp)
                temp = 0
        # 对剩下的部分进行加和
        for index in range(left-1, -1, -1):
            temp = temp+int(longest.get('a')[index])
            if temp >= 2:
                res.insert(0, temp-2)
                temp = 1
            else:
                res.insert(0, temp)
                temp = 0
        if temp:
            res.insert(0, temp)
        # 以字符的形式返回
        return ''.join(str(x) for x in res)
