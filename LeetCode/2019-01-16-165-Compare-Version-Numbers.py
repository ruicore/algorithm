# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 14:36:33
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 14:57:42


class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        list1, list2 = version1.split('.'), version2.split(".")
        count1, count2 = len(list1), len(list2)
        short = count1 if count1 < count2 else count2
        for i in range(short):
            if int(list1[i]) > int(list2[i]):
                return 1
            if int(list1[i]) < int(list2[i]):
                return -1
        if count1 > count2:
            i = count2
            while i < count1:
                if int(list1[i]) > 0:
                    return 1
                i+=1
        elif count1 < count2:
            i = count1
            while i < count2:
                if int(list2[i]) > 0:
                    return -1
                i+=1
        return 0
