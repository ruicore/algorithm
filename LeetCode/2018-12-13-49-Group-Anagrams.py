# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-13 16:05:46
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-13 16:32:08


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        strdict = {}
        for item in strs:
            key = ''.join(sorted(item))
            if key in strdict.keys():
                strdict[key].append(item)
            else:
                strdict[key] = []
                strdict[key].append(item)
        for key in strdict:
            res.append(strdict[key])
        return res

if __name__ == "__main__":
    so = Solution()
    res  = so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(res)