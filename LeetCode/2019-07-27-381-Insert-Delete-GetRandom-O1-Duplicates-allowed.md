# LeetCode 381. Insert Delete GetRandom O1 Duplicates allowed

## Description

Design a data structure that supports all following operations in average O(1) time.

Note: **Duplicate elements are allowed**.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

```py
// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
```

## 描述

设计一个支持在平均 时间复杂度 O(1) 下， 执行以下操作的数据结构。

注意: **允许出现重复元素**。

insert(val)：向集合中插入元素 val。
remove(val)：当 val 存在时，从集合中移除一个 val。
getRandom：从现有集合中随机获取一个元素。每个元素被返回的概率应该与其在集合中的数量呈线性相关。
示例:

```py
// 初始化一个空的集合。
RandomizedCollection collection = new RandomizedCollection();

// 向集合中插入 1 。返回 true 表示集合不包含 1 。
collection.insert(1);

// 向集合中插入另一个 1 。返回 false 表示集合包含 1 。集合现在包含 [1,1] 。
collection.insert(1);

// 向集合中插入 2 ，返回 true 。集合现在包含 [1,1,2] 。
collection.insert(2);

// getRandom 应当有 2/3 的概率返回 1 ，1/3 的概率返回 2 。
collection.getRandom();

// 从集合中删除 1 ，返回 true 。集合现在包含 [1,2] 。
collection.remove(1);

// getRandom 应有相同概率返回 1 和 2 。
collection.getRandom();
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


### 思路

* 基本思路同上一题，使用数组来存储元素，使用字典来存储元素和元素在数组中的位置。
* 字典结构：健为元素 val，值为一个 list，存储 val 在数组中的不同位置的索引。
* 数组结构：数组中的每一个元素为一个二元元祖；元祖第一个值为 val，第二值为这个 val 在对应的字典 list 中的索引。
* 例如，对 2，3，4，2，3，3，2 执行插入操作，得到如下的字典和数组。
```py
dicts = {2: [0, 3, 6], 3: [1, 4, 5], 4: [2], }
array = [(2, 0), (3, 0), (4, 0), (2, 1), (3, 1), (3, 2), (2, 2)]
```
* 插入操作：检查元素 val 是否在字典中，如果不在：记此时数组长度为 length = len(arary),在字典中新增一条记录 {val:[ length ]},在数组 array 中 append 一条记录 (val,0),0 表示 val 在字典对应的 list 中为 0 号元素；如果存在：记此时数组长度为 lenght = len(array), 记此时 val 在字典中对应 list 的长度为 val_lenght,在字典 val 对应的 list 中 append 一条记录 length，在数组中 append 一条记录 (val,val_length)。
* 删除，删除 val 的最后一个元素，记 val_last_index 为 val 对应字典中 list 的最后一个值；记录数组中最后一个元素 last_num 在对应字典list中的 引为 index_last_num（即 arry\[-1]\[1]），将数组中 val_last_index 位置的值与最后一个元素交换，删除最后一个元素；将字典中 last_num 对应 list 索引为 index_last_num 位置的值置为 val_last_index；如果此时 val 对应字典中的 list 为空，则删除字典中的健值对；
* 随机返回：使用 random 函数，随机返回数组中的一个元素的 0 号位的值。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-07-27 15:43:51
# @Last Modified by:   何睿
# @Last Modified time: 2019-07-27 18:14:22

import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = {}
        self.array = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """

        index = self.index
        array = self.array
        iscontain = False

        if val not in index:
            index[val] = []
            iscontain = True

        last_index = len(index[val])
        index[val].append(len(array))
        array.append((val, last_index))

        return iscontain

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        index = self.index
        array = self.array

        if val not in index:
            return False

        val_last_index = index[val][-1]

        last_tuple = array[-1]
        last_index = last_tuple[1]
        last_num = last_tuple[0]

        array[val_last_index], array[-1] = array[-1], array[val_last_index]

        index[last_num][last_index] = val_last_index

        del array[-1]
        del index[val][-1]

        if not index[val]:
            del index[val]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.array)[0]
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-07-27-381-Insert-Delete-GetRandom-O1-Duplicates-allowed.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-381-insert-delete-getrandom-o1-duplicates-allowed/) ，作者信息和本声明.
