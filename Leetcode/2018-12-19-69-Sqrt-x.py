# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-19 13:30:16
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-19 13:56:03


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 如果输入是1，则直接返回1
        if x == 1:
            return 1
        # 左边界，右边界，中间值，注意位运算9>>1=4,为整型
        left, right, middle = 0, x, x >> 1
        while True:
            # 对中间的值求平方
            multi = middle*middle
            # 如果平方小于x，说明sqrt(x)在[middle,right]之间
            if multi < x:
                left = middle
            # 如果平方大于x，说明sqrt(x)在[left,middle]之间
            elif multi > x:
                right = middle
            # 求middle+1的平方
            intmultib = (middle+1)*(middle+1)
            # 如果x落在了[middle,middle+1)之间，结束循环，返回middle
            if multi <= x < intmultib:
                return middle
            middle = left+((right-left) >> 1)


if __name__ == "__main__":
    so = Solution()
    res = so.mySqrt(190983754751)
    print(res)