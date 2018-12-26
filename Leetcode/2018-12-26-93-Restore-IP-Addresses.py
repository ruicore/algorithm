# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-26 14:00:33
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-26 14:00:33


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length, res = len(s), []
        self.recur(s, res, '', 0, 0, length)
        return res

    def recur(self, s, res, path, index, depth, length):
        # 如果已经取了三段，还有s字符串还有剩余，直接返回
        if depth == 4 and length > 0:
            return
        # 如果已经取了三段，并且s字符串没有剩余，说明当前结果有效，把当前结果添加到最终结果之中
        # 注意要去掉最后一个点号
        if depth == 4 and length == 0:
            res.append(path[:-1])
        # 每次都可以取1个，或者2个，或者3个字符.
        for i in range(1, 4):
            # 如果当前已经没有字符剩余，跳出循环
            if length <= 0:
                break
            # IP地址的每一段不能以0开头
            if s[index] == '0'and i != 1:
                continue
            # IP地址的每一段只能小于等于255
            if i == 3 and int(s[index:index+i]) > 255:
                break
            # 选择IP地址的下一段
            self.recur(s, res, path+s[index:index+i] +
                       ".", index+i, depth+1, length-i)


if __name__ == "__main__":
    so = Solution()
    res = so.restoreIpAddresses("111111111111111111111")
    print(res)
