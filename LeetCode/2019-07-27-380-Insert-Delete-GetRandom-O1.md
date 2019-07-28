# LeetCode 380. Insert Delete GetRandom O1

## Description

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

```py
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
```

## 描述

设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。

insert(val)：当元素 val 不存在时，向集合中插入该项。
remove(val)：元素 val 存在时，从集合中移除该项。
getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
示例 :

```py
// 初始化一个空的集合。
RandomizedSet randomSet = new RandomizedSet();

// 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomSet.insert(1);

// 返回 false ，表示集合中不存在 2 。
randomSet.remove(2);

// 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomSet.insert(2);

// getRandom 应随机返回 1 或 2 。
randomSet.getRandom();

// 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomSet.remove(1);

// 2 已在集合中，所以返回 false 。
randomSet.insert(2);

// 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
randomSet.getRandom();
```
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-delete-getrandom-o1
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 使用字典和数组这两种结构。
* 数组存储数值 val，字典中存储数值 val 和 val 在字典中的索引。
* 插入操作：如果要插入的数 val 已经在字典中（此操作时间复杂度为 O（1）），直接返回；如果不在数组中，将 val 放入数组末尾，在字典中新增健值对，健为 val ，值为 val 在数组中的索引。
* 删除操作：将要删除元素 val 和数组中的最后一个元素 num 交换位置；更新字典中 num 的值；删除数组的最后一个元素，删除字典中的 val 健值对；
* 随机返回：使用 random 函数，随机返回数组中的一个元素

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-07-27 13:59:36
# @Last Modified by:   何睿
# @Last Modified time: 2019-07-27 14:24:11

import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = dict()
        self.array = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.index:
            return False
        self.index[val] = len(self.array)
        self.array.append(val)

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.index:
            return False

        last_num = self.array[-1]
        val_index = self.index[val]

        self.index[val], self.index[last_num] = self.index[last_num], self.index[val]
        self.array[val_index] = self.array[-1]
        del self.index[val]
        del self.array[-1]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.array)
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-07-27-380-Insert-Delete-GetRandom-O1.py), 此代码于 2019-07-27 向 LeetCode 提交通过。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-380-insert-delete-getrandom-o1/) ，作者信息和本声明.
