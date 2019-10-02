# LeetCode 406. Queue Reconstruction by Height

## Description

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

```py
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```

## 描述

假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

```py
输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 对原数组进行排序，第一个值相同的按第二个大小进行排序。
* 假设一组数为 a = \[i,j]，那么如何确定 j 的位置？j 表示 a 所在位置前面的所有数对中，大于等于 i 的数 有 j 个。
* 于是就有了第一种思路：我们生命一个数组 res，res 的每一个位置都置为 None，我们从前向后遍历数组，统计 \[h,k] 中大于等于 i 和当前位置为 None 的个数，当统计个数达到 i 时，我们从这里往后找第一个为 None 的位置，此时 a 应当被放在这里；

```py

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = [None for _ in range(len(people))]
        for pair in sorted(people):
            h, k = pair[0], pair[1]
            if k == 0:
                idx = self.first_not_None(result, -1)
            else:
                idx = self.find_idx(result, h, k)
            result[idx] = pair
        return result

    def find_idx(self, result, h, k):

        cnt, start = 0, -1

        for start, people in enumerate(result):
            if people is None or people[0] >= h:
                cnt += 1
            if cnt == k:
                break

        return self.first_not_None(result, start)

    def first_not_None(self, result, start):
        for i in range(start + 1, len(result)):
            if result[i] is None:
                return i
```

* 第二种思路，我们按照 \[h,k] 中，h大的排前面，h 相同的 k  小的排前面；
* 声明一个数字 result，我们从前向后遍历数组，对于数组中的一对数 a，由于 a = \[i,j] 前面的数都比 a 大（或等于），所以只需要把 a 插入到 i 位置即可；

```py
class Solution:
    def reconstructQueue2(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        result = []
        for p in people:
            result.insert(p[1], p)
        return result
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-10-02-406-Queue-Reconstruction-by-Height.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-406-queue-reconstruction-by-height/) ，作者信息和本声明.
