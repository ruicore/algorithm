
### 题目描述

> 给定一个整数数组 ```nums``` 和一个目标值 ```target```，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
>
>

**1. 第一种最直接的思路是枚举每一种组合**，看看他们是否满足题意，我们需要用到两个 for 循环。
* TwoSum I 暴力版本
```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 数组长度
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # 不存在这么两个数
        return [-1, -1]
```
* 这种情况的时间复杂度是 O(N^2)，空间复杂度是 O(1)。


**2. towSum 的另外一种思路是使用 hash 表**，在上面的第二个循环中，我们是要找另一个数是否也在给定的数组中，这种判断元素是否在集合中的操作适合用 hash 表来做。
* TwoSum I 哈希表版本
```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 构建一个字典，键为 nums 中的数字，值为该数字在数组中的位置
        # 使用 python 内置函数 enumerate
        num_pos_dict = {num: pos for pos, num in enumerate(nums)}
        # 遍历数组，同时获取 `位置` 和该 `位置的值`
        for pos, num in enumerate(nums):
            # 另一个数字
            other = target - num
            # 另一个数字可能在 num_pos_dict 中的值
            other_pos = num_pos_dict.get(other, -1)
            # 如果 other 存在并且不是 num 本身
            if other in num_pos_dict and other_pos != pos:
                return [pos, other_pos]
        # 结果不存在
        return [-1, -1]
```

## 与我联系

* 如果有任何问题，欢迎交流联系

<img src="../wechat.jpeg" width = "220" align=center />