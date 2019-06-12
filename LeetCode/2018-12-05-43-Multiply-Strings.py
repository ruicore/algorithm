# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-05 16:46:00
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-06 11:10:31


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        lennum1, lennum2 = len(num1), len(num2)
        result = [0]*(lennum1+lennum2)

        # 共有两层
        for i in range(lennum1-1, -1, -1):
            for j in range(lennum2-1, -1, -1):
                # 首先计算乘积，注意用ASCII码的方式转换为数值
                temp = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
                # 计算所得应和i+j位置求和
                _sum = temp+result[i+j+1]
                # 第i+j个位置
                result[i+j+1] = _sum % 10
                # 第i+j-1个位置,此代码为python3，注意使用'//'等号进行运算，例5/2=2.5,5//2=2
                result[i+j] += _sum//10
        # 将数字转换为字符串
        result = [str(i) for i in result]
        return ''.join(result[1:]) if result[0] == "0" else ''.join(result)


if __name__ == "__main__":
    so = Solution()
    print(so.multiply(num1="2", num2='3'))
