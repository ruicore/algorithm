# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-08 11:59:57
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-08 12:23:10


class Solution:
    def canWinNim(self, n: 'int') -> 'bool':
        # 如果是4的倍数，一定会失败
        if not n % 4: return False
        # 返回成功
        return True