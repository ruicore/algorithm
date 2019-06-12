# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-18 17:28:42
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-18 17:36:33


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 结果数组
        res = []
        # 数组最后一个元素的索引
        index = len(digits)-1
        # 获取最后一个元素的值
        last = digits[index]
        # 当需要进位的时候才进行循环
        while last+1 == 10:
            # 需要进位，在首位插入0
            res.insert(0, 0)
            # index指向数组的前一个元素
            index -= 1
            # 如果index越界，重新赋值为0，即重新指向首位置
            if index == -1:
                index += 1
                # 在输入数组的首位插入0占位
                digits.insert(0, 0)
            # last继续指向输入数组的末尾位置，此时index已经自减一次
            last = digits[index]
        digits[index] += 1
        # 将res和digits数组中的元素合并
        res = digits[:index+1]+res
        return res
