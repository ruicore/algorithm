# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-22 14:29:05
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-22 17:21:06


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row, col = len(board), len(board[0])
        ischecked = [[False for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if self.check(i, j, 0, ischecked, board, word):
                    return True
        return False

    def check(self, row, col, index, ischecked, board, word):
        # 如果index等于word的长度，说明此时已经找完所有的字符，只有前面的字符通过了才会找下一个字符
        # 说明所有的字符都通过，返回Ture
        if index == len(word):
            return True
        # 如果越界或者当前位置已经检查过了，则返回False
        if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0 or ischecked[row][col]:
            return False
        # 如果当前位置没有被占用并且当前位置和要检查的字符不等，返回False
        if not ischecked[row][col] and board[row][col] != word[index]:
            return False
        # 通过了上面的所有条件，说明此时要检查的字符是相等的
        # 记录此时的位置，表示已经检查过了.
        ischecked[row][col] = True
        # 检查右边一个字符
        if self.check(row, col+1, index+1, ischecked, board, word):
            return True
        # 检查下边一个字符
        if self.check(row, col-1, index+1, ischecked, board, word):
            return True
        # 检查左边一个字符
        if self.check(row+1, col, index+1, ischecked, board, word):
            return True
        # 检查右边一个字符
        if self.check(row-1, col, index+1, ischecked, board, word):
            return True
        # 清空已经检查的情况
        ischecked[row][col] = False
        return False


if __name__ == "__main__":
    so = Solution()
    res = so.exist([["a"]], "ab")
    print(res)
