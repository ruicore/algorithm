# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-28 20:01:58
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-28 22:42:49


class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # 第一个矩形的面积，第二个矩形的面积
        area1, area2 = (C - A) * (D - B), (G - E) * (H - F)
        # 重叠的长，重叠的宽
        _long, _width = min(C, G) - max(A, E), min(D, H) - max(B, F)
        # 如果长宽中有一个小于零，说明并不存在重叠的矩形，设置其面积为0，否则其面积为长*宽
        overlap = _long * _width if _long > 0 and _width > 0 else 0
        return area1 + area2 - overlap
