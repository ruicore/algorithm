# LeetCode 42 Trapping Rain Water

## Description

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example: Input: [0,1,0,2,1,0,1,3,2,1,2,1] Output: 6.

## 描述

给定n个非负整数，每个非负整数表示一个宽度为1的柱子，计算下雨后能够捕获多少水.

![rainwatertrap](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

上面的柱状图由数组[0,1,0,2,1,0,1,3,2,1,2,1]表示。在这种情况下，蓝色部分表示的6个单位雨水可以被柱子围住.

例: 输入: [0,1,0,2,1,0,1,3,2,1,2,1] 输出: 6.

### 思路一

>* 我们观察图中所示的例子，一每一个柱子为思考点，想一下它能够装的水是由什么决定的呢？
>* 以编号为5的柱子(令示例中的数组为a，即a[5]=0)为例，观察发现：
>* 每个柱子能够困住的水是由以柱子所在位置为基点，此基点左边所有柱子中最大值和此基点右边所有柱子中最大值共同决定的，即：
>* **A[5]能困住的水 = Min{A[5]左边所有柱子的最大值，A[5]右边所有柱子的最大值} - A[5]**.

有了这个思路，就有了第一种解决方案：

>* 从左往右遍历数组，找到每一个值左边的最大值，用一个数组记录下来
>* 从右往左遍历数组，找到每一个值右边的最大值，用一个数组记录下来
>* 能够装的水=min(该位置左边最大值，该位置右边最大值)-该位置的值
>* 时间复杂度O(n)，空间复杂度O(n)

```python
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 数组的长度，如果数组长度小于等于2，则一定装不了水
        length = len(height)
        if length <= 2:
            return 0
        # 声明两个数组，分别用于存储左边的最大值和右边的最大值
        leftmax, rightmax = [0]*length, [0]*length
        temp, water = 0, 0
        # 找到左边的最大值
        for index in range(length):
            if height[index] >= temp:
                temp = height[index]
            leftmax[index] = temp
        # 找到右边的最大值
        temp = 0
        for index in range(length-1, -1, -1):
            if height[index] >= temp:
                temp = height[index]
            rightmax[index] = temp
        # 遍历求和
        for index in range(length):
            water += min(leftmax[index], rightmax[index])-height[index]
        return water
```

### 思路二

>* 在思路一中，我们从每一个柱子出发，思考到决定每个柱子能容多少水是由该柱子左边最高的柱子和该柱子右边最高的柱子共同决定的，
>* 因此我们为每一个柱子求得其左边最高的柱子和右边最高的柱子，这样空间复杂度是O(n)。但是我们反过来想，其实有很多柱子的左右最高柱.
>* 是一样的，也就是说有很多柱子左右最高柱子使用同一对柱作为最高柱.于是，我们可以反过来，看在左右最高柱确定的情况下，哪些柱子以这两个柱为最高柱.
>* 我们需要四个值，leftmax:左边最高柱子的值,left:当前左边柱子的索引，rightmax：右边最高柱子的值，right:当前右边柱子的值.画图最直观.

![图1左低右高](https://www.ruicore.cn/wp-content/uploads/2018/12/20181203leetcode42-001.svg)

>* 如上图1，左边的最高值leftmax和右边的最高值rightmax已经确定，索引为left和right的柱子之间还有柱子.
>* 如果leftmax<=rightmax,索引为left的柱子能够装的水就确定了，为leftmax-left柱子自身的高度，而索引为right的柱子还不确定.
>* 因为left和right中间无论有什么情况的柱子:如果有比left高的柱子，left装水量由左边矮的leftmax确定，为leftmax-自身高度.
>* 如果有比left矮的柱子,但是由于rightmax比较大，left也可以达到leftmax的高度.
>* 但是right并不能确定,如果left和right有更高的柱子，right就可以装水，如果没有，right就无法装水.
>* 反过来，如果leftmax>rightmax,则right就能确定,而left不能确定.如下图2.

![图2左高右低](https://www.ruicore.cn/wp-content/uploads/2018/12/20181203leetcode42-002.svg)

有了这个思路就有了第二个解决方案

>* 更新左边柱子的最大值leftmax.
>* 更新右边柱子的最大值rightmax.
>* 如果leftmax<=rightmax,则该柱子出水量为leftmax-自身高度,left向右走一步.
>* 如果leftmax>rightmax,则该柱子出水量为rightmax-自身高度,rihgh向左走一步.
>* 时间复杂度O(n)，空间复杂度O(1)

```python
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 数组的长度，如果数组长度小于等于2，则一定装不了水
        length = len(height)
        if length <= 2:
            return 0
        # 声明五个变量，总水量，左边最高柱的值，右边最高柱的值，左边柱子的索引，右边柱子的索引
        water, leftmax, rightmax, left, right = 0, 0, 0, 0, length-1
        # 只有左边索引小于右边索引才执行
        while left < right:
            # 更新左边最高柱子
            if height[left] > leftmax:
                leftmax = height[left]
            # 更新右边最高柱子
            if height[right] > rightmax:
                rightmax = height[right]
            # 如果是左低右高(包括左右一样高)的情形
            if leftmax <= rightmax:
                water += leftmax-height[left]
                left += 1
            # 如果是左高右低这种情况
            elif rightmax < leftmax:
                water += rightmax-height[right]
                right -= 1
        return water
```

### 优化空间

>* 在思路二实现的代码中，前面两个if条件每次都会判断，实际上，如果第一个条件满足那么第二个条件就一定不会满足.
>* 同样的道理，如果第二个条件满足，那么第一个条件就不会满足，因此，我们可以把代码改写成下面的形式.

```python
class Solution3:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 数组的长度，如果数组长度小于等于2，则一定装不了水
        length = len(height)
        if length <= 2:
            return 0
        # 声明五个变量，总水量，左边最高柱的值，右边最高柱的值，左边柱子的索引，右边柱子的索引
        water, leftmax, rightmax, left, right = 0, 0, 0, 0, length-1
        # 只有左边索引小于右边索引才执行
        while left < right:
            # 首先判断是什么情形,如果是左低右高这种情形
            # 这里隐藏了一点是当height[left] <= height[right]时，leftmax一定小于等于 height[right]
            if height[left] <= height[right]:
                if leftmax > height[left]:
                    water += leftmax-height[left]
                else:
                    leftmax = height[left]
                left += 1
            # 同理，当height[left]>height[right]时，rightmax一定小于等于height[left]
            if height[left] > height[right]:
                if rightmax > height[right]:
                    water += rightmax-height[right]
                else:
                    rightmax = height[right]
                right -= 1
        return water
```

©本文首发于[何睿的博客](https://www.ruicore.cn/)，欢迎转载，转载需保留文章来源，作者信息和本声明.