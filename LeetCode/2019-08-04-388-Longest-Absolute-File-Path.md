# LeetCode 388. Longest Absolute File Path

## Description

Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

```shell
dir
    subdir1
    subdir2
        file.ext
```
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

```shell
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.

## 描述

假设我们以下述方式将我们的文件系统抽象成一个字符串:

字符串 "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" 表示:

```shell
dir
    subdir1
    subdir2
        file.ext
```
目录 dir 包含一个空的子目录 subdir1 和一个包含一个文件 file.ext 的子目录 subdir2 。

字符串 "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 表示:

```shell
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```
目录 dir 包含两个子目录 subdir1 和 subdir2。 subdir1 包含一个文件 file1.ext 和一个空的二级子目录 subsubdir1。subdir2 包含一个二级子目录 subsubdir2 ，其中包含一个文件 file2.ext。

我们致力于寻找我们文件系统中文件的最长 (按字符的数量统计) 绝对路径。例如，在上述的第二个例子中，最长路径为 "dir/subdir2/subsubdir2/file2.ext"，其长度为 32 (不包含双引号)。

给定一个以上述格式表示文件系统的字符串，返回文件系统中文件的最长绝对路径的长度。 如果系统中没有文件，返回 0。

说明:

文件名至少存在一个 . 和一个扩展名。
目录或者子目录的名字不能包含 .。
要求时间复杂度为 O(n) ，其中 n 是输入字符串的大小。

请注意，如果存在路径 aaaaaaaaaaaaaaaaaaaaa/sth.png 的话，那么  a/aa/aaa/file1.txt 就不是一个最长的路径。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-absolute-file-path
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 涉及到文件路径的问题可以首先考虑使用栈。
* 我们用一个栈，栈中记录文件夹的信息，栈的每一个元素为包含两个元素的二元组合。组合记录了文件路径的深度，从跟节点到当前节点的路径字符个数。
* 我们用换行符 ‘\n’ 对字符串进行拆分，然后遍历字符串，我们用 max_length 记录当前的最长字符串个数。
* 统计每个字符串中 ‘\t’ 的个数，用于计算层级。如果当前字符串表示的是路径（路径中含有 '.' 号 ），我们对栈进行检查，pop 出栈中深度大于等于当前路径的路径，然后将当前路径押入栈。
* 如果当前字符串表示的是文本，我们获取当前路径的字符串个数，然后和 max_length 进行比较，更新 max_length。
* 最后返回 max_length。

```py

class Solution(object):
    def lengthLongestPath(self, input):

        max_length = 0
        dot, blank = '.', ''
        stack = [(-1, 0)]  # -1 表示目录深度，0 表示当前所有字符串的长度

        for name in input.split("\n"):
            level = name.count('\t')
            name = name.replace('\t', blank)
            # 去当前的目录深度
            while stack and level <= stack[-1][0]:  # 如果一样深，或者当前目录的层级更浅
                stack.pop()
            if dot not in name:  # 如果是目录
                stack.append((level, len(name) + stack[-1][1] + 1))
            else:  # 如果是文件
                max_length = max(max_length, len(name) + stack[-1][1])

        return max_length
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-08-04-388-Longest-Absolute-File-Path.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-388-longest-absolute-file-path/) ，作者信息和本声明.
