# LeetCode 68. Text Justification

## Description

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

## 描述

给定一个单词数组和一个宽度maxWidth，格式化文本，使每行具有正确的maxWidth字符并完全（左和右）对齐。

你应该使用贪婪的方式处理每一行; 也就是说，在每行中包含尽可能多的单词。 必要时填充额外的空格，以便每行具有正确的maxWidth字符。

单词之间的额外空格应尽可能均匀分布。 如果一行上的空格数不均匀分配，则左侧的空插槽将分配比右侧插槽更多的空格。

对于最后一行文本，它应该是左对齐的，并且在单词之间不插入额外的空格。

注意：

单词定义为仅由非空格字符组成的字符序列。
每个单词的长度保证大于0且不超过maxWidth。
输入数组字包含至少一个字。

### 思路

* 这道题并没有考察特别的算法，按照题目要求处理即可.
* 题意是给定一些单词，给定一行的最大宽度maxWidth（即最多能够放多少个字符），让把这些单词按行放置，
* 要求：尽可能多的放置单词在每一行中，每个单词之间空格隔开，空格均匀分布，且左边的空格数大于右边的空格数
* 例如一行有四个单词，四个单词占据了9个字符，一行允许有16个字符：则四个单词需要三个间隔，三个间隔共占据7个空格
* 每个间隔的空格数为：3，2，2
* 我们使用nums表示单词个数，count来表示已经占据的字符个数,words数组中从下标i到j的单词一共需要占据如下公式个字符：

$$ count[i:j] = \sum_{k=i}^j{(len(words[k])+1)}$$

* 因为每个单词至少都要一个空格(最后一个单词是不需要的空格的，单独处理)
* 当count大于等于最大宽度的时候，我们开始填入一行
* 如果count>maxWidth+2:表示count中的最后一个单词需要填在下一行，我们让nums减去1，count减去最后一个单词与一个空格的长度.
* evenspace表示每个单词（除去最后一个单词）都能分配到的字符，lastspace表示剩余的字符
* 我们为单词分配一个evenspace个数的空格字符串，然后检查lastspace是否大于0，若是则再给单词分配一个空格.
* 我们最后再把最后一个单词填入当前行

```python
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
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-18-68-Text-Justification.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-68-text-justification/)，欢迎转载，转载需保留文章来源，作者信息和本声明.