# 43. Multiply Strings

## Description

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

## 描述

给定两个表示为字符串形式的非负整数num1和num2，返回num1和num2的乘积，也表示为字符串形式。

例:输入 num1 = "2", num2 = "3",输出 "6" 输入 num1 = "123",num2 = "456", 输出"56088"

注意：

>* 字符串num1和num2的长度都小于110
>* 字符串num1和num2都只包含数字0-9
>* 字符串num1和num2起始都不会为0,除了num1和num2只有一个字符0本身的情况
>* 不能使用任何函数自带得乘法运算也不能使用字符串转换为整数的函数
  
### 思路

回顾乘法的运算法则,如下图

![乘法运算法则示例一](https://wp.me/aaizn9-N1)

>* 如上图所示，我们把两个数右对齐，依次排好，从右至左依次进行运算，每次运算结果按位置对其，最后进行加和，这就完成了乘法运算
>* 再给出一个示例，如下图

![乘法运算法则示例二](https://wp.me/aaizn9-N2)

```python
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        lennum1, lennum2 = len(num1), len(num2)
        result = [0]*(lennum1+lennum2)

        # 共有两层
        for i in range(lennum1-1, -1, -1):
            for j in range(lennum2-1, -1, -1):
                # 首先计算乘积，注意用ASCII码的方式转换为数值
                temp = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
                # 计算所得应和i+j位置求和
                _sum = temp+result[i+j+1]
                # 第i+j个位置
                result[i+j+1] = _sum % 10
                # 第i+j-1个位置,此代码为python3，注意使用'//'等号进行运算，例5/2=2.5,5//2=2
                result[i+j] += _sum//10
        # 将数字转换为字符串
        result = [str(i) for i in result]
        return ''.join(result[1:]) if result[0] == "0" else ''.join(result)
```

[源文件地址在这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-05-43-Multiply-Strings.py)
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-43-multiply-strings/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
