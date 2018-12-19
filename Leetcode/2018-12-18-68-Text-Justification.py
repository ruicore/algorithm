# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-18 22:18:40
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-19 11:02:22

from pprint import pprint


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        wordsnum, nums, count, res, sequence = len(words), 0, 0, [], []
        if not wordsnum:
            return None
        i = 0
        while i < wordsnum:
            # 记录当前的所有索引
            sequence.append(i)
            # 记录当前已经占据的字符个数
            count += len(words[i])+1
            # 记录当前的单词个数
            nums += 1
            # 如果当前占据的字符个数已经超过了最大宽度
            if count >= maxWidth:
                # 如果是严格超出了一个单词
                if count >= maxWidth+2:
                    # 当前已经占据的宽度减去最后一次添加的单词长度，减去一个空格
                    count = count - 1 - len(words[i])
                    # 单词个数减一
                    nums = nums - 1
                    # 单词索引回退一个
                    i = i-1
                    # 数组弹出最后一个单词的索引
                    sequence.pop()
                # 空格字符的个数 = 最大宽度 - 所有单词所占据的个数
                space = maxWidth - (count - nums)
                # 如果当前行不止一个单词
                if nums > 1:
                    # 每个单词（除去最后一个单词，因为它不需要占据空格）能够被平均分配的空格
                    evensapce = space//(nums-1)
                    # 剩余的空格数，这些空格将从前往后，依次分配给每个单词，每个单词分配一个空格，直到所有的空格都分配完为止
                    lastspace = space % (nums-1)
                else:
                    # 如果只有一个单词，则所有的空格都将被分配给它
                    lastspace = space
                line = ''
                # 从前往后为每一个单词分配空格（最后一个不分配）
                for index in sequence[:-1]:
                    line += words[index]+' '*evensapce
                    if lastspace > 0:
                        line += ' '
                        lastspace -= 1
                # 填入最后一个单词：在单词个数不止一个的情况下lastspace==0，在只有一个单词的情况下lastspace可能不为0
                # 如果单词长度 == maxWidth，即使只有一个单词，lastspace也为零，所以说"在只有一个单词的情况下lastspace可能不为0"
                line += words[sequence[-1]]+" "*lastspace
                # 在结果数组中添加当前结果
                res.append(line)
                # 重置 nums, count, sequence
                nums, count, sequence = 0, 0, []
                del line
            i += 1
        if sequence:
            line = ''
            for index in sequence:
                line += words[index]+' '
            line += ' '*(maxWidth - count)
            res.append(line)
            del line

        return res


if __name__ == "__main__":
    so = Solution()
    res = so.fullJustify(
        ["What", "must", "be", "acknowledgment", "shall", "be"], 16)
    pprint(res)
