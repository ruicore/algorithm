# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-04 19:25:43
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-04 20:31:32


class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 维护一个数字到英语的转换字典
        self.IntEng = {
            "0": 'Zero',
            "1": 'One',
            "2": 'Two',
            "3": 'Three',
            "4": 'Four',
            "5": 'Five',
            "6": 'Six',
            "7": 'Seven',
            "8": 'Eight',
            "9": 'Nine',
            "10": 'Ten',
            "11": 'Eleven',
            "12": 'Twelve',
            "13": 'Thirteen',
            "14": 'Fourteen',
            "15": 'Fifteen',
            "16": 'Sixteen',
            "17": 'Seventeen',
            "18": 'Eighteen',
            "19": 'Nineteen',
            "20": 'Twenty',
            "30": 'Thirty',
            "40": 'Forty',
            "50": 'Fifty',
            "60": 'Sixty',
            "70": 'Seventy',
            "80": 'Eighty',
            "90": 'Ninety',
            "100": 'Hundred',
        }
        # 没三节为一个单位，2^31最大用到的单位为Billion
        units = ['', 'Thousand', 'Million', 'Billion']
        res = ''
        # 将数字转换成为字符串
        _str = str(num)
        # count:字符串中字符个数，i:数字三个为一节，当前数字所在节
        count, i = len(_str), 0
        while count - (i + 1) * 3 >= 0:
            # 取出三个数字
            _num = _str[count - (i + 1) * 3:count - i * 3]
            # 三个数字都不为0进行计算
            if not _num == "000":
                s = self.__readthree(_num)
                res = s + " " + units[i] + " " + res
            # 进入下一节
            i += 1
        # 如果最后一节不足三个数，处理剩下的数
        if count - (i * 3):
            s = self.__readthree(_str[0:count - (i * 3)])
            res = s + " " + units[i] + " " + res
        # 返回结果，去掉最后的空格
        return res.strip()

    # 私有函数，读一节（三个数字）数
    def __readthree(self, _str):
        _str = str(int(_str))
        if len(_str) == 1:
            return self.IntEng[_str]
        if len(_str) == 2:
            return self.__readtwo(_str)
        if len(_str) == 3:
            res = self.IntEng[_str[0]] + " " + "Hundred"
            if int(_str) % 100:
                return res + " " + self.__readtwo(_str[1:])
            else:
                return res

    # 私有函数，读两位数，辅助读一节数字
    def __readtwo(self, _str):
        _str = str(int(_str))
        if int(_str) <= 20 or _str[1] == "0":
            return self.IntEng[_str]
        else:
            return self.IntEng[_str[0] + '0'] + " " + self.IntEng[_str[1]]
