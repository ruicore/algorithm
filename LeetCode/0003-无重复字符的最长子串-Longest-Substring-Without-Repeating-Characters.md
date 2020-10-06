
### 题目描述

* > 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

```py
示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

* 使用滑动窗格，滑动窗格本质的上是一个队列，因此我们维护一个队列即可。
* 对列中的元素不重复，在队列尾部新增一个元素之前，检查该元素是否已经在队列中存在；若已经存在，则从队首开始移除元素，直到移除到重复元素的位置【重复元素本身也需要移除】。
* 判断新增的元素是否在队列中存在，我们维护一个 hash set，这样可以达到 O(1) 的时间复杂度。
* 在移除元素之前，记录当前队列的长度，和上一次最大队列长度作比较，更新最大长度为当前的最大值。

```py
from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 新建一个队列
        queue = deque([])
        # 队列中的所有元素
        visited = set()
        # 最长子串长度
        max_count = 0

        for char in s:
            # visited 中的元素和 deque 中的元素只有位置不同
            # 如果需要新增在队尾的元素 char 在 queue 中已经存在
            if char in visited:
                # 从队列首部开始移除元素，直到遇到重复的元素为止
                while deque and char in visited:
                    visited.remove(queue.popleft())
            visited.add(char)
            queue.append(char)
            # 更新最长子串的长度
            max_count = max(len(queue), max_count)
        return max_count
```

## 与我联系

* 如果有任何问题，欢迎交流联系

<img src="../wechat.jpeg" width = "220" align=center />